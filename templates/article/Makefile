## Makefile
## Copyright 2023 Tom M. Ragonneau and Zaikun Zhang
LC := latexmk
LCFLAGS := -file-line-error -halt-on-error -interaction=nonstopmode

pdf: *.tex
	$(LC) $(LCFLAGS) $^

bib: pdf *.bib
	getbib

all: pdf bib

.PHONY: clean
clean:
	$(LC) -c
	rm -f *.dvi *.log *.aux *.bbl *.blg *.fdb_latexmk *.fls *.out *.synctex.gz *.toc *.bcf  \
		*.synctex.gz\(busy\) *.synctex\(busy\) *.synctex.gz\(busy\)* *.synctex\(busy\)*
