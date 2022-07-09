pkgname = msgpack-cli
_name=${pkgname}

git:
	git clone https://github.com/jakm/msgpack-cli

prepare: $(pkgname)
	mkdir -p "src/mvdan.cc"
	mv ${_name} src/mvdan.cc/${_name}


build: export srcdir := $(shell pwd)
build:
	cd ${srcdir}/src/mvdan.cc/${_name} && go build -ldflags='-w -s'

package: export srcdir := $(shell pwd)
package: export pkgdir := /tmp/kk
package:
	cd ${srcdir}/src/mvdan.cc/${_name}; install -Dm755 ${_name} `goenv root`/versions/`goenv  version| awk '{print $$1}'`/bin/;
