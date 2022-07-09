# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from cansi.autotools.src__projectX__Makefile_am import src__projectX__Makefile_am
from cansi.autotools.m4__autotools_enable_debug_m4 import m4__autotools_enable_debug_m4
from cansi.autotools.src__projectX__alpha_c import src__projectX__alpha_c
from cansi.autotools.README_md import README_md
from cansi.autotools.common__args__args_h import common__args__args_h
from cansi.autotools.src__projectX__alpha_h import src__projectX__alpha_h
from cansi.autotools.src__projectX__beta_c import src__projectX__beta_c
from cansi.autotools.common__args__Makefile_am import common__args__Makefile_am
from cansi.autotools.Makefile_am import Makefile_am
from cansi.autotools.common__args__args_c import common__args__args_c
from cansi.autotools.autogen_sh import autogen_sh
from cansi.autotools.src__projectX__main_c import src__projectX__main_c
from cansi.autotools.dot_local_vimrc import dot_local_vimrc
from cansi.autotools.about_c import about_c
from cansi.autotools.m4__autotools_disable_gnu_args_m4 import m4__autotools_disable_gnu_args_m4
from cansi.autotools.configure_ac import configure_ac
from cansi.autotools.src__projectX__beta_h import src__projectX__beta_h
from cansi.autotools.dot_projections_json import dot_projections_json


template = {
    'cansi.autotools.src__projectX__Makefile_am': src__projectX__Makefile_am(),
    'cansi.autotools.m4__autotools_enable_debug_m4': m4__autotools_enable_debug_m4(),
    'cansi.autotools.src__projectX__alpha_c': src__projectX__alpha_c(),
    'cansi.autotools.README_md': README_md(),
    'cansi.autotools.common__args__args_h': common__args__args_h(),
    'cansi.autotools.src__projectX__alpha_h': src__projectX__alpha_h(),
    'cansi.autotools.src__projectX__beta_c': src__projectX__beta_c(),
    'cansi.autotools.common__args__Makefile_am': common__args__Makefile_am(),
    'cansi.autotools.Makefile_am': Makefile_am(),
    'cansi.autotools.common__args__args_c': common__args__args_c(),
    'cansi.autotools.autogen_sh': autogen_sh(),
    'cansi.autotools.src__projectX__main_c': src__projectX__main_c(),
    'cansi.autotools.dot_local_vimrc': dot_local_vimrc(),
    'cansi.autotools.about_c': about_c(),
    'cansi.autotools.m4__autotools_disable_gnu_args_m4': m4__autotools_disable_gnu_args_m4(),
    'cansi.autotools.configure_ac': configure_ac(),
    'cansi.autotools.src__projectX__beta_h': src__projectX__beta_h(),
    'cansi.autotools.dot_projections_json': dot_projections_json(),
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

