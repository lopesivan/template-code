"""Classe de template."""
from .factory import Factory
from .sh import Sh
import sys


class TTictac_c(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.cmd = data_model['cmd']
        self.tmpl.name = "%s/%s" %(self.tmpl.cmd['dir'], self.tmpl.cmd['name'])

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName, file=sys.stderr)
        print (self.tmpl)

    def save(self):
        fileName = "%s" % self.tmpl.name
        sh = Sh(fileName)
        sh.mkdir()
        print ("Save File: %s" % fileName, file=sys.stderr)
        open(fileName, 'w').write(str(self.tmpl))
