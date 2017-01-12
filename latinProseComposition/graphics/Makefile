OBJECTS := $(addprefix thumb-, $(wildcard lesson_*.jpeg))
	
all:       main

main:      $(OBJECTS)

thumb-%.jpeg : %.jpeg
	convert $< -resize 1200x1200 $@

. PHONY : clean

clean : 
	rm -f $(OBJECTS)



