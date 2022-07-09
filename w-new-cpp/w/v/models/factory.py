# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from new_cpp.commmand.CMakeLists_txt import CMakeLists_txt
from new_cpp.commmand.dot_ccls import dot_ccls
from new_cpp.commmand.dot_gitignore import dot_gitignore
from new_cpp.commmand.dot_ccls___root import dot_ccls___root
from new_cpp.commmand.dot_local_vimrc import dot_local_vimrc
from new_cpp.commmand.dot_projections_json import dot_projections_json


template = {
    'new_cpp.commmand.CMakeLists_txt': CMakeLists_txt(),
    'new_cpp.commmand.dot_ccls': dot_ccls(),
    'new_cpp.commmand.dot_gitignore': dot_gitignore(),
    'new_cpp.commmand.dot_ccls___root': dot_ccls___root(),
    'new_cpp.commmand.dot_local_vimrc': dot_local_vimrc(),
    'new_cpp.commmand.dot_projections_json': dot_projections_json(),
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

