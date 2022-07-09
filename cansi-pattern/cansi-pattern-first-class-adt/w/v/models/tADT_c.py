"""Classe de template."""
from .factory import Factory
from .sh import Sh


class TADT_c(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.adt = data_model['adt']
        fileName = "%s.c" % self.tmpl.adt['name']
        if len(self.tmpl.adt['dir']) == 0:
            self.tmpl.name = "./%s" %(fileName)
        else:
            self.tmpl.name = "%s/%s" %(self.tmpl.adt['dir'], fileName)
        #self.tmpl.log = data_model['log']

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        if len(self.tmpl.adt['dir']) > 0:
            sh = Sh(self.tmpl.adt['dir'])
            sh.mkdir()
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
