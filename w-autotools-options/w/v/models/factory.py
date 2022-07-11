# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from configure_ac.new_opts.options_boolean import options_boolean


template = {
    'configure_ac.new_opts.options_boolean': options_boolean(),
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

