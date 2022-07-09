    def save(self):
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))
