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

        t = models.TFiles__modules__targetUNDERscore_linux__cmake__moduledot_cmake(data_model, 'ezored.linux_app.files__modules__targetUNDERscore_linux__cmake__moduledot_cmake')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__config__target_linuxdot_py(data_model, 'ezored.linux_app.files__config__target_linuxdot_py')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__verbs__preparedot_py(data_model, 'ezored.linux_app.files__targets__linux__verbs__preparedot_py')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__verbs__packagedot_py(data_model, 'ezored.linux_app.files__targets__linux__verbs__packagedot_py')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__verbs__distdot_py(data_model, 'ezored.linux_app.files__targets__linux__verbs__distdot_py')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__verbs__builddot_py(data_model, 'ezored.linux_app.files__targets__linux__verbs__builddot_py')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__conan__recipe__conanfiledot_py(data_model, 'ezored.linux_app.files__targets__linux__conan__recipe__conanfiledot_py')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__conan__profile__ezored_linux_profile(data_model, 'ezored.linux_app.files__targets__linux__conan__profile__ezored_linux_profile')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TFiles__targets__linux__cmake__CMakeListsdot_txt(data_model, 'ezored.linux_app.files__targets__linux__cmake__CMakeListsdot_txt')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

    else:
        print ("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
