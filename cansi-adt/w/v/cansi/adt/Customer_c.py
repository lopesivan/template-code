#!/usr/bin/env python
# -*- coding: utf-8 -*-




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
__CHEETAH_genTime__ = 1568019487.0705307
__CHEETAH_genTimestamp__ = 'Mon Sep  9 05:58:07 2019'
__CHEETAH_src__ = '../m/Customer_c.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Sep  9 05:44:21 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Customer_c(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Customer_c, self).__init__(*args, **KWs)
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
        
        write('''#include "''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 2, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 2, col 12.
        write('''.h"
''')
        if len(VFSL([locals()]+SL+[globals(), builtin],"cmd.class",True)) > 0: # generated from line 3, col 1
            write('''/*
''')
            for i in range(0, len(VFSL([locals()]+SL+[globals(), builtin],"cmd.class",True))): # generated from line 5, col 1
                write('''#include "''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"class",True)[i],"name",True) # '${cmd.class[i].name}' on line 6, col 12
                if _v is not None: write(_filter(_v, rawExpr='${cmd.class[i].name}')) # from line 6, col 12.
                write('''.h"
''')
        write('''*/
#include <stdlib.h>

struct ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 12, col 8
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 12, col 8.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.suffix",True) # '${cmd.suffix}' on line 12, col 19
        if _v is not None: write(_filter(_v, rawExpr='${cmd.suffix}')) # from line 12, col 19.
        write('''
{
''')
        for i in range(0, len(VFSL([locals()]+SL+[globals(), builtin],"cmd.struct",True))): # generated from line 14, col 1
            write('''    ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"struct",True)[i],"type",True) # '${cmd.struct[i].type}' on line 15, col 5
            if _v is not None: write(_filter(_v, rawExpr='${cmd.struct[i].type}')) # from line 15, col 5.
            write(''' ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"struct",True)[i],"name",True) # '${cmd.struct[i].name}' on line 15, col 27
            if _v is not None: write(_filter(_v, rawExpr='${cmd.struct[i].name}')) # from line 15, col 27.
            write(''';
''')
        write('''};

#ifdef NOMEMMORY
#define MAX_NO_OF_''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"upper",False)() # '${cmd.name.upper()}' on line 20, col 20
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.upper()}')) # from line 20, col 20.
        write('''S ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.objects",True) # '${cmd.objects}' on line 20, col 41
        if _v is not None: write(_filter(_v, rawExpr='${cmd.objects}')) # from line 20, col 41.
        write('''

static struct ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 22, col 15
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 22, col 15.
        write(''' objectPool[MAX_NO_OF_''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"upper",False)() # '${cmd.name.upper()}' on line 22, col 48
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.upper()}')) # from line 22, col 48.
        write('''S];
static size_t numberOfObjects = 0;


''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 26, col 1
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 26, col 1.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 26, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 26, col 12.
        write(''' create''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 26, col 29
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 26, col 29.
        if len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True)) > 1: # generated from line 27, col 1
            write('''(''')
            for i in range(0, len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True))-1): # generated from line 29, col 1
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"type",True) # '${cmd.ctor[i].type}' on line 30, col 1
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].type}')) # from line 30, col 1.
                write(''' ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"name",True) # '${cmd.ctor[i].name}' on line 30, col 21
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].name}')) # from line 30, col 21.
                write(''', ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"type",True) # '${cmd.ctor[-1].type}' on line 32, col 1
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].type}')) # from line 32, col 1.
            write(''' ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"name",True) # '${cmd.ctor[-1].name}' on line 32, col 22
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].name}')) # from line 32, col 22.
            write(''')
''')
        else: # generated from line 34, col 1
            if len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True)) == 0: # generated from line 35, col 1
                write('''()
''')
            else: # generated from line 37, col 1
                write('''    (''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[0],"type",True) # '${cmd.ctor[0].type}' on line 38, col 6
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[0].type}')) # from line 38, col 6.
                write(''' ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[0],"name",True) # '${cmd.ctor[0].name}' on line 38, col 26
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[0].name}')) # from line 38, col 26.
                write(''')
''')
        write('''{
    ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 42, col 5
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 42, col 5.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 42, col 16
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 42, col 16.
        write(''' ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 42, col 27
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 42, col 27.
        write(''' = NULL;

    if (numberOfObjects < MAX_NO_OF_''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"upper",False)() # '${cmd.name.upper()}' on line 44, col 37
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.upper()}')) # from line 44, col 37.
        write('''S)
    {
        customer = &objectPool[numberOfObjects++];
        /* Initialize the object... */
        /* Initialize each field in the ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 48, col 41
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 48, col 41.
        write('''... */
''')
        for i in range(0, len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True))-1): # generated from line 49, col 1
            write('''        ''')
            _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 50, col 9
            if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 50, col 9.
            write('''->''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"name",True) # '${cmd.ctor[i].name}' on line 50, col 30
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].name}')) # from line 50, col 30.
            write(''' = ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"name",True) # '${cmd.ctor[i].name}' on line 50, col 52
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].name}')) # from line 50, col 52.
            write(''';
''')
        write('''        ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 52, col 9
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 52, col 9.
        write('''->''')
        _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"name",True) # '${cmd.ctor[-1].name}' on line 52, col 30
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].name}')) # from line 52, col 30.
        write(''' = ''')
        _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"name",True) # '${cmd.ctor[-1].name}' on line 52, col 53
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].name}')) # from line 52, col 53.
        write(''';
    }

    return ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 55, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 55, col 12.
        write(''';
}


