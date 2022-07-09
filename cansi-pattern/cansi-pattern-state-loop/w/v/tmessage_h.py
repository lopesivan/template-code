"""Classe de template."""
from .factory import Factory


class TMessage_h(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.name = "message_h"

        #self.tmpl.log = data_model['log']

    def put(self):
        fileName = "message.h"
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "message.h"
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

