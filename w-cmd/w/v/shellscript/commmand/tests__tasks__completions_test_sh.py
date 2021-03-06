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
__CHEETAH_genTime__ = 1576846546.211697
__CHEETAH_genTimestamp__ = 'Fri Dec 20 09:55:46 2019'
__CHEETAH_src__ = '../m/tests__tasks__completions_test_sh.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Mar 20 17:34:23 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class tests__tasks__completions_test_sh(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(tests__tasks__completions_test_sh, self).__init__(*args, **KWs)
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
        
        write('''b.module.require unittest

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 4, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 4, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 4, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 4, col 21.
        write(''' completions
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 5, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 5, col 17.
        write('''_completions () {

  local cmd="$(
    echo \'--help --version --usage\' \\
          \'-a --add\'                \\
          \'-l --list\'               \\
          \'-n --name\' |

    sed \'s/ /\\n/g\' )"

  b.unittest.assert_equal \\
    "${cmd}" "$(''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 16, col 19
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 16, col 19.
        write(''' completions)"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 20, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 20, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 20, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 20, col 21.
        write(''' completions --help
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 21, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 21, col 17.
        write('''_long_option_help () {
  local jsonfile="$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 22, col 54
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 22, col 54.
        write(''')))/etc/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 22, col 73
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 22, col 73.
        write('''doc.json"

  test -n "$jsonfile"           # se a variavel nao e nula
  b.unittest.assert_success $?  # entao sucesso

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 27, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 27, col 14.
        write(''' completions --help"

  local description=$(cat $jsonfile |
    jq --raw-output \'.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 30, col 23
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 30, col 23.
        write('''[] | select(.command == "completions") | .description\'
  )

  b.unittest.assert_equal \\
    "$description" "$(${cmd})"
}

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

    _mainCheetahMethod_for_tests__tasks__completions_test_sh = 'respond'

## END CLASS DEFINITION

if not hasattr(tests__tasks__completions_test_sh, '_initCheetahAttributes'):
    templateAPIClass = getattr(tests__tasks__completions_test_sh,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(tests__tasks__completions_test_sh)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=tests__tasks__completions_test_sh()).run()


