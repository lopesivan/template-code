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
__CHEETAH_genTime__ = 1576846546.6110249
__CHEETAH_genTimestamp__ = 'Fri Dec 20 09:55:46 2019'
__CHEETAH_src__ = '../m/tests__tasks__default_test_sh.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Mar 20 17:34:23 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class tests__tasks__default_test_sh(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(tests__tasks__default_test_sh, self).__init__(*args, **KWs)
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
        write('''_default () {

  local output="Usage: ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 7, col 24
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 7, col 24.
        write(''' [tasks] [options]"

  b.unittest.assert_equal \\
    "${output}" "$(''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 10, col 22
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 10, col 22.
        write(''')"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 14, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 14, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 14, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 14, col 21.
        write(''' --help
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 15, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 15, col 17.
        write('''_long_option_help () {

  local f=$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 17, col 46
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 17, col 46.
        write(''')))/tests/outfiles/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 17, col 76
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 17, col 76.
        write('''__help.out

  local output="$(cat $f)"

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 21, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 21, col 14.
        write(''' --help"

  b.unittest.assert_equal \\
    "$output" "$(${cmd})"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 28, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 28, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 28, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 28, col 21.
        write(''' --debug
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 29, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 29, col 17.
        write('''_long_option_debug () {

  local f=$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 31, col 46
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 31, col 46.
        write(''')))/tests/outfiles/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 31, col 76
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 31, col 76.
        write('''__debug.out

  local output="$(cat $f)"

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 35, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 35, col 14.
        write(''' --debug"

  b.unittest.assert_equal \\
    "$output" "$(${cmd})"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 42, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 42, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 42, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 42, col 21.
        write(''' --debug --list
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 43, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 43, col 17.
        write('''_long_option_debug_list () {

  local f=$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 45, col 46
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 45, col 46.
        write(''')))/tests/outfiles/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 45, col 76
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 45, col 76.
        write('''__debug__list.out

  local output="$(cat $f)"

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 49, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 49, col 14.
        write(''' --debug --list"

  b.unittest.assert_equal \\
    "$output" "$(${cmd})"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 56, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 56, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 56, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 56, col 21.
        write(''' --debug --add
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 57, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 57, col 17.
        write('''_long_option_debug_add () {

  local f=$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 59, col 46
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 59, col 46.
        write(''')))/tests/outfiles/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 59, col 76
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 59, col 76.
        write('''__debug__add.out

  local output="$(cat $f)"

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 63, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 63, col 14.
        write(''' --debug --add"

  b.unittest.assert_equal \\
    "$output" "$(${cmd})"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 70, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 70, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 70, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 70, col 21.
        write(''' --debug --add --list
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 71, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 71, col 17.
        write('''_long_option_debug_add_list () {

  local f=$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 73, col 46
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 73, col 46.
        write(''')))/tests/outfiles/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 73, col 76
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 73, col 76.
        write('''__debug__add__list.out

  local output="$(cat $f)"

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 77, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 77, col 14.
        write(''' --debug --add --list"

  b.unittest.assert_equal \\
    "$output" "$(${cmd})"
}

# test:
# ''')
        _v = VFFSL(SL,"unicode.arrow",True) # '${unicode.arrow}' on line 84, col 4
        if _v is not None: write(_filter(_v, rawExpr='${unicode.arrow}')) # from line 84, col 4.
        write(''' ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 84, col 21
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 84, col 21.
        write(''' --debug --list --add
function b.test.''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 85, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 85, col 17.
        write('''_long_option_debug_list_add () {

  local f=$(dirname $(readlink -f $(which ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 87, col 46
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 87, col 46.
        write(''')))/tests/outfiles/''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 87, col 76
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 87, col 76.
        write('''__debug__add__list.out

  local output="$(cat $f)"

  local cmd="''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 91, col 14
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 91, col 14.
        write(''' --debug --list --add"

  b.unittest.assert_equal \\
    "$output" "$(${cmd})"
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

    _mainCheetahMethod_for_tests__tasks__default_test_sh = 'respond'

## END CLASS DEFINITION

if not hasattr(tests__tasks__default_test_sh, '_initCheetahAttributes'):
    templateAPIClass = getattr(tests__tasks__default_test_sh,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(tests__tasks__default_test_sh)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=tests__tasks__default_test_sh()).run()

