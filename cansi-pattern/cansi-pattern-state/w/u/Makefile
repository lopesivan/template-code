YAML =  2.yml

all: build

rebuild: distclean build
build:
	make -C ../c
distclean:
	make -C ../c clean

view: build
	python app.py -p -y $(YAML)

clean:
	ls | grep -vE '(Makefile|app.py|*.yml)' | xargs rm

# END OF FILE
