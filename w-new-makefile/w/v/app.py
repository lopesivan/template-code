# encoding: utf-8
"""Criação de arquivos."""

import sys
import os
import os.path
import yaml
import optparse

import models

parser = optparse.OptionParser(usage="%prog -[ [s] --[save] ]", version="%prog 1.0")

#
# -p, --stdout
#
parser.add_option( '-p', '--stdout',
        dest    = "stdout",
        default = False,
        action  = "store_true",
        help    = "Show file in stdout."
        )

#
# -s, --save
#
parser.add_option( '-s', '--save',
        dest    = "save",
        default = False,
        action  = "store_true",
        help    = "Active save mode."
        )

#
# -y, --yml
#
parser.add_option( '-y', '--yml',
        dest    = "yml",
        default = "1.yml",
        help    = "Define yml file"
        )

def main():
    options, remainder = parser.parse_args()

    """Método principal de criação de arquivos."""
    path = options.yml

    if os.path.isfile(path) and os.access(path, os.R_OK):
        # Load YAML file
        config_file = open(path, 'r')
        data_model = yaml.load(config_file, Loader=yaml.BaseLoader)
        #data_model = yaml.load(config_file, Loader=yaml.SafeLoader)
        #data_model = yaml.load(config_file, Loader=yaml.FullLoader)
        config_file.close()

        print(sys.argv[4])
        s = "models.T{}_mk(data_model, 'new_makefile.commmand.{}_mk')".format(sys.argv[4].capitalize(), sys.argv[4])
        t = eval(s)
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        # t = models.TVaca_mk(data_model, 'new_makefile.commmand.vaca_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TVenv_mk(data_model, 'new_makefile.commmand.venv_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TC_mk(data_model, 'new_makefile.commmand.c_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TArduino_profile_mk(data_model, 'new_makefile.commmand.arduino_profile_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TSo_mk(data_model, 'new_makefile.commmand.so_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TConditional(data_model, 'new_makefile.commmand.conditional')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TCpp11_mk(data_model, 'new_makefile.commmand.cpp11_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TS_mk(data_model, 'new_makefile.commmand.s_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TArduino_mk(data_model, 'new_makefile.commmand.arduino_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TJava_mk(data_model, 'new_makefile.commmand.java_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TGo_mk(data_model, 'new_makefile.commmand.go_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TPy_mk(data_model, 'new_makefile.commmand.py_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TModernc_mk(data_model, 'new_makefile.commmand.modernc_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TMaven_mk(data_model, 'new_makefile.commmand.maven_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TM_mk(data_model, 'new_makefile.commmand.m_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

        # t = models.TCpp_mk(data_model, 'new_makefile.commmand.cpp_mk')
        # if options.stdout == True :
        #     t.put()
        # if options.save == True :
        #     t.save()

    else:
        print ("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
