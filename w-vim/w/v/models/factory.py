# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from vimscript.commmand.autoload__amake_vim import autoload__amake_vim
from vimscript.commmand.README_md import README_md
from vimscript.commmand.LICENSE import LICENSE
from vimscript.commmand.plugin__amake_vim import plugin__amake_vim


template = {
    'vimscript.commmand.autoload__amake_vim': autoload__amake_vim(),
    'vimscript.commmand.README_md': README_md(),
    'vimscript.commmand.LICENSE': LICENSE(),
    'vimscript.commmand.plugin__amake_vim': plugin__amake_vim(),
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

