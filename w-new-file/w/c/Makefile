LANGUAGE       = new_file
DESIGN_PATTERN = commmand
YAML           = commmand.yml

model = ../m
view  = ../v
SRCS  = $(shell find $(model) -name \*.tmpl -printf '%f\n' )

templates = $(foreach s,$(SRCS), $(addprefix $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)/,$(s:.tmpl=.py)))
TARGETS   = $(templates)

all: $(TARGETS)

# tmpl -> py
$(view)/$(LANGUAGE)/$(DESIGN_PATTERN)/%.py:  $(model)/%.tmpl
	cheetah-compile --flat $^ --odir $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)

view:
	python app.py $(view)/$(YAML)

clean:
	find $(view) -name "*.pyc" -delete
	find $(view) -name "*.py.bak" -delete
	find $(model) -type l -a -name "*.tmpl" -delete
	rm -rf $(view)/$(LANGUAGE)/$(DESIGN_PATTERN)
	rm -rf $(view)/$(LANGUAGE)

build:
	(cd ../m; ./mk-code.sh)
	(make)
	(cd ../v; ./mk-models.sh)

# END OF FILE
