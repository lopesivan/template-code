# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""

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
        config_file = file(path, 'r')
        data_model = yaml.load(config_file)
        config_file.close()

        t = models.TADT_h(data_model, 'cansi.adt.ADT_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TADT_c(data_model, 'cansi.adt.ADT_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TADTStrategy_h(data_model, 'cansi.adt.ADTStrategy_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TADTCategories_h(data_model, 'cansi.adt.ADTCategories_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMemoryPool_ADT_c(data_model, 'cansi.adt.MemoryPool_ADT_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        for x in range(0, len(data_model['adt']['class'])):
            t = models.TClass1_h(data_model, 'cansi.adt.Class1_h', x)
            if options.stdout == True :
                t.put()
            if options.save == True :
                t.save()

        t = models.TADTCategories_c(data_model, 'cansi.adt.ADTCategories_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
