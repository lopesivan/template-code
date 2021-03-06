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

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1540961081.615731
__CHEETAH_genTimestamp__ = 'Wed Oct 31 01:44:41 2018'
__CHEETAH_src__ = '../m/common__args__args_c.tmpl'
__CHEETAH_srcLastModified__ = 'Sat Oct 27 04:10:30 2018'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class common__args__args_c(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(common__args__args_c, self).__init__(*args, **KWs)
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
        
        #  comment
        write(u'''#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>

#include "args.h"

void
print_help (void)
{
    printf ("\\
Usage: \\e[1;34m%s\\e[m [OPTION]...\\n\\
Prints \\"Hello, world!\\" to the console.\\n\\
  -h, --help          display this help and exit\\n\\
  -v, --version       display version information and exit\\n\\
\\n\\
Report bugs to: <\\e[1;34m%s\\e[m>\\n\\
hello-world home page: <\\e[1;34m%s\\e[m>\\n", PACKAGE, PACKAGE_BUGREPORT, PACKAGE_URL);
}

void
print_version (void)
{
    printf ("\\
\\e[1;34m%s\\e[m\\n\\
Copyright (C) 2018 %s\\n\\
License GPLv3+: GNU GPL version 3 or later <%s>\\n\\
This is free software: you are free to change and redistribute it.\\n\\
There is NO WARRANTY, to the extent permitted by law.\\n",
    PACKAGE_STRING,
    AUTHOR,
    LICENSE_URL);
}
void
arguments (int argc, char **argv)
{
    int o;

    static struct option long_options[] =
    {
        { "help", no_argument, NULL, \'h\'    },
        { "version", no_argument, NULL, \'v\' },
        { NULL, 0, NULL, 0                  }
    };

    while (1)
    {

        /*
         * getopt_long stores the option index here.
         */
        int option_index = 0;

        o = getopt_long (argc, argv, "hv", long_options, &option_index);

        /*
         * Detect the end of the options.
         */
        if (o == -1)
            break;

        switch (o)
        {
        case \'h\':
            print_help ();
            exit (EXIT_SUCCESS);
            break;

        case \'v\':
            print_version ();
            exit (EXIT_SUCCESS);
            break;

        case \'?\':
            /*
             * getopt_long already printed an error message.
             */
            break;

        default:
            abort ();
        }
    }
}

/* vim: set ts=4 sw=4 tw=78 ft=c: */
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

    _mainCheetahMethod_for_common__args__args_c= 'respond'

## END CLASS DEFINITION

if not hasattr(common__args__args_c, '_initCheetahAttributes'):
    templateAPIClass = getattr(common__args__args_c, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(common__args__args_c)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=common__args__args_c()).run()


