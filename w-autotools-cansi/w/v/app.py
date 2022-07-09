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
        config_file = file(path, 'r')
        data_model = yaml.load(config_file)
        config_file.close()

        t = models.TSrc__projectX__Makefile_am(data_model, 'cansi.autotools.src__projectX__Makefile_am')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TM4__autotools_enable_debug_m4(data_model, 'cansi.autotools.m4__autotools_enable_debug_m4')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TSrc__projectX__alpha_c(data_model, 'cansi.autotools.src__projectX__alpha_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TREADME_md(data_model, 'cansi.autotools.README_md')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TCommon__args__args_h(data_model, 'cansi.autotools.common__args__args_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TSrc__projectX__alpha_h(data_model, 'cansi.autotools.src__projectX__alpha_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TSrc__projectX__beta_c(data_model, 'cansi.autotools.src__projectX__beta_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TCommon__args__Makefile_am(data_model, 'cansi.autotools.common__args__Makefile_am')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMakefile_am(data_model, 'cansi.autotools.Makefile_am')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TCommon__args__args_c(data_model, 'cansi.autotools.common__args__args_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TAutogen_sh(data_model, 'cansi.autotools.autogen_sh')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TSrc__projectX__main_c(data_model, 'cansi.autotools.src__projectX__main_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TDot_local_vimrc(data_model, 'cansi.autotools.dot_local_vimrc')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TAbout_c(data_model, 'cansi.autotools.about_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TM4__autotools_disable_gnu_args_m4(data_model, 'cansi.autotools.m4__autotools_disable_gnu_args_m4')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TConfigure_ac(data_model, 'cansi.autotools.configure_ac')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TSrc__projectX__beta_h(data_model, 'cansi.autotools.src__projectX__beta_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TDot_projections_json(data_model, 'cansi.autotools.dot_projections_json')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
