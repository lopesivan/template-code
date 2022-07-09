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

        t = models.TTemplate(data_model, 'shellscript.commmand.template')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTests__file_test_sh(data_model, 'shellscript.commmand.tests__file_test_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTemplate_bash(data_model, 'shellscript.commmand.template_bash')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__usage_sh(data_model, 'shellscript.commmand.tasks__usage_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TModules__exception_sh(data_model, 'shellscript.commmand.modules__exception_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TModules__config_sh(data_model, 'shellscript.commmand.modules__config_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTests__tasks__git_test_sh(data_model, 'shellscript.commmand.tests__tasks__git_test_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TEtc__rules__run_mk(data_model, 'shellscript.commmand.etc__rules__run_mk')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TEtc__rules__build_mk(data_model, 'shellscript.commmand.etc__rules__build_mk')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__completions_sh(data_model, 'shellscript.commmand.tasks__completions_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TModules__options_sh(data_model, 'shellscript.commmand.modules__options_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__commands_sh(data_model, 'shellscript.commmand.tasks__commands_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TLocalexecutable(data_model, 'shellscript.commmand.localexecutable')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__subcmd__ls_sh(data_model, 'shellscript.commmand.tasks__subcmd__ls_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__java_sh(data_model, 'shellscript.commmand.tasks__java_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTests__tasks__completions_test_sh(data_model, 'shellscript.commmand.tests__tasks__completions_test_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__subcmd__beans_sh(data_model, 'shellscript.commmand.tasks__subcmd__beans_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TEtc__rules__tests_mk(data_model, 'shellscript.commmand.etc__rules__tests_mk')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTests__tasks__default_test_sh(data_model, 'shellscript.commmand.tests__tasks__default_test_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.THOWTOCLONE(data_model, 'shellscript.commmand.HOWTOCLONE')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TEtc__templatedoc_json(data_model, 'shellscript.commmand.etc__templatedoc_json')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__init_sh(data_model, 'shellscript.commmand.tasks__init_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TEtc__completion_bash(data_model, 'shellscript.commmand.etc__completion_bash')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTests__tasks__commands_test_sh(data_model, 'shellscript.commmand.tests__tasks__commands_test_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMakefile(data_model, 'shellscript.commmand.Makefile')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TDot_projections_json(data_model, 'shellscript.commmand.dot_projections_json')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TTasks__default_sh(data_model, 'shellscript.commmand.tasks__default_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TModules__exit_sh(data_model, 'shellscript.commmand.modules__exit_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

    else:
        print ("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
