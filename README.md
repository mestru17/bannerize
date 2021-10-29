# bannerize
bannerize is a command line script that reads lines of LaTeX markup (either as program arguments or from stdin) and inserts comment banners for each section and chapter. This makes it easier to see where one section ends and the next one begins on long LaTeX documents.

## Example

Before:
```latex
\chapter{Analysis and Solutions}\label{ch:AnalysisAndSolutions}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum faucibus vitae purus vitae varius. Aliquam rutrum odio luctus metus luctus sodales. Mauris at urna nec felis varius cursus non id leo. Phasellus id ex ac orci euismod imperdiet eget feugiat libero. Sed convallis efficitur convallis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sit amet ante non arcu suscipit lobortis. Sed vitae mollis nunc, non dictum lorem. In convallis ex nec neque malesuada, eget finibus augue interdum. Etiam eget placerat erat. Mauris ut viverra risus.

\section{Analysis}label{sec:AnalysisAndSolutions:Analysis}

\subsection{Use Cases}label{sec:AnalysisAndSolutions:Analysis:UseCases}
Sed id nunc rutrum ipsum scelerisque molestie. Nunc pharetra mauris vitae nisl ultricies, nec feugiat lectus interdum. Donec tempor a velit sed commodo. Nulla euismod metus nisi. Aenean commodo non turpis non consequat. Vivamus gravida ligula eget metus interdum, a dapibus purus molestie. Phasellus nec ultrices risus. Nunc imperdiet urna erat, in commodo purus interdum nec. Aliquam erat volutpat. Sed tincidunt nulla non mollis venenatis.

\cref{tab:AnalysisAndSolutions:Analysis:UseCases:UseCases} gives a quick overview of all the use cases.

\begin{table}[htbp]
    \caption{Use Cases}
    \centering
    \input{tables/AnalysisAndSolutions/UseCases}
    \label{tab:AnalysisAndSolutions:Analysis:UseCases:UseCases}
\end{table}

\subsection{Requirements}label{sec:AnalysisAndSolutions:Analysis:Requirements}

\subsection{Prioritization}label{sec:AnalysisAndSolutions:Analysis:Prioritization}

\section{Solutions}label{sec:AnalysisAndSolutions:Solutions}
```

After:
```latex
%=============================================================%
%                   Analysis and Solutions                    %
%=============================================================%
\chapter{Analysis and Solutions}\label{ch:AnalysisAndSolutions}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum faucibus vitae purus vitae varius. Aliquam rutrum odio luctus metus luctus sodales. Mauris at urna nec felis varius cursus non id leo. Phasellus id ex ac orci euismod imperdiet eget feugiat libero. Sed convallis efficitur convallis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec sit amet ante non arcu suscipit lobortis. Sed vitae mollis nunc, non dictum lorem. In convallis ex nec neque malesuada, eget finibus augue interdum. Etiam eget placerat erat. Mauris ut viverra risus.

%========================================================%
%                        Analysis                        %
%========================================================%
\section{Analysis}label{sec:AnalysisAndSolutions:Analysis}

%=====================================================================%
%                              Use Cases                              %
%=====================================================================%
\subsection{Use Cases}label{sec:AnalysisAndSolutions:Analysis:UseCases}
Sed id nunc rutrum ipsum scelerisque molestie. Nunc pharetra mauris vitae nisl ultricies, nec feugiat lectus interdum. Donec tempor a velit sed commodo. Nulla euismod metus nisi. Aenean commodo non turpis non consequat. Vivamus gravida ligula eget metus interdum, a dapibus purus molestie. Phasellus nec ultrices risus. Nunc imperdiet urna erat, in commodo purus interdum nec. Aliquam erat volutpat. Sed tincidunt nulla non mollis venenatis.

\cref{tab:AnalysisAndSolutions:Analysis:UseCases:UseCases} gives a quick overview of all the use cases.

\begin{table}[htbp]
\caption{Use Cases}
\centering
\input{tables/AnalysisAndSolutions/UseCases}
\label{tab:AnalysisAndSolutions:Analysis:UseCases:UseCases}
\end{table}

%============================================================================%
%                                Requirements                                %
%============================================================================%
\subsection{Requirements}label{sec:AnalysisAndSolutions:Analysis:Requirements}

%================================================================================%
%                                 Prioritization                                 %
%================================================================================%
\subsection{Prioritization}label{sec:AnalysisAndSolutions:Analysis:Prioritization}

%==========================================================%
%                         Solutions                        %
%==========================================================%
\section{Solutions}label{sec:AnalysisAndSolutions:Solutions}
```

## Usage
`bannerize.py` writes the new LaTeX file to stdout:
```shell
$ cat somefile.tex | python3 bannerize.py > new_somefile.tex
```

It is also possible to copy the output directly to your clipboard (only works for WSL users) with the bash script:
```shell
$ cat somefile.tex | ./bannerize
```

