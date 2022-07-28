# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from ezored.linux_app.linux__verbs__preparedot_py import linux__verbs__preparedot_py
from ezored.linux_app.linux__verbs__packagedot_py import linux__verbs__packagedot_py
from ezored.linux_app.linux__verbs__distdot_py import linux__verbs__distdot_py
from ezored.linux_app.linux__verbs__builddot_py import linux__verbs__builddot_py
from ezored.linux_app.linux__conan__recipe__conanfiledot_py import linux__conan__recipe__conanfiledot_py
from ezored.linux_app.linux__conan__profile__ezored_linux_profile import linux__conan__profile__ezored_linux_profile
from ezored.linux_app.linux__cmake__CMakeListsdot_txt import linux__cmake__CMakeListsdot_txt


template = {
    'ezored.linux_app.linux__verbs__preparedot_py': linux__verbs__preparedot_py(),
    'ezored.linux_app.linux__verbs__packagedot_py': linux__verbs__packagedot_py(),
    'ezored.linux_app.linux__verbs__distdot_py': linux__verbs__distdot_py(),
    'ezored.linux_app.linux__verbs__builddot_py': linux__verbs__builddot_py(),
    'ezored.linux_app.linux__conan__recipe__conanfiledot_py': linux__conan__recipe__conanfiledot_py(),
    'ezored.linux_app.linux__conan__profile__ezored_linux_profile': linux__conan__profile__ezored_linux_profile(),
    'ezored.linux_app.linux__cmake__CMakeListsdot_txt': linux__cmake__CMakeListsdot_txt(),
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

