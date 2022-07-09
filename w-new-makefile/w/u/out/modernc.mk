CC       = gcc
LD       = ${CC}

INCFLAGS = -I.
GDBFLAGS = -g
CFLAGS   = -std=gnu99 -Wall -Wno-parentheses ${INCFLAGS} ${GDBFLAGS}
LDFLAGS  = -o
LIBS     = -lm

SRCS    = $(wildcard *.c)
OBJECTS = $(foreach s,$(SRCS), $(s:.c=.o))
HEADERS = $(wildcard *.h)

TARGETS = main

all: ${TARGETS}

main: $(OBJECTS)
	$(LD) ${LDFLAGS} $@ $^ ${LIBS}
run: main
	./main
clean:
	/bin/rm ${TARGETS} $(OBJECTS) tags

$(OBJECTS): ${HEADERS}

tags: $(SRCS) $(HEADERS)
	$(CC) -M $^                          | \
	sed -e 's/[\\ ]/\n/g'                | \
	sed -e '/^$$/d' -e '/\.o:[ \t]*$$/d' | \
	ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q
valgrind:
	valgrind ./main
