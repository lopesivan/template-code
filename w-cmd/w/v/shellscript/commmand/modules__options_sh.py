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
__CHEETAH_genTime__ = 1576846545.5420864
__CHEETAH_genTimestamp__ = 'Fri Dec 20 09:55:45 2019'
__CHEETAH_src__ = '../m/modules__options_sh.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Mar 20 17:34:23 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class modules__options_sh(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(modules__options_sh, self).__init__(*args, **KWs)
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
        
        write('''# modules/options.sh

function ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 3, col 10
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 3, col 10.
        write('''.options.load () {
  # Help (--help and -h added as flags)
  b.opt.add_flag --debug "enable debug mode"
  b.opt.add_flag --help "display this help and exit"
  b.opt.add_flag --version "output version information and exit"

  b.opt.add_flag --add "adiciona path dos arquivos presentes no diretorio"
  b.opt.add_alias --add -a

  b.opt.add_flag --list "lista os ''')
        _v = VFFSL(SL,"cmd.name",True) # '${cmd.name}' on line 12, col 35
        if _v is not None: write(_filter(_v, rawExpr='${cmd.name}')) # from line 12, col 35.
        write('''s"
  b.opt.add_alias --list -l

  b.opt.add_opt --name "Specify name to be used"
  b.opt.add_alias --name -n

  # Set required args (will raise errors if not specified)
  #b.opt.required_args --name
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

    _mainCheetahMethod_for_modules__options_sh = 'respond'

## END CLASS DEFINITION

if not hasattr(modules__options_sh, '_initCheetahAttributes'):
    templateAPIClass = getattr(modules__options_sh,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(modules__options_sh)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=modules__options_sh()).run()


