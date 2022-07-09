"""Classe de template."""
from .factory import Factory
from .sh import Sh


class TConfigure_ac(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.autotools = data_model['autotools']
        self.tmpl.name = "%s/%s" %(self.tmpl.autotools['dir'], "configure.ac")
        #self.tmpl.log = data_model['log']

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)
        print self.tmpl
    def save(self):
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
