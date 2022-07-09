"""Classe de template."""
from .factory import Factory
from .sh import Sh


class TTypedefStruct_h(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name, index):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.index = index
        self.tmpl.cmd = data_model['adt']
        self.tmpl.name = "%s/%s" %(self.tmpl.cmd['dir'], "typedefStruct.h")
        fileName = "%s.h" % self.tmpl.cmd['class'][self.tmpl.index]['name']
        if len(self.tmpl.cmd['dir']) == 0:
            self.tmpl.name = "./%s" %(fileName)
        else:
            self.tmpl.name = "%s/%s" %(self.tmpl.cmd['dir'], fileName)
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
