python plots.py

pdflatex -halt-on-error report.tex
bibtex report
pdflatex -halt-on-error report.tex
pdflatex -halt-on-error report.tex
