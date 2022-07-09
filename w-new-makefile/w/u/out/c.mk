sources :=

CC = gcc
LD = $(CC)

#INCFLAGS = `pkg-config --cflags gtk+-3.0`
#LIBS     = `pkg-config --libs gtk+-3.0`
CFLAGS   = -Wall -c
LDFLAGS  = -o
#GDBFLAGS = -g

target  := main
targets := tags $(target)

# Compile
.c.o:
	$(CC) $(GDBFLAGS) $(INCFLAGS) $(CFLAGS) $<

all: $(targets)
main: $(sources:.c=.o)
	$(CC) $(LDFLAGS) $@ $(notdir $^) $(LIBS)

tags:
	$(CC) -M $(INCFLAGS) $(sources) |\
	sed -e 's/[\\ ]/\n/g' |\
	sed -e '/^$$/d' -e '/\.o:[ \t]*$$/d' |\
	ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q
	cscope -bRq

clean:
	/bin/rm -rf $(target) $(notdir $(sources:.c=.o))
# END OF FILE
