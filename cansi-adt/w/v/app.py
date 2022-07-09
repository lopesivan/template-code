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
        data_model = yaml.load(config_file)
        config_file.close()

        for x in range(0, len(data_model['adt']['class'])):
            t = models.TTypedefStruct_h(data_model, 'cansi.adt.typedefStruct_h', x)
            if options.stdout == True :
                t.put()
            if options.save == True :
                t.save()
            if ((options.stdout == False) and (options.save == False)) :
                t.status()

        t = models.TCustomer_h(data_model, 'cansi.adt.Customer_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()
        if ((options.stdout == False) and (options.save == False)) :
            t.status()

        t = models.TCustomer_c(data_model, 'cansi.adt.Customer_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()
        if ((options.stdout == False) and (options.save == False)) :
            t.status()

    else:
        print ("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
