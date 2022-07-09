#
# Makefile
#
#
APP = ../../app.py
YML = test.yml

SRCS    = $(wildcard *.c)
OBJECTS = $(foreach s,$(SRCS), $(s:.c=.o))
HEADERS = $(wildcard *.h)

all: gen

main: $(OBJECTS)
	$(CC) -o $@ $^
run: main
	./main

reset:
	@(ls | grep -vE '(Makefile|*.yml)'| xargs rm)
#	@make gen
clean:
	/bin/rm $(OBJECTS)

$(OBJECTS): ${HEADERS}

tags: $(SRCS) $(HEADERS)
	$(CC) -M $<                        | \
	sed -e 's/[\\ ]/\n/g'              | \
	sed -e '/^$/d' -e '/\.o:[ \t]*$/d' | \
	ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q

valgrind:
	valgrind ./main
gen:
	python $(APP) -s -y $(YML)|sort
pyenv:
	pyenv local neovim2
