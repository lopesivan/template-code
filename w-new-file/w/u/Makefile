YAML =  1.yml
dir  = ./out

all: view

save:
	python app.py -s -y $(YAML)
view:
	python app.py -p -y $(YAML) helloworld cpp

clean:
	rm -rf ${dir}
#	ls | grep -vE '(Makefile|app.py|*.yml)' | xargs rm

# END OF FILE
