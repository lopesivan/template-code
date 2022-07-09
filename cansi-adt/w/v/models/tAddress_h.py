"""Classe de template."""
from .factory import Factory
from .sh import Sh


class TAddress_h(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.cmd = data_model['adt']
        self.tmpl.name = "%s/%s" %(self.tmpl.cmd['dir'], "Address.h")
        #self.tmpl.log = data_model['log']

    def status(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)
        print (self.tmpl)

    def save(self):
        fileName = "%s" % self.tmpl.name
        sh = Sh(fileName)
        sh.mkdir()
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
