# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from ip.network.cable import cable
from ip.network.wifi import wifi
from ip.network.hosts import hosts
from ip.network.interfaces import interfaces


template = {
    'ip.network.cable': cable(),
    'ip.network.wifi': wifi(),
    'ip.network.hosts': hosts(),
    'ip.network.interfaces': interfaces(),
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

