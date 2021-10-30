#!/usr/bin/env python3

"""Bannerizes sections and chapters in LaTeX markdown when run as a script.

When not run as a script, this module mainly exports the bannerize() function,
which takes any iterable of lines and returns a new iterable with the same
lines but with injected banners. This makes it possible to use it with
practically any kind of input - i.e. files, stdin, lists, etc.

Script Example:
    echo "Bannerize somefile.tex and print it to stdout."
    cat somefile.tex | ./bannerize.py

Code Example:
    # Bannerize somefile.tex and print it to stdout.
    with open("somefile.tex", 'r') as f:
        for line in bannerize(f):
            print(line)
"""

from pathlib import Path
import re
import sys
from typing import Generator, Iterable, Union

TITLE_REGEX = re.compile("^.*(?:chapter|section)\\{(.+?)\\}.*$")


def _main():
    if len(sys.argv) >= 2 and sys.argv[1].endswith(".tex"):
        files = (Path(s) for s in sys.argv[1:])
        _bannerize_files(files)
    else:
        for line in bannerize(_get_lines()):
            print(line, end="")


def _bannerize_files(files: Iterable[Path]):
    for file in files:
        if is_latex_file(file):
            bannerize_file(file)
            print(f"Bannerized {file}.")
        else:
            print(f"Not a valid LaTeX file: {file}. Skipped.")


def _get_lines() -> Iterable[str]:
    """Returns a line iterable from program arguments if possible and stdin otherwise."""
    if len(sys.argv) >= 2:
        return sys.argv[1:]

    return (line for line in sys.stdin)


def is_latex_file(path: Path) -> bool:
    """Checks if a given path points to a valid existing LaTeX file."""
    return path.suffix == ".tex" and path.is_file()


def bannerize_file(file: Path):
    """Bannerizes a given LaTeX file.

    Replaces the given LaTeX file.

    Args:
        file: Path to a valid LaTeX file to bannerize.
    """
    swapfile = file.with_suffix(file.suffix + ".swp")

    with file.open("r") as f, swapfile.open("w+") as sf:
        for line in bannerize(f):
            sf.write(line)

    swapfile.replace(file)


def bannerize(lines: Iterable[str]) -> Generator[str, None, None]:
    """Transforms a line iterable into a generator with injected banners.

    Does not modify the given iterable besides iterating over it.

    Args:
        lines: Line iterable to inject banners into.

    Yields:
        The same lines that was given as input with injected lines as well.
    """
    for line in lines:
        if get_title(line):
            for banner_line in new_banner_stream(line):
                yield banner_line
        yield line


def get_title(section_line: str) -> Union[str, None]:
    """Attempts to extract the title from a given LaTeX section or chapter line.

    Args:
        section_line: LaTeX section or chapter line.

    Returns:
        The section/chapter title if the given line was valid and None otherwise.
    """
    title_matches = TITLE_REGEX.findall(section_line)

    if not title_matches or len(title_matches) == 0:
        return None

    return title_matches[0]


def new_banner_stream(line: str) -> Generator[str, None, None]:
    """Creates a banner generator for a given LaTeX section/chapter line.

    Args:
        line: A valid LaTeX section or chapter line.

    Yields:
        Each line of the banner.
    """
    title = get_title(line)

    if not title:
        print("Could not parse title.")
        quit()

    rule = new_rule(len(line.strip()))

    yield rule
    yield new_title_line(line, title)
    yield rule


def new_rule(length: int) -> str:
    """Creates a banner rule line with a given length.

    Args:
        length: The length of the rule.

    Returns:
        A new banner rule line with the given length.
    """
    return "%" + "=" * (length - 2) + "%\n"


def new_title_line(section_line: str, title: str) -> str:
    """Creates a banner title line.

    Args:
        section_line: A valid LaTeX section or chapter line.
        title: The title of the banner.

    Returns:
        A new banner title line with the given title and the same length as
        the given line.
    """
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
    _main()
