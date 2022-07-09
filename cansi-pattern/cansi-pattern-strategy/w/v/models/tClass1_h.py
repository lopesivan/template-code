"""Classe de template."""
from .factory import Factory


class TClass1_h(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name, index):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.index = index

        self.tmpl.adt = data_model['adt']

    def put(self):
        fileName = "%s.h" % self.tmpl.adt['class'][self.tmpl.index]['name']
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%s.h" % self.tmpl.adt['class'][self.tmpl.index]['name']
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

