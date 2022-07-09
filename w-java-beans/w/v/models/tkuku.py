"""Classe de template."""
from .factory import Factory
from .sh import Sh


class TKuku(Factory):
    """Classe de template."""

    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.tmpl.version = data_model['version']
        self.tmpl.dir = data_model['dir']
        self.tmpl.klass = data_model['Class']
        self.tmpl.name = "%s/%s.kuku" %(self.tmpl.dir, self.tmpl.klass['name'])

    def put(self):
        fileName = "%s" % self.tmpl.name
        print("File: %s" % fileName)
        print(self.tmpl)

    def save(self):
        fileName = "%s" % self.tmpl.name
        sh = Sh(fileName)
        sh.mkdir()
        print("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
