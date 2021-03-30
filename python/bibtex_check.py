#!/usr/bin/env python
"""
bibtex_check checks bib files according to conventions and requirements in applied mathematics.
Developed based on bibtex_check (v0.2.0) by Fabian Beck released under the MIT license. The
original version by Fabian Beck is archived in ./original/.
"""

import sys
from optparse import OptionParser

# Parse options
usage = (
    sys.argv[0]
    + " [-b|--bib=<input.bib>] [-a|--aux=<input.aux>] [-o|--output=<output.html>] [-l|--latex] [-h|--help]"
)
parser = OptionParser(usage)
parser.add_option("-b", "--bib", dest="bibFile", help="Bib File", metavar="input.bib", default="")
parser.add_option("-a", "--aux", dest="auxFile", help="Aux File", metavar="input.aux", default="")
parser.add_option("-o", "--output", dest="htmlOutput", help="HTML Output File", metavar="output.html", default="bibtex_check.html")
parser.add_option("-l", "--latex", dest="bibLaTeX", help="Check BibLaTeX instead of BibTeX", action="store_true", default=False)
(options, args) = parser.parse_args()

# files
bibFile = options.bibFile
auxFile = options.auxFile
htmlOutput = options.htmlOutput
bibLaTeX = options.bibLaTeX

# links
libgenHref = "http://libgen.rs/search.php?req="
libgenArtHref = "http://libgen.rs/scimag/?q="
scholarHref = "http://scholar.google.com/scholar?hl=en&q="
googleHref = "https://www.google.com/search?q="
mathscinetHref = "https://mathscinet.ams.org/mathscinet/search/publdoc.html?co4=AND&pg4=AUCN&pg5=TI&r=1&s4=&s5="
literatureHref = "~/Bureau/bibliographie/literature/"

# fields that are required for a specific type of entry
if bibLaTeX:
    requiredFields = (("article", ("author", "title", "journaltitle", "date", "volume")),
                ("book",("author","publisher","title","date", "location")),
                ("report",("type","author","institution","title","date")),
                ("inproceedings",("author","booktitle","pages","publisher","title","date")),
                ("incollection",("author","booktitle","pages","publisher","title","date", "editor")),
                ("inbook",("author","booktitle","pages","publisher","title","date")),
                ("proceedings",("editor","publisher","title","date")),
                ("thesis",("type","author","institution","title","date")),
                ("electronic",("author","title","url","date")),
                ("misc",("author","howpublished","title","date")),
                )
else:
    requiredFields = (("article", ("author", "title", "journal", "year", "volume")),
                ("book",("author","publisher","title","year","address")),
                ("techreport",("author","institution","title","year")),
                ("inproceedings",("author","booktitle","pages","publisher","title","year")),
                ("incollection",("author","booktitle","pages","publisher","title","year", "editor")),
                ("inbook",("author","booktitle","pages","publisher","title","year")),
                ("proceedings",("editor","publisher","title","year")),
                ("phdthesis",("author","school","title","year")),
                ("mastersthesis",("author","school","title","year")),
                ("electronic",("author","title","url","year")),
                ("misc",("author","howpublished","title","year")),
                )

####################################################################

import string
import re

usedIds = set()

try:
    fInAux = open(auxFile, 'r', encoding="utf8")
    for line in fInAux:
        if line.startswith("\\citation"):
            ids = line.split("{")[1].rstrip("} \n").split(",")
            for id in ids:
                if (id != ""):
                    usedIds.add(id)
    fInAux.close()
except IOError as e:
    print("no aux file '"+auxFile+"' exists -> do not restrict entities")

fIn = open(bibFile, 'r', encoding="utf8")
completeEntry = ""
currentId = ""
ids = []
currentType = ""
currentArticleId = ""
currentTitle = ""
fields = []
bibTags = []
bibTag = []
problems = []

counterEntry = 0
counterMissingFields = 0
counterFlawedNames = 0
counterWrongTypes = 0
counterNonUniqueId = 0

removePunctuationMap = dict((ord(char), None) for char in string.punctuation)

