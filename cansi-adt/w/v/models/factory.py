# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from cansi.adt.typedefStruct_h import typedefStruct_h
from cansi.adt.Customer_h import Customer_h
from cansi.adt.Customer_c import Customer_c


template = {
    'cansi.adt.typedefStruct_h': typedefStruct_h(),
    'cansi.adt.Customer_h': Customer_h(),
    'cansi.adt.Customer_c': Customer_c(),
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

    @abstractmethod
    def status(self):
        """Lista arquivos que serão gerados."""
        pass

