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
# for f in *.tmpl; do
#     test -e $f && rm $f
# done
##############################################################################
##############################################################################
##############################################################################
d=../data
find $d \
    -type f -not -path '*/\.git/*' \
    -printf "%P\n" |
      sed \
      -e'h;g' \
      -e 's@/@__@g' \
      -e 's@\.@dot_@' \
      -e 's@-@UNDERscore_@' \
      -e 's/$/.tmpl/' \
      -e 'x; s/^/cp ..\/data\//; G ; s/\n/ /'|
      sh
# ----------------------------------------------------------------------------
# Run!
chmod -x *.tmpl
sed 's/^\([ ]\+\)\(#\)/\1\\\2/g' -i *.tmpl
sed 's/^#/\\#/g' -i *.tmpl
sed 's/\$/\\&/g' -i *.tmpl
sed.acentos -i *.tmpl
# sed 's/template/${cmd.name}/g' -i *.tmpl
# ----------------------------------------------------------------------------
exit 0
