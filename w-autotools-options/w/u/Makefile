YAML =  1.yml
dir  = ./out

all: view

save:
	python app.py -s -y $(YAML) helloworld cpp
view:
	python app.py -y $(YAML) helloworld cpp

clean:
	rm -rf ${dir}

# END OF FILE
