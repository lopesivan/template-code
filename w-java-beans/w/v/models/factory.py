# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from java.beans.kiko_cpp import kiko_cpp
from java.beans.kuku import kuku
from java.beans.ddd__kiko_cpp import ddd__kiko_cpp
from java.beans.aa__bb__cc__juca_txt import aa__bb__cc__juca_txt
from java.beans.beans_java import beans_java


template = {
    'java.beans.kiko_cpp': kiko_cpp(),
    'java.beans.kuku': kuku(),
    'java.beans.ddd__kiko_cpp': ddd__kiko_cpp(),
    'java.beans.aa__bb__cc__juca_txt': aa__bb__cc__juca_txt(),
    'java.beans.beans_java': beans_java(),
}

class Factory(object):
    """Metodo fabrica."""
    __metaclass__ = ABCMeta

    def __init__(self, template_name):
        self.tmpl = template[template_name]

    @abstractmethod
    def put(self):
        """Imprime mensagem na tela."""
        pass

    @abstractmethod
    def save(self):
        """Salva em arquivo."""
        pass

