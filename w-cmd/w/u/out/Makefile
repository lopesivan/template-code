VERSION   = 0.1
NAME      = ttjava

include etc/rules/build.mk
include etc/rules/tests.mk
include etc/rules/run.mk

install: install-$(PROJECT)

clean:
	@-rm -rf $(prefix)/bin/$(PROJECT)
	chmod -x exec
	echo bash-it disable completion ttjava
	rm /home/ivan/developer/bash-it/completion/available/ttjava.completion.bash

test-task-list:
	@(ls tests/tasks/| sed -r 's/(^.+)_test.sh/make \1-task-test/')

test-task:
	ls tests/tasks/| sed -r 's/(^.+)_test.sh/make \1-task-test/'|sh
test:
	bang test

test-clean:
	@-rm tests/*.out