for line in fIn:
    line = line.strip("\n")
    if line.startswith("@"):
        counterEntry += 1
        if (counterEntry > 1) and (currentId in usedIds or not usedIds) and (currentType.lower() != "string"):
            for requiredFieldsType in requiredFields:
                if requiredFieldsType[0] == currentType:
                    for field in requiredFieldsType[1]:
                        if field not in fields:
                            problems.append("missing field '"+field+"'")
                            counterMissingFields += 1
            bibTag = "\n\n<div id='"+currentId+"' class='bibTag severe"+str(len(problems))+"'>"
            bibTag += "\n<h2>"+currentId+" ("+currentType+")</h2> "
            bibTag += "\n<div class='links'>"
            bibTag += "\n | <a href='"+libgenHref+currentTitle+"' target='_blank'>LibGen</a>"
            bibTag += "\n | <a href='"+libgenArtHref+currentTitle+"' target='_blank'>LibGenArt</a>"
            bibTag += "\n | <a href='"+scholarHref+currentTitle+"' target='_blank'>Scholar</a>"
            bibTag += "\n | <a href='"+googleHref+currentTitle+"' target='_blank'>Google</a>"
            bibTag += "\n | <a href='"+mathscinetHref+currentTitle+"' target='_blank'>MathSciNet</a>"
            bibTag += "\n</div>"
            #bibTag += "\n<div class='reference'>"+cucurrentTitle
            bibTag += "\n<div class='reference'><a href='"literatureHref+currentId+currentTitle
            bibTag += "\n</div>"
            bibTag += "\n<ul class='enumprob'>"
            for problem in problems:
                bibTag += "\n<li>"+problem+"</li>"
            bibTag += "\n</ul>"
            bibTag += "\n<form class='bibTag_control'><label>checked</label><input type='checkbox' class='checked'/></form>"
            bibTag += "\n<div class='bibtex_toggle'>Current BibTeX Entry</div>"
            bibTag += "\n<div class='bibtex'>"+completeEntry +"</div>"
            bibTag += "\n</div>"
            bibTags.append(bibTag)
            bibTag = []

        fields = []
        problems = []
        currentId = line.split("{")[1].rstrip(",\n")
        if currentId in ids:
            problems.append("non-unique id: '"+currentId+"'")
            counterNonUniqueId += 1
        else:
            ids.append(currentId)
        currentType = line.split("{")[0].strip("@ ")
        completeEntry = line + "<br />"
    else:
        if line != "":
            completeEntry += line + "<br />"
        if currentId in usedIds or not usedIds:
            if "=" in line:
                field = line.split("=")[0].strip()
                fields.append(field)
                value = line.split("=")[1].strip("{} ,\n")
                if field == "author":
                    currentAuthor = filter(lambda x: not (x in "\\\"{}"), value.split(" and ")[0])
                if field == "title":
                    currentTitle = re.sub(r'\}|\{',r'',value)

                ####################################################################
                # Checks (please (de)activate/extend to your needs)
                ####################################################################


                # check if type 'proceedings' might be 'inproceedings'
                if currentType == "proceedings" and field == "pages":
                    problems.append("wrong type: maybe should be 'inproceedings' because entry has page numbers")
                    counterWrongTypes += 1

                # check if abbreviations are used in journal titles
                if currentType == "article" and (field == "journal" or field == "journaltitle"):
                    if "." in line:
                        problems.append("flawed name: abbreviated journal title '"+value+"'")
                        counterFlawedNames += 1

                # check booktitle format; expected format "ICBAB '13: Proceeding of the 13th International Conference on Bla and Blubb"
                #if currentType == "inproceedings" and field == "booktitle":
                    #if ":" not in line or ("Proceedings" not in line and "Companion" not in line) or "." in line or " '" not in line or "workshop" in line or "conference" in line or "symposium" in line:
                        #problems.append("flawed name: inconsistent formatting of booktitle '"+value+"'")
                        #counterFlawedNames += 1

                 # check if title is capitalized (heuristic)
                 #if field == "title":
                    #for word in currentTitle.split(" "):
                        #word = word.strip(":")
                        #if len(word) > 7 and word[0].islower() and not  "-" in word and not "_"  in word and not "[" in word:
                            #problems.append("flawed name: non-capitalized title '"+currentTitle+"'")
                            #counterFlawedNames += 1
                            #break

                ####################################################################

