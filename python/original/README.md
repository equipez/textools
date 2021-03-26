# bibtex-check
Do you also hate revising the bibliography of a paper? Then, this little piece of software may somewhat ease your life.

BibTeX Check is a small Python script that goes through a list of references and checks if certain required fields are available, for instance, if each publication is assigned a year or if a journal article has a volume and issue number. Moreover, it allows for first consistency checks of names of conference proceedings and you can easily extend it to support further of such checks. The results are printed to an html file, which includes links to Google Scholar, DBLP, etc. for each flawed reference. These links help retrieving missing information and correcting the entries efficiently.

But please note that BibTeX Check is not a BibTeX validator. And in the current version, it might not yet be able to parse every valid bib file. The software targets the specific needs of Computer Scientist, but may be applicable in other fields as well.

The code is not complicated. Feel free to modify it to your needs!

**The code was originally written by Fabian Beck. Code was provided with an MIT license. Thanks**

URL: [code.google.com/archive/p/bibtex-check/](https://code.google.com/archive/p/bibtex-check/)

## Getting Started
Just copy the file bibtex_check.py into a directory with write permission, change the path of test.bib to the bib file you want to test, and run the script with Python 3.

You may also provide an additional aux file (these are created when compiling a tex document). Then, the check of the bib file becomes restricted to only those entries that are really cited in the tex document.

The html output is tested with Firefox and Chrome, but the current version does not properly work with Internet Explorer.

Screenshot
