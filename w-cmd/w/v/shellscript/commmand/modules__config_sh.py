#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.compat import unicode

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.5a0'
__CHEETAH_versionTuple__ = (3, 2, 5, 'alpha', 0)
__CHEETAH_genTime__ = 1576846544.8802438
__CHEETAH_genTimestamp__ = 'Fri Dec 20 09:55:44 2019'
__CHEETAH_src__ = '../m/modules__config_sh.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Mar 20 17:34:23 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class modules__config_sh(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(modules__config_sh, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''# modules/config.sh

function ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 3, col 10
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 3, col 10.
        write(""".config.load () {

    b.unset '""")
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 5, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 5, col 14.
        write(""".config'

    _""")
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 7, col 6
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 7, col 6.
        write('''.config.load_default_config

    return $?
}

function _''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 12, col 11
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 12, col 11.
        write('''.config.load_from_file () {

    local file="$1"

    local number_of_tasks=$(cat $file | jq \'.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 16, col 48
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 16, col 48.
        write('''[] .start\' | wc -l)
    let number_of_tasks--
    for i in `seq 0 $number_of_tasks`; do

        local command=$(cat $file |
            jq --raw-output ".''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 21, col 31
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 21, col 31.
        write('''[$i].command")

        local description=$(cat $file |
            jq --raw-output ".''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 24, col 31
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 24, col 31.
        write('''[$i].description")

        b.set "''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 26, col 16
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 26, col 16.
        write('''.config.help_message_$command" "$description"
    done

    local name=$(cat $file | jq --raw-output ".id.name")

    local version=$(cat $file | jq --raw-output ".id.version")

    b.set "''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 33, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 33, col 12.
        write('''.config.name" "$name"
    b.set "''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 34, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 34, col 12.
        write('''.config.version" "$version"
    b.set "''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 35, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 35, col 12.
        write('''.config.author" "`git config --get user.name`"
    b.set "''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 36, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 36, col 12.
        write('''.config.email"  "`git config --get user.email`"

}

function _''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 40, col 11
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 40, col 11.
        write('''.config.load_default_config () {

    b.set "''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 42, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 42, col 12.
        write('''.config.help_message" \'2\'

    local file="$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 44, col 52
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 44, col 52.
        write(''')))/etc/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 44, col 71
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 44, col 71.
        write('''doc.json"

    if [ -n "$file" ]; then                   # se variavel nao nula
        if [ -e "$file" ]; then               # se arquivo existe
            _''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 48, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 48, col 14.
        write('''.config.load_from_file "$file" # carrega arquivo

            return $?
        else
            b.raise FileNotFoundException     # se arquivo nao encontrado
        fi
    else
        b.raise StringIsNullException         # se a variavel e nula
    fi

    return 1
}

# vim: set ts=4 sw=4 tw=78 ft=sh:
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_modules__config_sh = 'respond'

## END CLASS DEFINITION

if not hasattr(modules__config_sh, '_initCheetahAttributes'):
    templateAPIClass = getattr(modules__config_sh,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(modules__config_sh)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=modules__config_sh()).run()


