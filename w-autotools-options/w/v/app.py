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
        default = True,
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

        if len(sys.argv) > 4:
            if len(sys.argv) == 6:
                s = "models.T{}_{}(data_model, 'configure_ac.new_opts.{}_{}')".format( sys.argv[4].capitalize(), sys.argv[5], sys.argv[4], sys.argv[5])
            if len(sys.argv) == 5:
                s = "models.T{}_{}(data_model, 'configure_ac.new_opts.{}_{}')".format( sys.argv[3].capitalize(), sys.argv[4], sys.argv[3], sys.argv[4])

            print (sys.argv[4], file=sys.stderr)

            t = eval(s)

            if options.save == True :
                t.save()
            else:
                t.put()
        else:
            print ("Exemplo de uso:\n")
            print("python app.py {-s} -y file.yml options boolean")

    else:
        print ("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
