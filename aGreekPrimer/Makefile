
OBJECTS := $(patsubst %.tex,%.pdf,$(wildcard aGreekPrimer*.tex))
	
all:       main

main:      $(OBJECTS)

%.pdf : %.tex
	@echo  "costruisco:" $<
	xelatex -quiet $<
	bibtex $(basename $<)
	xelatex -quiet $<
	xelatex -quiet $<

. PHONY : distclean clean

distclean : clean
	rm -f $(OBJECTS)

clean :
	rm -f *.aux *.log *.out *.bbl *.blg


