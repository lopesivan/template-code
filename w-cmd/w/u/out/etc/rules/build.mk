PROJECT   = $(NAME)
prefix   ?= /usr/local

install-$(PROJECT):
	-mkdir -p $(prefix)/bin
	ln -s `pwd`/exec $(prefix)/bin/$(PROJECT)
	chmod +x exec
	cp `pwd`/ttjava.bash /home/ivan/developer/bash-it/completion/available/ttjava.completion.bash
	echo bash-it enable completion ttjava

