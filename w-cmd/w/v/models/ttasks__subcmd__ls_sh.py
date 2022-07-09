"""Classe de template."""
from .factory import Factory
from .sh import Sh


class TTasks__subcmd__ls_sh(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)
        self.data_model = data_model
        self.tmpl.unicode = data_model['unicode']
        self.tmpl.cmd = data_model['cmd']
        self.tmpl.name = "%s/%s" %(self.tmpl.cmd['dir'], "tasks/subcmd/ls.sh".replace('template', self.tmpl.cmd['name']))
        #self.tmpl.log = data_model['log']

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
