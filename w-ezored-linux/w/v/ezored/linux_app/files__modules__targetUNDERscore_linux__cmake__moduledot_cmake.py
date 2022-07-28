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
__CHEETAH_genTime__ = 1659045630.4152172
__CHEETAH_genTimestamp__ = 'Thu Jul 28 19:00:30 2022'
__CHEETAH_src__ = '../m/files__modules__targetUNDERscore_linux__cmake__moduledot_cmake.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jul 28 18:53:42 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class files__modules__targetUNDERscore_linux__cmake__moduledot_cmake(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(files__modules__targetUNDERscore_linux__cmake__moduledot_cmake, self).__init__(*args, **KWs)
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
        
        write('''if(PROJECT_TARGET_NAME STREQUAL "''')
        _v = VFFSL(SL,"data.name",True) # '${data.name}' on line 1, col 34
        if _v is not None: write(_filter(_v, rawExpr='${data.name}')) # from line 1, col 34.
        write('''")
    # module files
    file(GLOB H_FILES_C "${PROJECT_ROOT_PATH}/projects/others/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 3, col 64
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 3, col 64.
        write('''/include/*.h")
    file(GLOB H_FILES_CXX "${PROJECT_ROOT_PATH}/projects/others/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 4, col 66
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 4, col 66.
        write('''/include/*.hpp")

    file(GLOB S_FILES_CXX "${PROJECT_ROOT_PATH}/projects/others/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 6, col 66
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 6, col 66.
        write('''/src/*.cpp")

    file(GLOB H_FILES_LOGGER_IMPL "${PROJECT_MODULES_PATH}/logger/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 8, col 87
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 8, col 87.
        write('''/util/Simple*.hpp")
    file(GLOB S_FILES_LOGGER_IMPL "${PROJECT_MODULES_PATH}/logger/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 9, col 87
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 9, col 87.
        write('''/util/Simple*.cpp")

    file(GLOB H_FILES_HTTP_CLIENT_IMPL "${PROJECT_MODULES_PATH}/http-client/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 11, col 97
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 11, col 97.
        write('''/net/http/Simple*.hpp")
    file(GLOB S_FILES_HTTP_CLIENT_IMPL "${PROJECT_MODULES_PATH}/http-client/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 12, col 97
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 12, col 97.
        write('''/net/http/Simple*.cpp")

    file(GLOB H_FILES_SHARED_DATA_IMPL "${PROJECT_MODULES_PATH}/shared-data/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 14, col 97
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 14, col 97.
        write('''/data/Simple*.hpp")
    file(GLOB S_FILES_SHARED_DATA_IMPL "${PROJECT_MODULES_PATH}/shared-data/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 15, col 97
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 15, col 97.
        write('''/data/Simple*.cpp")

    file(GLOB H_FILES_FILE_HELPER_IMPL "${PROJECT_MODULES_PATH}/file-helper/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 17, col 97
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 17, col 97.
        write('''/io/Simple*.hpp")
    file(GLOB S_FILES_FILE_HELPER_IMPL "${PROJECT_MODULES_PATH}/file-helper/implementation/cpp/''')
        _v = VFFSL(SL,"data.project.name",True) # '${data.project.name}' on line 18, col 97
        if _v is not None: write(_filter(_v, rawExpr='${data.project.name}')) # from line 18, col 97.
        write('''/io/Simple*.cpp")

    # header files
    project_add_header_files("${H_FILES_C}")
    project_add_header_files("${H_FILES_CXX}")

    project_add_header_files("${H_FILES_LOGGER_IMPL}")
    project_add_header_files("${H_FILES_HTTP_CLIENT_IMPL}")
    project_add_header_files("${H_FILES_SHARED_DATA_IMPL}")
    project_add_header_files("${H_FILES_FILE_HELPER_IMPL}")

    # source files
    project_add_source_files("${S_FILES_CXX}")

    project_add_source_files("${S_FILES_LOGGER_IMPL}")
    project_add_source_files("${S_FILES_HTTP_CLIENT_IMPL}")
    project_add_source_files("${S_FILES_SHARED_DATA_IMPL}")
    project_add_source_files("${S_FILES_FILE_HELPER_IMPL}")
endif()

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

    _mainCheetahMethod_for_files__modules__targetUNDERscore_linux__cmake__moduledot_cmake = 'respond'

## END CLASS DEFINITION

if not hasattr(files__modules__targetUNDERscore_linux__cmake__moduledot_cmake, '_initCheetahAttributes'):
    templateAPIClass = getattr(files__modules__targetUNDERscore_linux__cmake__moduledot_cmake,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(files__modules__targetUNDERscore_linux__cmake__moduledot_cmake)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=files__modules__targetUNDERscore_linux__cmake__moduledot_cmake()).run()

