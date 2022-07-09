# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from new_file.commmand.helloworld_java import helloworld_java
from new_file.commmand.tictac_c import tictac_c
from new_file.commmand.helloworld_rs import helloworld_rs
from new_file.commmand.helloworld_py import helloworld_py
from new_file.commmand.helloworld_cpp import helloworld_cpp
from new_file.commmand.helloworld_c import helloworld_c
from new_file.commmand.tictac_cpp import tictac_cpp
from new_file.commmand.helloworld_tex import helloworld_tex


template = {
    'new_file.commmand.helloworld_java': helloworld_java(),
    'new_file.commmand.tictac_c': tictac_c(),
    'new_file.commmand.helloworld_rs': helloworld_rs(),
    'new_file.commmand.helloworld_py': helloworld_py(),
    'new_file.commmand.helloworld_cpp': helloworld_cpp(),
    'new_file.commmand.helloworld_c': helloworld_c(),
    'new_file.commmand.tictac_cpp': tictac_cpp(),
    'new_file.commmand.helloworld_tex': helloworld_tex(),
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