fIn.close()

if (currentId in usedIds or not usedIds) and (currentType.lower() != "string"):
    for requiredFieldsType in requiredFields:
        if requiredFieldsType[0] == currentType:
            for field in requiredFieldsType[1]:
                if field not in fields:
                    problems.append("missing field '"+field+"'")
                    counterMissingFields += 1
    bibTag = "\n\n<div id='"+currentId+"' class='bibTag severe"+str(len(problems))+"'>"
    bibTag = "\n\n<div id='"+currentId+"' class='bibTag severe"+str(len(problems))+"'>"
    bibTag += "\n<h2>"+currentId+" ("+currentType+")</h2> "
    bibTag += "\n<div class='links'>"
    bibTag += "\n | <a href='"+libgenHref+currentTitle+"' target='_blank'>LibGen</a>"
    bibTag += "\n | <a href='"+libgenArtHref+currentTitle+"' target='_blank'>LibGenArt</a>"
    bibTag += "\n | <a href='"+scholarHref+currentTitle+"' target='_blank'>Scholar</a>"
    bibTag += "\n | <a href='"+googleHref+currentTitle+"' target='_blank'>Google</a>"
    bibTag += "\n | <a href='"+mathscinetHref+currentTitle+"' target='_blank'>MathSciNet</a>"
    bibTag += "\n</div>"
    bibTag += "\n<div class='reference'>"+currentTitle
    bibTag += "\n</div>"
    bibTag += "\n<ul class='enumprob'>"
    for problem in problems:
        bibTag += "\n<li>"+problem+"</li>"
    bibTag += "\n</ul>"
    bibTag += "\n<form class='bibTag_control'><label>checked</label><input type='checkbox' class='checked'/></form>"
    bibTag += "\n<div class='bibtex_toggle'>Current BibTeX Entry</div>"
    bibTag += "\n<div class='bibtex'>"+completeEntry +"</div>"
    bibTag += "\n</div>"
    bibTags.append(bibTag)

