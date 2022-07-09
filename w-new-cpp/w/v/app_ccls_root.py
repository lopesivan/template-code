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

        t = models.TDot_ccls(data_model, 'new_cpp.commmand.dot_ccls')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TDot_ccls___root(data_model, 'new_cpp.commmand.dot_ccls___root')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()
    else:
        print ("Either file is missing or is not readable")

if __name__ == "__main__":
    main()
