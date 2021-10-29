import re
import sys
from typing import Iterable, Union

TITLE_REGEX = re.compile("^.*(?:chapter|section)\\{(.+?)\\}.*$")

def main():
    for line in bannerize(get_lines()):
        print(line, end="")


def get_lines() -> Iterable[str]:
    if len(sys.argv) >= 2:
        return sys.argv[1:]

    return (line for line in sys.stdin)


def bannerize(lines: Iterable[str]) -> Iterable[str]:
    for line in lines:
        if get_title(line):
            for banner_line in new_banner_stream(line):
                yield banner_line
        yield line


def new_banner(line: str) -> str:
    return "\n".join(new_banner_stream(line))


def new_banner_stream(line: str) -> Iterable[str]:
    title = get_title(line)

    if not title:
        print("Could not parse title.")
        quit()

    rule = new_rule(len(line.strip()))

    yield rule
    yield new_title_line(line, title)
    yield rule


def get_title(section_line: str) -> Union[str, None]:
    title_matches = TITLE_REGEX.findall(section_line)

    if not title_matches or len(title_matches) == 0:
        return None

    return title_matches[0]


def new_rule(length: int) -> str:
    return "%" + "=" * (length - 2) + "%\n"


def new_title_line(section_line: str, title: str) -> str:
    section_line_width = len(section_line.strip())

    title_start = section_line_width // 2 - len(title) // 2 - 1
    title_end = title_start + len(title)

    line_elems = ["%"]
    i = 0
    while i < section_line_width - 2:
        if i >= title_start and i < title_end:
            line_elems.append(title)
            i += len(title)
        else:
            line_elems.append(" ")
            i += 1
    line_elems.append("%\n")

    return "".join(line_elems)


if __name__ == "__main__":
    main()

