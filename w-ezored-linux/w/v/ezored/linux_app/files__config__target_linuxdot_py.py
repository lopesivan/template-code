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
__CHEETAH_genTime__ = 1659042202.4577212
__CHEETAH_genTimestamp__ = 'Thu Jul 28 18:03:22 2022'
__CHEETAH_src__ = '../m/files__config__target_linuxdot_py.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jul 28 18:02:10 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class files__config__target_linuxdot_py(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(files__config__target_linuxdot_py, self).__init__(*args, **KWs)
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
        
        write('''def run(proj_path, target_name, params):
    return {
        "project_name": "''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 3, col 26
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 3, col 26.
        write('''",
        "version": "''')
        _v = VFFSL(SL,"data.project.version",True) # '${data.project.version}' on line 4, col 21
        if _v is not None: write(_filter(_v, rawExpr='${data.project.version}')) # from line 4, col 21.
        write('''",
        "build_types": ''')
        _v = VFN(VFFSL(SL,"data.project.build_types",True),"split",False)("\n")[:-1] # '${data.project.build_types.split("\\n")[:-1]}' on line 5, col 24
        if _v is not None: write(_filter(_v, rawExpr='${data.project.build_types.split("\\n")[:-1]}')) # from line 5, col 24.
        write(''',
        "archs": [
            {
                "arch": "''')
        _v = VFFSL(SL,"data.project.arch",True) # '${data.project.arch}' on line 8, col 26
        if _v is not None: write(_filter(_v, rawExpr='${data.project.arch}')) # from line 8, col 26.
        write('''",
                "conan_arch": "''')
        _v = VFFSL(SL,"data.project.arch",True) # '${data.project.arch}' on line 9, col 32
        if _v is not None: write(_filter(_v, rawExpr='${data.project.arch}')) # from line 9, col 32.
        write('''",
                "conan_profile": "ezored_''')
        _v = VFFSL(SL,"data.name",True) # '${data.name}' on line 10, col 42
        if _v is not None: write(_filter(_v, rawExpr='${data.name}')) # from line 10, col 42.
        write('''_profile",
            },
        ],
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

    _mainCheetahMethod_for_files__config__target_linuxdot_py = 'respond'

## END CLASS DEFINITION

if not hasattr(files__config__target_linuxdot_py, '_initCheetahAttributes'):
    templateAPIClass = getattr(files__config__target_linuxdot_py,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(files__config__target_linuxdot_py)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=files__config__target_linuxdot_py()).run()


