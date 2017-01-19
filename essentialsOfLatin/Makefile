
OBJECTS := $(patsubst %.tex,%.pdf,$(wildcard essentialsOfLatin*.tex))
BIBLIOFILE := latinBiblio.bib
	
all:       main

main:      $(OBJECTS)

%.pdf : %.tex $(BIBLIOFILE)
	@echo  "costruisco:" $@
	rm -f $@
	xelatex -quiet $<
	bibtex $(basename $<)
	xelatex -quiet $<
	xelatex -quiet $<

. PHONY : distclean clean

distclean : clean
	rm -f $(OBJECTS)

clean :
	rm -f *.aux *.log *.out *.bbl *.blg


