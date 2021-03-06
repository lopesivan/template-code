CC          = gcc
LD          = $(CC)
INCLUDE    := ../../src

TARGETS     := \
	module.so \
	module2.so \
	module3.so

all: $(TARGETS)

module.so: module.c
	$(CC) -I$(INCLUDE) -shared -fPIC -o $@ $^
module2.so: module2.c
	$(CC) -I$(INCLUDE) -shared -fPIC -o $@ $^
module3.so: module3.c
	$(CC) -I$(INCLUDE) -shared -fPIC -o $@ $^

clean:
	/bin/rm -f $(TARGETS)

install: $(TARGETS)
	install -m 755 module.so ~/.config/scim/module
	install -m 755 module2.so ~/.config/scim/module
	install -m 755 module3.so ~/.config/scim/module

uninstall:
	rm ~/.config/scim/module/module.so
	rm ~/.config/scim/module/module2.so
	rm ~/.config/scim/module/module3.so
