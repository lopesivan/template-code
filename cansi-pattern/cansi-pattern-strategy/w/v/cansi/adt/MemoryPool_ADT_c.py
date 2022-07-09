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

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1550588530.725845
__CHEETAH_genTimestamp__ = 'Tue Feb 19 12:02:10 2019'
__CHEETAH_src__ = '../m/MemoryPool_ADT_c.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Mar  8 03:24:24 2018'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class MemoryPool_ADT_c(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(MemoryPool_ADT_c, self).__init__(*args, **KWs)
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
        
        write(u'''#include "''')
        _v = VFFSL(SL,"adt.name",True) # u'${adt.name}' on line 1, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name}')) # from line 1, col 12.
        write(u'''.h"
''')
        if len(VFFSL(SL,"adt.class",True)) > 0: # generated from line 2, col 1
            write(u'''#include "''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"class",True)[0],"name",True) # u'${adt.class[0].name}' on line 3, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.class[0].name}')) # from line 3, col 12.
            write(u'''.h"
''')
        write(u'''#include <stdlib.h>

struct ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 7, col 8
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 7, col 8.
        write(u'''
{
''')
        for i in range(0, len(VFFSL(SL,"adt.struct",True))): # generated from line 9, col 1
            write(u'''    ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"struct",True)[i],"type",True) # u'${adt.struct[i].type}' on line 10, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.struct[i].type}')) # from line 10, col 5.
            write(u''' ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"struct",True)[i],"name",True) # u'${adt.struct[i].name}' on line 10, col 27
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.struct[i].name}')) # from line 10, col 27.
            write(u''';
''')
        write(u'''};

#define MAX_NO_OF_''')
        _v = VFN(VFFSL(SL,"adt.name",True),"upper",False)() # u'${adt.name.upper()}' on line 14, col 20
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.upper()}')) # from line 14, col 20.
        write(u'''S 42

static struct ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 16, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 16, col 15.
        write(u''' objectPool[MAX_NO_OF_''')
        _v = VFN(VFFSL(SL,"adt.name",True),"upper",False)() # u'${adt.name.upper()}' on line 16, col 61
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.upper()}')) # from line 16, col 61.
        write(u'''S];
static size_t numberOfObjects = 0;

''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 19, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 19, col 1.
        _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 19, col 25
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 19, col 25.
        write(u''' create''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 19, col 42
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 19, col 42.
        write(u'''
''')
        if len(VFFSL(SL,"adt.ctor",True)) > 1: # generated from line 20, col 1
            write(u''' (''')
            for i in range(0, len(VFFSL(SL,"adt.ctor",True))-1): # generated from line 22, col 1
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[i],"type",True) # u'${adt.ctor[i].type}' on line 23, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[i].type}')) # from line 23, col 1.
                write(u''' ''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[i],"name",True) # u'${adt.ctor[i].name}' on line 23, col 21
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[i].name}')) # from line 23, col 21.
                write(u''', ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[-1],"type",True) # u'${adt.ctor[-1].type}' on line 25, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[-1].type}')) # from line 25, col 1.
            write(u''' ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[-1],"name",True) # u'${adt.ctor[-1].name}' on line 25, col 22
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[-1].name}')) # from line 25, col 22.
            write(u''')
''')
        else: # generated from line 27, col 1
            if len(VFFSL(SL,"adt.ctor",True)) == 0: # generated from line 28, col 1
                write(u'''()
''')
            else: # generated from line 30, col 1
                write(u'''(''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"type",True) # u'${adt.ctor[0].type}' on line 31, col 2
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].type}')) # from line 31, col 2.
                write(u''' ''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"name",True) # u'${adt.ctor[0].name}' on line 31, col 22
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].name}')) # from line 31, col 22.
                write(u''')
''')
        write(u'''{
    ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 35, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 35, col 5.
        _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 35, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 35, col 29.
        write(u''' ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 35, col 40
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 35, col 40.
        write(u''' = NULL;

    if (numberOfObjects < MAX_NO_OF_''')
        _v = VFN(VFFSL(SL,"adt.name",True),"upper",False)() # u'${adt.name.upper()}' on line 37, col 37
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.upper()}')) # from line 37, col 37.
        write(u'''S)
    {
        ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 39, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 39, col 9.
        write(u''' = &objectPool[numberOfObjects++];
        /* Initialize the object... */
        ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 41, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 41, col 9.
        write(u'''->''')
        _v = VFN(VFFSL(SL,"strategy.name",True),"lower",False)() # u'${strategy.name.lower()}' on line 41, col 30
        if _v is not None: write(_filter(_v, rawExpr=u'${strategy.name.lower()}')) # from line 41, col 30.
        write(u'''Strategy = ''')
        _v = VFN(VFFSL(SL,"strategy.name",True),"capitalize",False)() # u'${strategy.name.capitalize()}' on line 41, col 65
        if _v is not None: write(_filter(_v, rawExpr=u'${strategy.name.capitalize()}')) # from line 41, col 65.
        write(u'''Strategy;
    }

    return ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 44, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 44, col 12.
        write(u''';
}

void destroy''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 47, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 47, col 13.
        write(u'''
    (''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 48, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 48, col 6.
        _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 48, col 30
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 48, col 30.
        write(u''' ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 48, col 41
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 48, col 41.
        write(u''')
{
    /*
      In case de-allocation is needed, an array will still do, but a more
      sophisticated method for keeping track of "allocated" objects will be
      needed.  However, such an algorithm is outside the scope of this book.
    */
}


void ''')
        _v = VFN(VFFSL(SL,"strategy.method",True),"lower",False)() # u'${strategy.method.lower()}' on line 58, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'${strategy.method.lower()}')) # from line 58, col 6.
        _v = VFN(VFFSL(SL,"strategy.name",True),"capitalize",False)() # u'${strategy.name.capitalize()}' on line 58, col 32
        if _v is not None: write(_filter(_v, rawExpr=u'${strategy.name.capitalize()}')) # from line 58, col 32.
        write(u'''Category''')
        if len(VFFSL(SL,"strategy.ctor",True)) > 1: # generated from line 59, col 1
            write(u'''(''')
            for i in range(0, len(VFFSL(SL,"strategy.ctor",True))-1): # generated from line 61, col 1
                _v = VFN(VFN(VFFSL(SL,"strategy",True),"ctor",True)[i],"type",True) # u'${strategy.ctor[i].type}' on line 62, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'${strategy.ctor[i].type}')) # from line 62, col 1.
                write(u''' ''')
                _v = VFN(VFN(VFFSL(SL,"strategy",True),"ctor",True)[i],"name",True) # u'${strategy.ctor[i].name}' on line 62, col 26
                if _v is not None: write(_filter(_v, rawExpr=u'${strategy.ctor[i].name}')) # from line 62, col 26.
                write(u''', ''')
            _v = VFN(VFN(VFFSL(SL,"strategy",True),"ctor",True)[-1],"type",True) # u'${strategy.ctor[-1].type}' on line 64, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'${strategy.ctor[-1].type}')) # from line 64, col 1.
            write(u''' ''')
            _v = VFN(VFN(VFFSL(SL,"strategy",True),"ctor",True)[-1],"name",True) # u'${strategy.ctor[-1].name}' on line 64, col 27
            if _v is not None: write(_filter(_v, rawExpr=u'${strategy.ctor[-1].name}')) # from line 64, col 27.
            write(u''')
''')
        else: # generated from line 66, col 1
            if len(VFFSL(SL,"strategy.ctor",True)) == 0: # generated from line 67, col 1
                write(u'''()
''')
            else: # generated from line 69, col 1
                write(u'''(''')
                _v = VFN(VFN(VFFSL(SL,"strategy",True),"ctor",True)[0],"type",True) # u'${strategy.ctor[0].type}' on line 70, col 2
                if _v is not None: write(_filter(_v, rawExpr=u'${strategy.ctor[0].type}')) # from line 70, col 2.
                write(u''' ''')
                _v = VFN(VFN(VFFSL(SL,"strategy",True),"ctor",True)[0],"name",True) # u'${strategy.ctor[0].name}' on line 70, col 27
                if _v is not None: write(_filter(_v, rawExpr=u'${strategy.ctor[0].name}')) # from line 70, col 27.
                write(u''')
''')
        write(u'''{
    ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 74, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 74, col 5.
        write(u'''->''')
        _v = VFN(VFFSL(SL,"strategy.name",True),"lower",False)() # u'${strategy.name.lower()}' on line 74, col 26
        if _v is not None: write(_filter(_v, rawExpr=u'${strategy.name.lower()}')) # from line 74, col 26.
        write(u'''Strategy = new''')
        _v = VFN(VFFSL(SL,"strategy.name",True),"capitalize",False)() # u'${strategy.name.capitalize()}' on line 74, col 64
        if _v is not None: write(_filter(_v, rawExpr=u'${strategy.name.capitalize()}')) # from line 74, col 64.
        write(u'''Strategy;
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

    _mainCheetahMethod_for_MemoryPool_ADT_c= 'respond'

## END CLASS DEFINITION

if not hasattr(MemoryPool_ADT_c, '_initCheetahAttributes'):
    templateAPIClass = getattr(MemoryPool_ADT_c, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(MemoryPool_ADT_c)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=MemoryPool_ADT_c()).run()


