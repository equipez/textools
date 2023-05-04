## Makefile
## Copyright 2023 Tom M. Ragonneau and Zaikun Zhang
LC := latexmk
LCFLAGS := -file-line-error -halt-on-error -interaction=nonstopmode

all: pdf bib

pdf: *.tex
	$(LC) $(LCFLAGS) $^

bib: pdf *.bib
	getbib

.PHONY: clean
clean:
	$(LC) -c
	rm -f *.log *.aux *.bbl *.blg *.fdb_latexmk *.fls *.out *.synctex.gz *.toc *.bcf  \
		*.synctex.gz\(busy\) *.synctex\(busy\) *.synctex.gz\(busy\)* *.synctex\(busy\)*
