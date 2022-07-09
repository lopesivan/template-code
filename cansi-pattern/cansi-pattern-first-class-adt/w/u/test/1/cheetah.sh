#!/usr/bin/env bash

test -n "$DEBUG" && set -x

##############################################################################
##############################################################################
##############################################################################

# ----------------------------------------------------------------------------
# Run!

ls|
  grep -vE '(cmake-*|main.c|Makefile|CMakeLists.txt|*.yml|*.sh)'|
    xargs ls

ADT=/developer/cansi-pattern/cansi-pattern-first-class-adt
APP=${ADT}/w/v/app.py
YML=adt.yml

python ${APP} -s -y ${YML}|sort

gcc -M *.c *.h                       | \
  sed -e 's/[\\ ]/\n/g'              | \
  sed -e '/^$/d' -e '/\.o:[ \t]*$/d' | \
  ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q

find . -maxdepth 1 -name \*.c -o -name \*.h |
xargs astyle \
 --pad-first-paren-out \
 --style=linux \
 -A1 \
 --indent=spaces=4 \
 --convert-tabs

rm *.orig

# ----------------------------------------------------------------------------
exit 0
