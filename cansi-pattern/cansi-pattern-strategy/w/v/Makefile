d              =\
$$PWD

ctags_init     =\
	ctags -R --python-kinds --fields=+iaS --extra=+q \
	`find $d -name '*.py'`

all: tags

tags        : ctags
ctags       :
	#Update file tags
	$(shell $(ctags_init) )

clean:
	@/bin/rm -rf tags *~
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.py.bak" -delete
