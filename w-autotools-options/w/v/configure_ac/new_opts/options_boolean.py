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
__CHEETAH_version__ = '3.2.6.post1'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 1)
__CHEETAH_genTime__ = 1657551357.808246
__CHEETAH_genTimestamp__ = 'Mon Jul 11 11:55:57 2022'
__CHEETAH_src__ = '../m/options_boolean.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Jul 11 11:55:55 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class options_boolean(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(options_boolean, self).__init__(*args, **KWs)
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
        
        if VFFSL(SL,"data.arg.value",True) == 'true': # generated from line 1, col 1
            write('''variable: ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 2, col 11
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 2, col 11.
            write('''
value: TRUE

file: m4/autotools_disable_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 5, col 28
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 5, col 28.
            write('''.m4
dnl = [begin] ================================================================
dnl [ --disable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 7, col 17
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 7, col 17.
            write(''' ]
dnl The variable ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 8, col 18
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 8, col 18.
            write(''' is TRUE
dnl Usage:
dnl * CONVERT TO FALSE
dnl ----------------------------------------they are equivalent
dnl ./configure  --enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 12, col 27
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 12, col 27.
            write('''=no
dnl ./configure  --disable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 13, col 28
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 13, col 28.
            write('''
dnl
dnl * IN C CODE:
dnl #if ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 16, col 10
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 16, col 10.
            write('''  // <- default: TRUE
dnl     printf ("%s is TRUE\\n", "''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 17, col 34
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 17, col 34.
            write('''");
dnl #else // --disable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 18, col 25
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 18, col 25.
            write('''
dnl        // <- FALSE
dnl     printf ("%s is FALSE\\n", "''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 20, col 35
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 20, col 35.
            write('''");
dnl #endif
dnl
dnl     |----------------------+---------------+-------|
dnl     | Command Line         | Variable      | State |
dnl     |----------------------+---------------+-------|
dnl     | ""                   | WITH_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 26, col 39
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 26, col 39.
            write(''' | 1     | <- default
dnl     | "--disable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 27, col 22
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 27, col 22.
            write('''" | WITH_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 27, col 73
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 27, col 73.
            write(''' | 0     |
dnl     |----------------------+---------------+-------|
dnl
AC_ARG_ENABLE([''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 30, col 16
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 30, col 16.
            write('''],
  [AS_HELP_STRING([--disable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 31, col 30
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 31, col 30.
            write('''],
    [disable ''')
            _v = VFFSL(SL,"data.arg.name",True) # '${data.arg.name}' on line 32, col 14
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name}')) # from line 32, col 14.
            write(''' @<:@default: no@:>@])],
  [''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 33, col 4
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 33, col 4.
            write('''=${enableval}], [''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 33, col 64
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 33, col 64.
            write('''=yes])

if test "x${''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 35, col 14
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 35, col 14.
            write('''}" = xyes; then
   AC_DEFINE(''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 36, col 14
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 36, col 14.
            write(''', 1, [Enable args])
fi
dnl = [end] ==================================================================

file: ''')
            _v = VFFSL(SL,"data.name",True) # '${data.name}' on line 40, col 7
            if _v is not None: write(_filter(_v, rawExpr='${data.name}')) # from line 40, col 7.
            write('''
dnl = [begin] ================================================================
m4_include([m4/autotools_disable_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 42, col 34
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 42, col 34.
            write('''.m4])

AM_CONDITIONAL([WITH_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 44, col 22
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 44, col 22.
            write('''], [test x${''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 44, col 77
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 44, col 77.
            write('''} = xyes])
dnl = [end] ==================================================================
''')
        else: # generated from line 46, col 1
            write('''variable: ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 47, col 11
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 47, col 11.
            write('''
value: FALSE

file: m4/autotools_enable_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 50, col 27
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 50, col 27.
            write('''.m4
dnl = [begin] ================================================================
dnl [ --enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 52, col 16
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 52, col 16.
            write(''' ]
dnl The variable ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 53, col 18
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 53, col 18.
            write(''' is FALSE
dnl Usage:
dnl * CONVERT TO TRUE
dnl ----------------------------------------they are equivalent
dnl ./configure  --enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 57, col 27
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 57, col 27.
            write('''
dnl ./configure  --enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 58, col 27
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 58, col 27.
            write('''=yes
dnl
dnl * IN C CODE:
dnl #if ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 61, col 10
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 61, col 10.
            write('''  // --enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 61, col 66
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 61, col 66.
            write('''
dnl        // <- TRUE
dnl     printf ("%s is TRUE\\n", "''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 63, col 34
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 63, col 34.
            write('''");
dnl #else // <- default: FALSE
dnl     printf ("%s is FALSE\\n", "''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 65, col 35
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 65, col 35.
            write('''");
dnl #endif
dnl
dnl     |----------------------+---------------+-------|
dnl     | Command Line         | Variable      | State |
dnl     |----------------------+---------------+-------|
dnl     | ""                   | WITH_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 71, col 39
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 71, col 39.
            write(''' | 0     | <- default
dnl     | "--enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 72, col 21
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 72, col 21.
            write('''"  | WITH_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 72, col 73
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 72, col 73.
            write(''' | 1     |
dnl     |----------------------+---------------+-------|
dnl
AC_ARG_ENABLE([''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 75, col 16
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 75, col 16.
            write('''],
  [AS_HELP_STRING([--enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 76, col 29
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 76, col 29.
            write('''],
    [Turn on ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 77, col 14
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 77, col 14.
            write(''' @<:@default: no@:>@])],
  [case "${enableval}" in
    yes) ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 79, col 10
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 79, col 10.
            write('''=true ;;
    no)  ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 80, col 10
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 80, col 10.
            write('''=false ;;
    *) AC_MSG_ERROR([bad value ${enableval} for --enable-''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '-') # '${data.arg.name.lower().replace(" ", \'-\')}' on line 81, col 59
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'-\')}')) # from line 81, col 59.
            write(''']) ;;
  esac],
  [''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 83, col 4
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 83, col 4.
            write('''=false])

if test "x${''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 85, col 14
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 85, col 14.
            write('''}" = xtrue; then
  AC_DEFINE(''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 86, col 13
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 86, col 13.
            write(''', 1, [Turn on ''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 86, col 69
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 86, col 69.
            write('''])
fi
dnl = [end] ==================================================================

file: ''')
            _v = VFFSL(SL,"data.name",True) # '${data.name}' on line 90, col 7
            if _v is not None: write(_filter(_v, rawExpr='${data.name}')) # from line 90, col 7.
            write('''
dnl = [begin] ================================================================
m4_include([m4/autotools_enable_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 92, col 33
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 92, col 33.
            write('''.m4])

AM_CONDITIONAL([WITH_''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"upper",False)(),"replace",False)(" ", '_') # '${data.arg.name.upper().replace(" ", \'_\')}' on line 94, col 22
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.upper().replace(" ", \'_\')}')) # from line 94, col 22.
            write('''], [test x$''')
            _v = VFN(VFN(VFFSL(SL,"data.arg.name",True),"lower",False)(),"replace",False)(" ", '_') # '${data.arg.name.lower().replace(" ", \'_\')}' on line 94, col 76
            if _v is not None: write(_filter(_v, rawExpr='${data.arg.name.lower().replace(" ", \'_\')}')) # from line 94, col 76.
            write(''' = xtrue])
dnl = [end] ==================================================================


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

    _mainCheetahMethod_for_options_boolean = 'respond'

## END CLASS DEFINITION

if not hasattr(options_boolean, '_initCheetahAttributes'):
    templateAPIClass = getattr(options_boolean,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(options_boolean)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=options_boolean()).run()


