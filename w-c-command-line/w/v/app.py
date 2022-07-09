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

        t = models.THello___world_1(data_model, 'cansi.commmand_line.hello___world_1')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMain_c(data_model, 'cansi.commmand_line.main_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TBoolean_h(data_model, 'cansi.commmand_line.boolean_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTest(data_model, 'cansi.commmand_line.test')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TREADME_md(data_model, 'cansi.commmand_line.README_md')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TAUTHORS(data_model, 'cansi.commmand_line.AUTHORS')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TArgs_h(data_model, 'cansi.commmand_line.args_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TINSTALL(data_model, 'cansi.commmand_line.INSTALL')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TArgs_c(data_model, 'cansi.commmand_line.args_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TCOPYING(data_model, 'cansi.commmand_line.COPYING')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMakefile(data_model, 'cansi.commmand_line.Makefile')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

    else:
        print ("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
