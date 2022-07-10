all: install

configure:
	@bash -c ./configure-template-code.sh

reinstall:
	brew reinstall template-code
install:
	brew install template-code
clean:
	brew uninstall template-code
