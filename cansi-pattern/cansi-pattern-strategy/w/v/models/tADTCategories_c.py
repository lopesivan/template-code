"""Classe de template."""
from .factory import Factory


class TADTCategories_c(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.name = "ADTCategories_c"

        self.tmpl.adt = data_model['adt']
        self.tmpl.strategy = data_model['strategy']

    def put(self):
        fileName = "%sCategories.c" % self.tmpl.adt['name'].capitalize()
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%sCategories.c" % self.tmpl.adt['name'].capitalize()
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

