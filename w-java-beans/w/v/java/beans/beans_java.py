#!/usr/bin/env python
# -*- coding: UTF-8 -*-




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
__CHEETAH_version__ = '3.2.6.post2'
__CHEETAH_versionTuple__ = (3, 2, 6, 'post', 2)
__CHEETAH_genTime__ = 1621218549.4370422
__CHEETAH_genTimestamp__ = 'Sun May 16 23:29:09 2021'
__CHEETAH_src__ = '../m/beans_java.tmpl'
__CHEETAH_srcLastModified__ = 'Sun May 16 22:50:09 2021'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class beans_java(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(beans_java, self).__init__(*args, **KWs)
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
        
        write('''public class ''')
        _v = VFFSL(SL,"klass.name",True) # '$klass.name' on line 3, col 14
        if _v is not None: write(_filter(_v, rawExpr='$klass.name')) # from line 3, col 14.
        write(''' implements java.io.Serializable {
''')
        for att in VFFSL(SL,"klass.attributes",True): # generated from line 4, col 1
            type = list(VFN(VFFSL(SL,"att",True),"values",False)())[0]
            name = list(VFN(VFFSL(SL,"att",True),"keys",False)())[0]
            write('''    private ''')
            _v = VFFSL(SL,"type",True) # '${type}' on line 7, col 13
            if _v is not None: write(_filter(_v, rawExpr='${type}')) # from line 7, col 13.
            write(''' ''')
            _v = VFFSL(SL,"name",True) # '${name}' on line 7, col 21
            if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 7, col 21.
            write(''';
''')
        write('''
''')
        for att in VFFSL(SL,"klass.attributes",True): # generated from line 10, col 1
            type = list(VFN(VFFSL(SL,"att",True),"values",False)())[0]
            name = list(VFN(VFFSL(SL,"att",True),"keys",False)())[0]
            if type == "boolean": # generated from line 13, col 1
                write('''    public ''')
                _v = VFFSL(SL,"type",True) # '${type}' on line 14, col 12
                if _v is not None: write(_filter(_v, rawExpr='${type}')) # from line 14, col 12.
                write(''' is''')
                _v = VFN(VFFSL(SL,"name",True),"title",False)() # '${name.title()}' on line 14, col 22
                if _v is not None: write(_filter(_v, rawExpr='${name.title()}')) # from line 14, col 22.
                write('''()
    {
        return this.''')
                _v = VFFSL(SL,"name",True) # '${name}' on line 16, col 21
                if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 16, col 21.
                write(''';
    }
''')
            else: # generated from line 18, col 1
                write('''    public ''')
                _v = VFFSL(SL,"type",True) # '${type}' on line 19, col 12
                if _v is not None: write(_filter(_v, rawExpr='${type}')) # from line 19, col 12.
                write(''' get''')
                _v = VFN(VFFSL(SL,"name",True),"title",False)() # '${name.title()}' on line 19, col 23
                if _v is not None: write(_filter(_v, rawExpr='${name.title()}')) # from line 19, col 23.
                write('''()
    {
        return this.''')
                _v = VFFSL(SL,"name",True) # '${name}' on line 21, col 21
                if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 21, col 21.
                write(''';
    }
''')
            write('''
    public void set''')
            _v = VFN(VFFSL(SL,"name",True),"title",False)() # '${name.title()}' on line 25, col 20
            if _v is not None: write(_filter(_v, rawExpr='${name.title()}')) # from line 25, col 20.
            write(''' (''')
            _v = VFFSL(SL,"type",True) # '${type}' on line 25, col 37
            if _v is not None: write(_filter(_v, rawExpr='${type}')) # from line 25, col 37.
            write(''' ''')
            _v = VFFSL(SL,"name",True) # '${name}' on line 25, col 45
            if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 25, col 45.
            write(''')
    {
        this.''')
            _v = VFFSL(SL,"name",True) # '${name}' on line 27, col 14
            if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 27, col 14.
            write(''' = ''')
            _v = VFFSL(SL,"name",True) # '${name}' on line 27, col 24
            if _v is not None: write(_filter(_v, rawExpr='${name}')) # from line 27, col 24.
            write(''';
    }

''')
        write('''}

// vim: set ts=4 sw=4 tw=78 ft=java:
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

    _mainCheetahMethod_for_beans_java = 'respond'

## END CLASS DEFINITION

if not hasattr(beans_java, '_initCheetahAttributes'):
    templateAPIClass = getattr(beans_java,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(beans_java)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=beans_java()).run()


