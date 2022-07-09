# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from cansi.state.State_c import State_c
from cansi.state.StartedState_h import StartedState_h
from cansi.state.StateState_c import StateState_c
from cansi.state.StateInternal_h import StateInternal_h
from cansi.state.State_h import State_h
from cansi.state.message_h import message_h
from cansi.state.StoppedState_c import StoppedState_c
from cansi.state.main_c import main_c
from cansi.state.Context_c import Context_c
from cansi.state.Context_h import Context_h
from cansi.state.StartedState_c import StartedState_c
from cansi.state.message_c import message_c
from cansi.state.StoppedState_h import StoppedState_h
from cansi.state.StateState_h import StateState_h


template = {
    'cansi.state.State_c': State_c(),
    'cansi.state.StartedState_h': StartedState_h(),
    'cansi.state.StateState_c': StateState_c(),
    'cansi.state.StateInternal_h': StateInternal_h(),
    'cansi.state.State_h': State_h(),
    'cansi.state.message_h': message_h(),
    'cansi.state.StoppedState_c': StoppedState_c(),
    'cansi.state.main_c': main_c(),
    'cansi.state.Context_c': Context_c(),
    'cansi.state.Context_h': Context_h(),
    'cansi.state.StartedState_c': StartedState_c(),
    'cansi.state.message_c': message_c(),
    'cansi.state.StoppedState_h': StoppedState_h(),
    'cansi.state.StateState_h': StateState_h(),
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

