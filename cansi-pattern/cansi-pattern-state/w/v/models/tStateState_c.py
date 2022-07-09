"""Classe de template."""
from .factory import Factory


class TStateState_c(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name, index):

        Factory.__init__(self, template_name)

        self.data_model = data_model
        self.tmpl.index = index

        self.tmpl.name = "StateState_c"

        self.tmpl.state = data_model['state']
        #self.tmpl.log = data_model['log']

    def put(self):
        fileName = "%sState.c" % self.tmpl.state['states'][self.tmpl.index]['name'].capitalize()
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%sState.c" % self.tmpl.state['states'][self.tmpl.index]['name'].capitalize()
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

