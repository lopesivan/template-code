#!/usr/bin/env bash

test -n "$DEBUG" && set -x

#                      __ __       ___
#                     /\ \\ \    /'___`\
#                     \ \ \\ \  /\_\ /\ \
#                      \ \ \\ \_\/_/// /__
#                       \ \__ ,__\ // /_\ \
#                        \/_/\_\_//\______/
#                           \/_/  \/_____/
#                                         Algoritimos
#
#
#      Author: Ivan Lopes
#        Mail: ivan@42algoritmos.com.br
#        Site: http://www.42algoritmos.com.br
#     License: gpl
#       Phone: +1 561 801 7985
#    Language: Shell Script
#        File: mkView.sh
#        Date: Ter 26 Set 2017 12:54:29 BRT
# Description:
# ----------------------------------------------------------------------------
test -d models || mkdir models
##############################################################################
##############################################################################
##############################################################################

# 0 - stdin
# 1 - stdout
# 2 - stderr

exec 4>&1             # stdout duplicado ( FD 4 tem as mesmas caracteristicas
                      # do STDOUT), aponta para o terminal.

exec 1>app.py         # stdout aponta para `app.py'



# ----------------------------------------------------------------------------
# Run!
echo file: app.py >&4

cat <<EOF
# encoding: utf-8
"""Criação de arquivos."""

import sys
import os
import os.path
import yaml
import optparse

import models

parser = optparse.OptionParser(usage="%prog -[ [s] --[save] ]", version="%prog 1.0")

#
# -p, --stdout
#
parser.add_option( '-p', '--stdout',
        dest    = "stdout",
        default = False,
        action  = "store_true",
        help    = "Show file in stdout."
        )

#
# -s, --save
#
parser.add_option( '-s', '--save',
        dest    = "save",
        default = False,
        action  = "store_true",
        help    = "Active save mode."
        )

#
# -y, --yml
#
parser.add_option( '-y', '--yml',
        dest    = "yml",
        default = "1.yml",
        help    = "Define yml file"
        )

def main():
    options, remainder = parser.parse_args()

    """Método principal de criação de arquivos."""
    path = options.yml

    if os.path.isfile(path) and os.access(path, os.R_OK):
        # Load YAML file
        config_file = file(path, 'r')
        data_model = yaml.load(config_file)
        config_file.close()

EOF

L=$(look LANGUAGE ../c/Makefile | sed 's/.* =[ ]*//')
D=$(look DESIGN_PATTERN ../c/Makefile | sed 's/.* =[ ]*//')

find ../m/ -name \*.tmpl -exec basename {} .tmpl \; |
while read M; do
cat <<EOF
        t = models.T${M^}(data_model, '${L}.${D}.${M}')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

EOF
done

cat <<EOF
    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
EOF

exec 1>&4             # FD 1 recebe as caracteristicas de FD 4.
                      # FD 1 ressetado.

exec 4>&-             # FD 4 eh liberado.

##############################################################################
##############################################################################
##############################################################################

# 0 - stdin
# 1 - stdout
# 2 - stderr

exec 4>&1                 # stdout duplicado ( FD 4 tem as mesmas caracteristicas
                          # do STDOUT), aponta para o terminal.

exec 1>models/sh.py  # stdout aponta para `models/factory.py'

echo file: models/factory.py >&4

cat <<EOF
import errno
import os


class Sh(object):

    """Shell scripts mkdir -p dir"""

    def __init__(self, Dir):
        """TODO: to be defined1.

        :Dir: TODO

        """
        self._Dir = Dir

    def mkdir(self):
        if not os.path.exists(self._Dir):
            try:
                os.makedirs(self._Dir)
            except:
                raise OSError(
                    "Can't create destination directory (%s)!" % (self._Dir))

EOF

exec 1>&4             # FD 1 recebe as caracteristicas de FD 4.
                      # FD 1 ressetado.

exec 4>&-             # FD 4 eh liberado.

##############################################################################
##############################################################################
##############################################################################

# 0 - stdin
# 1 - stdout
# 2 - stderr

exec 4>&1                 # stdout duplicado ( FD 4 tem as mesmas caracteristicas
                          # do STDOUT), aponta para o terminal.

exec 1>models/factory.py  # stdout aponta para `models/factory.py'

echo file: models/factory.py >&4

cat <<EOF
# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

EOF

find ../m/ -name \*.tmpl -exec basename {} .tmpl \; |
while read M; do
cat <<EOF
from ${L}.${D}.${M} import ${M}
EOF
done

echo
echo
echo "template = {"

find ../m/ -name \*.tmpl -exec basename {} .tmpl \; |
while read M; do
cat <<EOF
    '${L}.${D}.${M}': ${M}(),
EOF
done
echo "}"

cat <<EOF

class Factory(object):
    """Metodo fabrica."""
    __metaclass__ = ABCMeta

    def __init__(self, template_name):
        self.tmpl = template[template_name]

    @abstractmethod
    def put(self):
        """Imprime mensagem na tela."""
        pass

    @abstractmethod
    def save(self):
        """Salva em arquivo."""
        pass

EOF

exec 1>&4             # FD 1 recebe as caracteristicas de FD 4.
                      # FD 1 ressetado.

exec 4>&-             # FD 4 eh liberado.

##############################################################################
##############################################################################
##############################################################################

# 0 - stdin
# 1 - stdout
# 2 - stderr

exec 4>&1                  # stdout duplicado ( FD 4 tem as mesmas caracteristicas
                           # do STDOUT), aponta para o terminal.

exec 1>models/__init__.py  # stdout aponta para `models/__init__.py'

echo file: models/__init__.py >&4

find ../m/ -name \*.tmpl -exec basename {} .tmpl \; |
while read M; do
cat <<EOF
from .t${M} import T${M^}
EOF
done

exec 1>&4             # FD 1 recebe as caracteristicas de FD 4.
                      # FD 1 ressetado.

exec 4>&-             # FD 4 eh liberado.

##############################################################################
##############################################################################
##############################################################################

# 0 - stdin
# 1 - stdout
# 2 - stderr

find ../m/ -name \*.tmpl -exec basename {} .tmpl \; |
while read M; do
# 0 - stdin
# 1 - stdout
# 2 - stderr

exec 4>&1               # stdout duplicado ( FD 4 tem as mesmas caracteristicas
                        # do STDOUT), aponta para o terminal.

exec 1>models/t${M}.py  # stdout aponta para `out.txt'

echo file: models/t${M}.py >&4
FILENAME=$(echo ${M} | sed -e 's=dot_=.=g' -e 's=___=-=g' -e 's=__=/=g' -e 's/_/./' -e 's=localexecutable=exec=g')
DIR=${FILENAME%/*}

cat <<EOF
"""Classe de template."""
from .factory import Factory
from .sh import Sh


class T${M^}(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.autotools = data_model['autotools']
        self.tmpl.name = "%s/%s" %(self.tmpl.autotools['dir'], "${FILENAME}")
        #self.tmpl.log = data_model['log']

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)
        print self.tmpl
EOF

if [ "$FILENAME" == "$DIR" ]; then
    cat <<EOF
    def save(self):
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
EOF
else
    cat <<EOF
    def save(self):
        DIR = "%s/%s" %(self.tmpl.autotools['dir'], "${DIR}")
        sh = Sh(DIR)
        sh.mkdir()
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
EOF
fi


exec 1>&4             # FD 1 recebe as caracteristicas de FD 4.
                      # FD 1 ressetado.

exec 4>&-             # FD 4 eh liberado.
done

# ----------------------------------------------------------------------------
exit 0
