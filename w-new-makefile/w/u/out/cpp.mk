sources :=

CC = g++
LD = $(CC)

INCFLAGS =
CFLAGS   = -c $(INCFLAGS)
LDFLAGS  = -o
GDBFLAGS = -g

target  := main
targets := tags $(target)

# Compile
.cpp.o:
	$(CC) $(CFLAGS) $<

all: $(targets)
main: $(sources:.cpp=.o)
	$(CC) $(LDFLAGS) $@ $(notdir $^)

tags:
	$(CC) -M $(INCFLAGS) $(sources) |\
	sed -e 's/[\\ ]/\n/g' |\
	sed -e '/^$$/d' -e '/\.o:[ \t]*$$/d' |\
	ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q
	cscope -bRq

clean:
	/bin/rm -rf $(target) $(notdir $(sources:.cpp=.o))
# END OF FILE
