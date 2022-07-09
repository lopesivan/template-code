YAML =  1.yml

all: save


save:
	python app.py -s -y $(YAML)
view:
	python app.py -p -y $(YAML)

clean:
	ls | grep -vE '(Makefile|app.py|*.yml)' | xargs rm

install:
	cp ./hosts /etc/
	cp ./interfaces /etc/network/
#	cp ./enp2s0f1 /etc/network/
	cp ./wlp3s0 /etc/network/
	systemctl  restart networking.service

# END OF FILE
