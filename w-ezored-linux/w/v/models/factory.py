# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from ezored.linux_app.projects__others__ezored__src__maindot_cpp import projects__others__ezored__src__maindot_cpp
from ezored.linux_app.files__modules__target___linux__cmake__moduledot_cmake import files__modules__target___linux__cmake__moduledot_cmake
from ezored.linux_app.files__config__target_linuxdot_py import files__config__target_linuxdot_py
from ezored.linux_app.files__targets__linux__verbs__preparedot_py import files__targets__linux__verbs__preparedot_py
from ezored.linux_app.files__targets__linux__verbs__packagedot_py import files__targets__linux__verbs__packagedot_py
from ezored.linux_app.files__targets__linux__verbs__distdot_py import files__targets__linux__verbs__distdot_py
from ezored.linux_app.files__targets__linux__verbs__builddot_py import files__targets__linux__verbs__builddot_py
from ezored.linux_app.files__targets__linux__conan__recipe__conanfiledot_py import files__targets__linux__conan__recipe__conanfiledot_py
from ezored.linux_app.files__targets__linux__conan__profile__ezored_linux_profile import files__targets__linux__conan__profile__ezored_linux_profile
from ezored.linux_app.files__targets__linux__cmake__CMakeListsdot_txt import files__targets__linux__cmake__CMakeListsdot_txt


template = {
    'ezored.linux_app.projects__others__ezored__src__maindot_cpp': projects__others__ezored__src__maindot_cpp(),
    'ezored.linux_app.files__modules__target___linux__cmake__moduledot_cmake': files__modules__target___linux__cmake__moduledot_cmake(),
    'ezored.linux_app.files__config__target_linuxdot_py': files__config__target_linuxdot_py(),
    'ezored.linux_app.files__targets__linux__verbs__preparedot_py': files__targets__linux__verbs__preparedot_py(),
    'ezored.linux_app.files__targets__linux__verbs__packagedot_py': files__targets__linux__verbs__packagedot_py(),
    'ezored.linux_app.files__targets__linux__verbs__distdot_py': files__targets__linux__verbs__distdot_py(),
    'ezored.linux_app.files__targets__linux__verbs__builddot_py': files__targets__linux__verbs__builddot_py(),
    'ezored.linux_app.files__targets__linux__conan__recipe__conanfiledot_py': files__targets__linux__conan__recipe__conanfiledot_py(),
    'ezored.linux_app.files__targets__linux__conan__profile__ezored_linux_profile': files__targets__linux__conan__profile__ezored_linux_profile(),
    'ezored.linux_app.files__targets__linux__cmake__CMakeListsdot_txt': files__targets__linux__cmake__CMakeListsdot_txt(),
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

