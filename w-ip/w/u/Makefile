YAML =  1.yml

all: view


view:
	python app.py -p -y $(YAML)

clean:
	ls | grep -vE '(test|Makefile|app.py|*.yml)' | xargs rm

# END OF FILE
