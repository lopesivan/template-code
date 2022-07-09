YAML =  1.yml
dir  = ./out

all: view

rebuild: build clean save
build:
	# Build templates
	@(cd ../c; make clean; make)
save:
	python app.py -s -y $(YAML)
view:
	python app.py -p -y $(YAML)

clean:
	rm -rf ${dir}
#	ls | grep -vE '(Makefile|app.py|*.yml)' | xargs rm

# END OF FILE
