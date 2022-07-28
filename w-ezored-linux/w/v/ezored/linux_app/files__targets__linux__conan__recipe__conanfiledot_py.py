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
__CHEETAH_genTime__ = 1658989387.4263444
__CHEETAH_genTimestamp__ = 'Thu Jul 28 03:23:07 2022'
__CHEETAH_src__ = '../m/files__targets__linux__conan__recipe__conanfiledot_py.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jul 28 02:11:02 2022'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class files__targets__linux__conan__recipe__conanfiledot_py(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(files__targets__linux__conan__recipe__conanfiledot_py, self).__init__(*args, **KWs)
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
        
        write('''from conans import ConanFile, CMake


class TargetConan(ConanFile):
    name = "''')
        _v = VFFSL(SL,"data.name",True) # '${data.name}' on line 5, col 13
        if _v is not None: write(_filter(_v, rawExpr='${data.name}')) # from line 5, col 13.
        write('''"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "ezored_name": "ANY",
        "ezored_version": "ANY",
        "ezored_arch": "ANY",
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "ezored_name": "ezored",
        "ezored_version": "ANY",
        "ezored_arch": "ANY",
        "sqlite3:threadsafe": 1,
        "sqlite3:build_executable": False,
        "poco:enable_apacheconnector": False,
        "poco:enable_activerecord": False,
        "poco:enable_cppparser": False,
        "poco:enable_crypto": True,
        "poco:enable_data": False,
        "poco:enable_data_mysql": False,
        "poco:enable_data_postgresql": False,
        "poco:enable_data_sqlite": False,
        "poco:enable_data_odbc": False,
        "poco:enable_encodings": False,
        "poco:enable_json": True,
        "poco:enable_jwt": True,
        "poco:enable_mongodb": False,
        "poco:enable_net": True,
        "poco:enable_netssl": True,
        "poco:enable_pdf": False,
        "poco:enable_pagecompiler": False,
        "poco:enable_pagecompiler_file2page": False,
        "poco:enable_pocodoc": False,
        "poco:enable_redis": False,
        "poco:enable_sevenzip": False,
        "poco:enable_util": True,
        "poco:enable_xml": True,
        "poco:enable_zip": False,
        "poco:enable_active_record": False,
        "date:header_only": True,
    }
    exports_sources = "*"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = self.settings.build_type
        cmake.definitions["PROJECT_CONFIG_NAME"] = self.options.get_safe("ezored_name")
        cmake.definitions["PROJECT_CONFIG_VERSION"] = self.options.get_safe(
            "ezored_version"
        )
        cmake.definitions["PROJECT_CONFIG_ARCH"] = self.options.get_safe("ezored_arch")
        cmake.configure()
        cmake.build()

    def requirements(self):
        self.requires("sqlite3/3.38.5")
        self.requires("rapidjson/1.1.0")
        self.requires("poco/1.11.3")
        self.requires("openssl/1.1.1o")
        self.requires("sqlitecpp/3.1.1")
        self.requires("date/3.0.1")
        self.requires("nlohmann_json/3.9.1")
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

    _mainCheetahMethod_for_files__targets__linux__conan__recipe__conanfiledot_py = 'respond'

## END CLASS DEFINITION

if not hasattr(files__targets__linux__conan__recipe__conanfiledot_py, '_initCheetahAttributes'):
    templateAPIClass = getattr(files__targets__linux__conan__recipe__conanfiledot_py,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(files__targets__linux__conan__recipe__conanfiledot_py)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=files__targets__linux__conan__recipe__conanfiledot_py()).run()


