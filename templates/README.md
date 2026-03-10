This directory contains LaTeX templates for the team of Dr. Zaikun Zhang.

## Remarks

1. Before starting, under the directory containing the main TeX file, create a symbolic link named "ref.bib" to the universal BibTeX file, which should be a local copy of
https://github.com/equipez/bibliographie/blob/main/ref.bib .
2. If you do not have access to the above file, then put your BibTeX entries in `template.bib`.
3. By default, the template is in the draft mode. Remove the `draft` option in the
`\documentclass` command to switch to the final mode.
4. If you are a vim user, then try the [vim template](../vim/templates/article.tex). It should be equivalent to the current one.

## Usage

1. `latexmk` or `make` or `make pdf` to get the pdf file.
2. `make bib` to get the BibTeX file; make sure to set the document to the draft mode, i.e.,
   `\documentclass[draft]{article}`.
3. `make all` to compile everything and get the BibTeX file.
4. `latexmk -c` or `make clean` to clean up the directory.
