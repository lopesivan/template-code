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

        t = models.TState_c(data_model, 'cansi.state.State_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TStartedState_h(data_model, 'cansi.state.StartedState_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TStateInternal_h(data_model, 'cansi.state.StateInternal_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TState_h(data_model, 'cansi.state.State_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMessage_h(data_model, 'cansi.state.message_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TStoppedState_c(data_model, 'cansi.state.StoppedState_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMain_c(data_model, 'cansi.state.main_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TContext_c(data_model, 'cansi.state.Context_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TContext_h(data_model, 'cansi.state.Context_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TStartedState_c(data_model, 'cansi.state.StartedState_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TMessage_c(data_model, 'cansi.state.message_c')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        t = models.TStoppedState_h(data_model, 'cansi.state.StoppedState_h')
        if options.stdout == True :
            t.put()
        if options.save == True :
            t.save()

        if len(data_model['state']['states']) > 0 :
            for x in range(0, len(data_model['state']['states'])):
                t = models.TStateState_h(data_model, 'cansi.state.StateState_h',x)
                if options.stdout == True :
                    t.put()
                if options.save == True :
                    t.save()

                t = models.TStateState_c(data_model, 'cansi.state.StateState_c',x)
                if options.stdout == True :
                    t.put()
                if options.save == True :
                    t.save()

    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
