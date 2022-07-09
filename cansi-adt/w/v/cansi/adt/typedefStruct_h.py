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
__CHEETAH_version__ = '3.2.3'
__CHEETAH_versionTuple__ = (3, 2, 3, 'final', 0)
__CHEETAH_genTime__ = 1568016542.3851314
__CHEETAH_genTimestamp__ = 'Mon Sep  9 05:09:02 2019'
__CHEETAH_src__ = '../m/typedefStruct_h.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Sep  9 05:08:53 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class typedefStruct_h(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(typedefStruct_h, self).__init__(*args, **KWs)
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
        
        id = VFSL([locals()]+SL+[globals(), builtin],"index",True)
        write('''#ifndef ''')
        _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"name",True),"upper",False)() # '${cmd.class[id].name.upper()}' on line 2, col 10
        if _v is not None: write(_filter(_v, rawExpr='${cmd.class[id].name.upper()}')) # from line 2, col 10.
        write('''_H
#define ''')
        _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"name",True),"upper",False)() # '${cmd.class[id].name.upper()}' on line 3, col 10
        if _v is not None: write(_filter(_v, rawExpr='${cmd.class[id].name.upper()}')) # from line 3, col 10.
        write('''_H
''')
        if len(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"include",True)) > 0: # generated from line 4, col 1
            for i in range(0, len(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"include",True))): # generated from line 5, col 1
                write('''#include "''')
                _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"include",True)[i],"name",True) # '${cmd.class[id].include[i].name}' on line 6, col 12
                if _v is not None: write(_filter(_v, rawExpr='${cmd.class[id].include[i].name}')) # from line 6, col 12.
                write('''"
''')
        write("""
/*
I never really dive into the details of this type.
Let's just create a dummy placeholder for the information.
*/
typedef struct
{
""")
        for i in range(0, len(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"struct",True))): # generated from line 16, col 1
            write('''    ''')
            _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"struct",True)[i],"type",True) # '${cmd.class[id].struct[i].type}' on line 17, col 5
            if _v is not None: write(_filter(_v, rawExpr='${cmd.class[id].struct[i].type}')) # from line 17, col 5.
            write(''' ''')
            _v = VFN(VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"struct",True)[i],"name",True) # '${cmd.class[id].struct[i].name}' on line 17, col 37
            if _v is not None: write(_filter(_v, rawExpr='${cmd.class[id].struct[i].name}')) # from line 17, col 37.
            write(''';
''')
        write('''} ''')
        _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[id],"name",True) # '${cmd.class[id].name}' on line 19, col 3
        if _v is not None: write(_filter(_v, rawExpr='${cmd.class[id].name}')) # from line 19, col 3.
        write(''';

#endif
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

    _mainCheetahMethod_for_typedefStruct_h = 'respond'

## END CLASS DEFINITION

if not hasattr(typedefStruct_h, '_initCheetahAttributes'):
    templateAPIClass = getattr(typedefStruct_h,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(typedefStruct_h)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=typedefStruct_h()).run()


