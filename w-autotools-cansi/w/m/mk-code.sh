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
#        File: arruma.sh
#        Date: Ter 12 Jun 2018 17:22:25 -03
# Description:
# ----------------------------------------------------------------------------
# Modo strict
set -euo pipefail
# ----------------------------------------------------------------------------
rm *.tmpl
##############################################################################
##############################################################################
##############################################################################
find ${HOME}/work/gg \
    -type f -not -path '*/\.git/*' \
    -printf "%P\n" |
    sed -e 'h' \
        -e 's=^=cp ${HOME}//work/gg/=' \
        -e 'p;g'  \
        -e 's/^\./dot_/g' \
        -e 's/\./_/g' \
        -e 's/-/___/g' \
        -e 's=/=__=g' \
        -e 's=exec=localexecutable=g' \
        -e 's/$/.tmpl/' |
            paste - -  |
                sh
# ----------------------------------------------------------------------------
# Run!


chmod -x *.tmpl
#sed 's=\\$=\\\\=g' -i *.tmpl
sed 's/#/\\&/g' -i *.tmpl
sed 's/\$/\\&/g' -i *.tmpl
sed "1i#encoding UTF-8\n#compiler commentStartToken = '//'\n// comment\n#compiler reset" -i *.tmpl
dos2unix *.tmpl
# ----------------------------------------------------------------------------
exit 0