html = open(htmlOutput, 'w')
html.write("""<html>
<head>
<title>BibTeX Check</title>
<style>
body {
    font-family: Calibri, Arial, Sans;
    padding: 10px;
    width: 1030px;
    margin: 10 auto;
    border-top: 1px solid black;
}

#title {
    width: 720px;

    border-bottom: 1px solid black;
}

#title h1 {
    margin: 10px 0px;
}

#title h1 a {
    color: black;
    text-decoration: none;
}

#control {
    clear: both;
}

#search {
    float: left;
}

#search input {
    width: 300px;
    font-size: 14pt;
}

#mode {
    text-align: right;
}

#mode label:first-child {
    font-weight: bold;
}

#mode input {
    margin-left: 20px;
}

.info {
    margin-top: 10px;
    padding: 10px;
    background: #FAFADD;
    width: 250px;
    float: right;
    box-shadow: 1px 1px 1px 1px #ccc;
    clear: both;
}

.info h2 {
    font-size: 12pt;
    padding: 0px;
    margin: 0px;
}

.bibTag {
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 10px;
    background: #FFBBAA;
    counter-increment: bibTag;
    width: 700px;
    border: 1px solid #993333;
    border-left: 5px solid #993333;
    box-shadow: 1px 1px 1px 1px #ccc;
    float: left;
}

.active {
    box-shadow: 5px 5px 3px 3px #ccc;
    position: relative;
    top: -2px;
}

.severe0 {
    background: #FAFAFA;
    border: 1px solid black;
    border-left: 5px solid black;
}

.severe1 {
    background: #FFEEDD;
}

.severe2 {
    background: #FFDDCC;
}

.severe3 {
    background: #FFCCBB;
}

.bibTag_checked {
    border: 1px solid #339933;
    border-left: 5px solid #339933;
}

.bibTag h2:before {
    content: counter(bibTag) ". "; color: gray;
}

.bibTag h2 {
    font-size: 11pt;
    font-weight: normal;
    font-family: monaco, monospace;
    padding: 0px;
    margin: 0px;
}

.bibTag .links {
    float: right;
    position:relative;
    top: -22px;
}

.bibTag .links a {
    color: #3333CC;
}

.bibTag .links a:visited {
    color: #666666;
}

.bibTag .reference {
    clear: both;
    margin-left: 20px;
    font-size: 11pt;
    font-weight:normal;
}

.bibTag ul {
    clear: both;
}

.enumprob {
    font-weight: light;
    font-size: 10pt;
}

.bibTag .bibTag_control {
    float: right;
    margin: 0px;
    padding: 0px;
}

.bibTag .bibtex_toggle{
    text-decoration: underline;
    font-size: 9pt;
    cursor: pointer;
    padding-top: 5px;
}

.bibTag .bibtex {
    margin-top: 5px;
    font-family: Monospace;
    font-size: 8pt;
    display: none;
    border: 1px solid black;
    background-color: #FFFFFF;
    padding: 5px;
}
</style>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
<script>

function isInProblemMode() {
    return $('#mode_problems:checked').val() == 'problems'
}

function update() {
    $('.bibTag').hide();
    $('.bibTag[id*='+$('#search input').val()+']').show();
    $('.bibTag .checked').each(function () {
        if ($(this).attr('checked')) {
            $(this).parents('.bibTag').addClass('bibTag_checked');
        } else {
            $(this).parents('.bibTag').removeClass('bibTag_checked');
        }
    });
    if (isInProblemMode()) {
        $('.severe0').hide();
        $('.bibTag_checked').hide();
    }
}

$(document).ready(function(){

    $(".bibtex_toggle").click(function(event){
        event.preventDefault();
        $(this).next().slideToggle();
    });

    $('#search input').live('input', function() {
        update();
    });

    $('#mode input').change(function() {
        update();
    });

    $("#uncheck_button").click(function(){
        $('.bibTag .checked').attr('checked',false);
        localStorage.clear();
        update();
    });

    $('.bibTag a').mousedown(function(event) {
        $('.bibTag').removeClass('active');
        $(this).parents('.bibTag').addClass('active');
    });

    $('.bibTag .checked').change(function(event) {
        var bibTag = $(this).parents('.bibTag');
        bibTag.toggleClass('bibTag_checked');
        var checked = bibTag.hasClass('bibTag_checked');
        localStorage.setItem(bibTag.attr('id'),checked);
        if (checked && isInProblemMode()) {
            bibTag.slideUp();
        }
    });

    $('.bibTag .checked').each(function () {
        $(this).attr('checked',localStorage.getItem($(this).parents('.bibTag').attr('id'))=='true');
    });
    update();
});

</script>
</head>
<body>
<div id="title">
<h1><a href='https://github.com/zaikunzhang/textools'>BibTeX Check</a></h1>
<div id="control">
<form id="search"><input placeholder="search entry ID ..."/></form>
<form id="mode">
<label>show entries:</label>
<input type = "radio"
                 name = "mode"
                 id = "mode_problems"
                 value = "problems"
                 checked = "checked" />
          <label for = "mode_problems">problems</label>
          <input type = "radio"
                 name = "mode"
                 id = "mode_all"
                 value = "all" />
          <label for = "mode_all">all</label>
<input type="button" value="uncheck all" id="uncheck_button"></button>
</form>
</div>
</div>
""")
html.write("<div class='info'><h2>Info</h2><ul>")
html.write("<li>bib file: "+bibFile+"</li>")
html.write("<li>aux file: "+auxFile+"</li>")
html.write("<li># entries: "+str(len(bibTags))+"</li>")
html.write("<li># bibTags: "+str(counterMissingFields+counterFlawedNames+counterWrongTypes+counterNonUniqueId)+"</li><ul>")
html.write("<li># missing fields: "+str(counterMissingFields)+"</li>")
html.write("<li># flawed names: "+str(counterFlawedNames)+"</li>")
html.write("<li># wrong types: "+str(counterWrongTypes)+"</li>")
html.write("<li># non-unique id: "+str(counterNonUniqueId)+"</li>")
html.write("</ul></ul></div>")

#bibTags.sort()
for bibTag in bibTags:
    print('Linje: ' + bibTag + '\n')
    html.write(bibTag)
html.write("</body></html>")
html.close()
