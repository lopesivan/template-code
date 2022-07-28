"""Classe de template."""
from .factory import Factory
from .sh import Sh
import sys


class TLinux__verbs__preparedot_py(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.data = data_model['data']
        self.tmpl.name = "%s/%s" %(self.tmpl.data['dir'], "linux/verbs/prepare.py".replace("linux", self.tmpl.data['name']))

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName, file=sys.stderr)
        print (self.tmpl)
    def save(self):
        fileName = "%s" % self.tmpl.name
        sh = Sh(fileName)
        sh.mkdir()
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
