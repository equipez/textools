This directory contains LaTeX templates for the team of Dr. Zaikun Zhang.

Before starting, under the directory containing the main TeX file, create a symbolic link named "ref.bib" to the universal BibTeX file, which should be a local copy of
https://github.com/equipez/bibliographie/blob/main/ref.bib

Usage:

- `latexmk` or `make` or `make pdf` to get the pdf file.
- `make bib` to get the BibTeX file; make sure to set the document to the draft mode, i.e.,
   \documentclass[draft]{article}.
- `make all` to compile everything and get the BibTeX file.
- `make clean` to clean up the directory.