void destroy''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 59, col 13
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 59, col 13.
        write('''(''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 60, col 2
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 60, col 2.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 60, col 13
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 60, col 13.
        write(''' ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 60, col 24
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 60, col 24.
        write(''')
{
    /* Perform clean-up of the ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 62, col 32
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 62, col 32.
        write(''' internals, if necessary.
    free (''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 63, col 11
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 63, col 11.
        write(''');
    */
}

#else

''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 69, col 1
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 69, col 1.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 69, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 69, col 12.
        write(''' create''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 69, col 29
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 69, col 29.
        if len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True)) > 1: # generated from line 70, col 1
            write('''(''')
            for i in range(0, len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True))-1): # generated from line 72, col 1
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"type",True) # '${cmd.ctor[i].type}' on line 73, col 1
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].type}')) # from line 73, col 1.
                write(''' ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"name",True) # '${cmd.ctor[i].name}' on line 73, col 21
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].name}')) # from line 73, col 21.
                write(''', ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"type",True) # '${cmd.ctor[-1].type}' on line 75, col 1
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].type}')) # from line 75, col 1.
            write(''' ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"name",True) # '${cmd.ctor[-1].name}' on line 75, col 22
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].name}')) # from line 75, col 22.
            write(''')
''')
        else: # generated from line 77, col 1
            if len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True)) == 0: # generated from line 78, col 1
                write('''()
''')
            else: # generated from line 80, col 1
                write('''    (''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[0],"type",True) # '${cmd.ctor[0].type}' on line 81, col 6
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[0].type}')) # from line 81, col 6.
                write(''' ''')
                _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[0],"name",True) # '${cmd.ctor[0].name}' on line 81, col 26
                if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[0].name}')) # from line 81, col 26.
                write(''')
''')
        write('''{
    ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 85, col 5
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 85, col 5.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 85, col 16
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 85, col 16.
        write(''' ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 85, col 27
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 85, col 27.
        write(''' = malloc (sizeof *''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 85, col 65
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 85, col 65.
        write(''');

    if (NULL != ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 87, col 17
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 87, col 17.
        write(''')
    {
        /* Initialize each field in the ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 89, col 41
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 89, col 41.
        write('''... */
''')
        for i in range(0, len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True))-1): # generated from line 90, col 1
            write('''        ''')
            _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 91, col 9
            if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 91, col 9.
            write('''->''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"name",True) # '${cmd.ctor[i].name}' on line 91, col 30
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].name}')) # from line 91, col 30.
            write(''' = ''')
            _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[i],"name",True) # '${cmd.ctor[i].name}' on line 91, col 52
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[i].name}')) # from line 91, col 52.
            write(''';
''')
        write('''        ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 93, col 9
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 93, col 9.
        write('''->''')
        _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"name",True) # '${cmd.ctor[-1].name}' on line 93, col 30
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].name}')) # from line 93, col 30.
        write(''' = ''')
        _v = VFN(VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd",True),"ctor",True)[-1],"name",True) # '${cmd.ctor[-1].name}' on line 93, col 53
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ctor[-1].name}')) # from line 93, col 53.
        write(''';
    }

    return ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 96, col 12
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 96, col 12.
        write(''';
}


void destroy''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 100, col 13
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 100, col 13.
        write('''(''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 101, col 2
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 101, col 2.
        _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 101, col 13
        if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 101, col 13.
        write(''' ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 101, col 24
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 101, col 24.
        write(''')
{
    /* Perform clean-up of the ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 103, col 32
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 103, col 32.
        write(''' internals, if necessary. */
    free (''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 104, col 11
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 104, col 11.
        write(''');
}
#endif

''')
        if len(VFSL([locals()]+SL+[globals(), builtin],"cmd.ctor",True)) > 1: # generated from line 108, col 1
            write('''void show''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 109, col 10
            if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 109, col 10.
            write('''(''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True) # '${cmd.name}' on line 110, col 2
            if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 110, col 2.
            _v = VFSL([locals()]+SL+[globals(), builtin],"cmd.ptr",True) # '${cmd.ptr}' on line 110, col 13
            if _v is not None: write(_filter(_v, rawExpr='${cmd.ptr}')) # from line 110, col 13.
            write(''' ''')
            _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"cmd.name",True),"lower",False)() # '${cmd.name.lower()}' on line 110, col 24
            if _v is not None: write(_filter(_v, rawExpr='${cmd.name.lower()}')) # from line 110, col 24.
            write(''')
{
    printf ("%s\\n", "Not implemented yet");
}
''')
        write('''
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

    _mainCheetahMethod_for_Customer_c = 'respond'

## END CLASS DEFINITION

if not hasattr(Customer_c, '_initCheetahAttributes'):
    templateAPIClass = getattr(Customer_c,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Customer_c)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Customer_c()).run()

