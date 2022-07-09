# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from cansi.adt.ADT_c import ADT_c
from cansi.adt.ADT_h import ADT_h
from cansi.adt.Class1_h import Class1_h
from cansi.adt.MemoryPool_ADT_c import MemoryPool_ADT_c


template = {
    'cansi.adt.ADT_c': ADT_c(),
    'cansi.adt.ADT_h': ADT_h(),
    'cansi.adt.Class1_h': Class1_h(),
    'cansi.adt.MemoryPool_ADT_c': MemoryPool_ADT_c(),
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

