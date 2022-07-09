# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from shellscript.commmand.template import template
from shellscript.commmand.tests__file_test_sh import tests__file_test_sh
from shellscript.commmand.template_bash import template_bash
from shellscript.commmand.tasks__usage_sh import tasks__usage_sh
from shellscript.commmand.modules__exception_sh import modules__exception_sh
from shellscript.commmand.modules__config_sh import modules__config_sh
from shellscript.commmand.tests__tasks__git_test_sh import tests__tasks__git_test_sh
from shellscript.commmand.etc__rules__run_mk import etc__rules__run_mk
from shellscript.commmand.etc__rules__build_mk import etc__rules__build_mk
from shellscript.commmand.tasks__completions_sh import tasks__completions_sh
from shellscript.commmand.modules__options_sh import modules__options_sh
from shellscript.commmand.tasks__commands_sh import tasks__commands_sh
from shellscript.commmand.localexecutable import localexecutable
from shellscript.commmand.tasks__subcmd__ls_sh import tasks__subcmd__ls_sh
from shellscript.commmand.tasks__java_sh import tasks__java_sh
from shellscript.commmand.tests__tasks__completions_test_sh import tests__tasks__completions_test_sh
from shellscript.commmand.tasks__subcmd__beans_sh import tasks__subcmd__beans_sh
from shellscript.commmand.etc__rules__tests_mk import etc__rules__tests_mk
from shellscript.commmand.tests__tasks__default_test_sh import tests__tasks__default_test_sh
from shellscript.commmand.HOWTOCLONE import HOWTOCLONE
from shellscript.commmand.etc__templatedoc_json import etc__templatedoc_json
from shellscript.commmand.tasks__init_sh import tasks__init_sh
from shellscript.commmand.etc__completion_bash import etc__completion_bash
from shellscript.commmand.tests__tasks__commands_test_sh import tests__tasks__commands_test_sh
from shellscript.commmand.Makefile import Makefile
from shellscript.commmand.dot_projections_json import dot_projections_json
from shellscript.commmand.tasks__default_sh import tasks__default_sh
from shellscript.commmand.modules__exit_sh import modules__exit_sh


template = {
    'shellscript.commmand.template': template(),
    'shellscript.commmand.tests__file_test_sh': tests__file_test_sh(),
    'shellscript.commmand.template_bash': template_bash(),
    'shellscript.commmand.tasks__usage_sh': tasks__usage_sh(),
    'shellscript.commmand.modules__exception_sh': modules__exception_sh(),
    'shellscript.commmand.modules__config_sh': modules__config_sh(),
    'shellscript.commmand.tests__tasks__git_test_sh': tests__tasks__git_test_sh(),
    'shellscript.commmand.etc__rules__run_mk': etc__rules__run_mk(),
    'shellscript.commmand.etc__rules__build_mk': etc__rules__build_mk(),
    'shellscript.commmand.tasks__completions_sh': tasks__completions_sh(),
    'shellscript.commmand.modules__options_sh': modules__options_sh(),
    'shellscript.commmand.tasks__commands_sh': tasks__commands_sh(),
    'shellscript.commmand.localexecutable': localexecutable(),
    'shellscript.commmand.tasks__subcmd__ls_sh': tasks__subcmd__ls_sh(),
    'shellscript.commmand.tasks__java_sh': tasks__java_sh(),
    'shellscript.commmand.tests__tasks__completions_test_sh': tests__tasks__completions_test_sh(),
    'shellscript.commmand.tasks__subcmd__beans_sh': tasks__subcmd__beans_sh(),
    'shellscript.commmand.etc__rules__tests_mk': etc__rules__tests_mk(),
    'shellscript.commmand.tests__tasks__default_test_sh': tests__tasks__default_test_sh(),
    'shellscript.commmand.HOWTOCLONE': HOWTOCLONE(),
    'shellscript.commmand.etc__templatedoc_json': etc__templatedoc_json(),
    'shellscript.commmand.tasks__init_sh': tasks__init_sh(),
    'shellscript.commmand.etc__completion_bash': etc__completion_bash(),
    'shellscript.commmand.tests__tasks__commands_test_sh': tests__tasks__commands_test_sh(),
    'shellscript.commmand.Makefile': Makefile(),
    'shellscript.commmand.dot_projections_json': dot_projections_json(),
    'shellscript.commmand.tasks__default_sh': tasks__default_sh(),
    'shellscript.commmand.modules__exit_sh': modules__exit_sh(),
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

