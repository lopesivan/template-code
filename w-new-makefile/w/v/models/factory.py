# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from new_makefile.commmand.vaca_mk import vaca_mk
from new_makefile.commmand.venv_mk import venv_mk
from new_makefile.commmand.c_mk import c_mk
from new_makefile.commmand.arduino_profile_mk import arduino_profile_mk
from new_makefile.commmand.so_mk import so_mk
from new_makefile.commmand.cpp11_mk import cpp11_mk
from new_makefile.commmand.s_mk import s_mk
from new_makefile.commmand.arduino_mk import arduino_mk
from new_makefile.commmand.java_mk import java_mk
from new_makefile.commmand.go_mk import go_mk
from new_makefile.commmand.py_mk import py_mk
from new_makefile.commmand.conditional_mk import conditional_mk
from new_makefile.commmand.modernc_mk import modernc_mk
from new_makefile.commmand.maven_mk import maven_mk
from new_makefile.commmand.m_mk import m_mk
from new_makefile.commmand.cpp_mk import cpp_mk


template = {
    'new_makefile.commmand.vaca_mk': vaca_mk(),
    'new_makefile.commmand.venv_mk': venv_mk(),
    'new_makefile.commmand.c_mk': c_mk(),
    'new_makefile.commmand.arduino_profile_mk': arduino_profile_mk(),
    'new_makefile.commmand.so_mk': so_mk(),
    'new_makefile.commmand.cpp11_mk': cpp11_mk(),
    'new_makefile.commmand.s_mk': s_mk(),
    'new_makefile.commmand.arduino_mk': arduino_mk(),
    'new_makefile.commmand.java_mk': java_mk(),
    'new_makefile.commmand.go_mk': go_mk(),
    'new_makefile.commmand.py_mk': py_mk(),
    'new_makefile.commmand.conditional_mk': conditional_mk(),
    'new_makefile.commmand.modernc_mk': modernc_mk(),
    'new_makefile.commmand.maven_mk': maven_mk(),
    'new_makefile.commmand.m_mk': m_mk(),
    'new_makefile.commmand.cpp_mk': cpp_mk(),
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

