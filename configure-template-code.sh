#!/usr/bin/env bash


function make_clean() {
    local path=$1
    local control=${path}/w/c
    cd "${control}" && make clean
}

function make_() {
    local path=$1
    local control=${path}/w/c
    cd "${control}" && make
}

function mk_code() {
    local path=$1
    local model=${path}/w/m
    cd "${model}" && ./mk-code.sh
}

function mk_models() {
    local path=$1
    local view=${path}/w/v
    cd "${view}" && {
        test -d models && rm -rf models;
        ./mk-models.sh;
    }

}
##############################################################################

function mvc_model() {
    local w=$1
    mk_code $w
}

function mvc_controller() {
    local w=$1
    make_clean $w
    make_ $w
}

function mvc_view() {
    local w=$1
    mk_models $w
}


function mvc() {
    local d=$1
    mvc_model $d
    mvc_controller $d
    mvc_view $d
}

export PYTHONIOENCODING=utf-8
export PYENV_VERSION=neovim3
#source ${HOME}/developer/qutebrowser/.venv/bin/activate
# DO STUFF
d=$(brew --prefix)/opt/template-code
mvc ${d}/w-new-file

# Reset version
unset PYENV_VERSION

