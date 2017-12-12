SHELL = bash

STYLEPROG = style61b

JFLAGS = -g -Xlint:unchecked -encoding utf8

SRCS = $(wildcard *.java)

CLASSES = $(SRCS:.java=.class)

# Tell make that these are not really files.
.PHONY: clean default style check

default: compile

compile: $(CLASSES)

style:
	$(STYLEPROG) $(SRCS)

check: $(CLASSES)
	java -ea MSTTest

$(CLASSES): sentinel

sentinel: $(SRCS)
	javac $(JFLAGS) $(SRCS)
	touch $@

# Find and remove all *~ and *.class files.
clean:
	$(RM) sentinel *.class *~

