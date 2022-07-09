YAML =  2.yml
UPP  = ../..

all: status

rebuild: distclean build
build:
	make -C ${UPP}/c
distclean:
	make -C ${UPP}/c clean

status: build
	python ${UPP}/v/app.py -y $(YAML)
view: build
	python ${UPP}/v/app.py -p -y $(YAML)
save: build
	python ${UPP}/v/app.py -s -y $(YAML)
clean:
	ls | grep -vE '(Makefile|app.py|*.yml|test)' | xargs rm -rf

# END OF FILE

