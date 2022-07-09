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
__CHEETAH_version__ = '3.2.4'
__CHEETAH_versionTuple__ = (3, 2, 4, 'final', 0)
__CHEETAH_genTime__ = 1594694038.6184785
__CHEETAH_genTimestamp__ = 'Mon Jul 13 23:33:58 2020'
__CHEETAH_src__ = '../m/maven_mk.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jun 25 20:18:24 2020'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class maven_mk(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(maven_mk, self).__init__(*args, **KWs)
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
        
        write('''package=br.com.fortytwo
project=NameOfProject

all: getting-started-with-maven-java-console-app

getting-started-with-maven-java-console-app:
\t''')
        _v = VFFSL(SL,"unicode.at",True) # '${unicode.at}' on line 7, col 2
        if _v is not None: write(_filter(_v, rawExpr='${unicode.at}')) # from line 7, col 2.
        write('''mvn archetype:generate -DgroupId=$(package) -DartifactId=$(project) -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

clean-project:
\trm -rf $(project)

compile:
\t''')
        _v = VFFSL(SL,"unicode.at",True) # '${unicode.at}' on line 13, col 2
        if _v is not None: write(_filter(_v, rawExpr='${unicode.at}')) # from line 13, col 2.
        write('''(cd $(project); mvn compile)

run:
\t''')
        _v = VFFSL(SL,"unicode.at",True) # '${unicode.at}' on line 16, col 2
        if _v is not None: write(_filter(_v, rawExpr='${unicode.at}')) # from line 16, col 2.
        write('''(cd $(project); mvn exec:java -Dexec.mainClass="$(package).App")

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

    _mainCheetahMethod_for_maven_mk = 'respond'

## END CLASS DEFINITION

if not hasattr(maven_mk, '_initCheetahAttributes'):
    templateAPIClass = getattr(maven_mk,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(maven_mk)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=maven_mk()).run()


