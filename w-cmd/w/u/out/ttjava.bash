#!/usr/bin/env bash

# ----------------------------------------------------------------------------
# Run!

TTJAVA=$(command -v ttjava)
[[ $TTJAVA ]] && eval "$( ttjava init )"
