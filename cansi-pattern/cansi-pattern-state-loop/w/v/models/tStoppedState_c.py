"""Classe de template."""
from .factory import Factory


class TStoppedState_c(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.name = "StoppedState_c"

        self.tmpl.state = data_model['state']

    def put(self):
        fileName = "%sState.c" %self.tmpl.state['stop']['name'].capitalize()
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%sState.c" %self.tmpl.state['stop']['name'].capitalize()
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
