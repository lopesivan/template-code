# -*- coding: utf-8 -*-

'''
Os itens contidos em objetos da classe Lista podem ser acessados pelos
ordinais de 'primeiro' até 'decimo', ou por abreviaturas de três letras
destes ordinais:

>>> l = Lista([11, 22, 33, 44, 55])
>>> l.primeiro
11
>>> l.ter
33

'''

# A implementação ficou assim:

from itertools import count

class Lista(list):

    __ordinais = ('primeiro segundo terceiro quarto quinto sexto setimo'
                  ' oitavo nono decimo').split()
    __abrevs   = [s[:3] for s in __ordinais]

    def __getattr__(self, atrib):
        atr = atrib[:3]
        for i, ordinal, abrev in zip(count(), self.__ordinais, self.__abrevs):
            if atrib == ordinal or atr == abrev:
                return self[i]
            else:
                msg = "'%s' object has no attribute '%s'"
                raise AttributeError(msg % (self.__class__.__name__, atrib))

    @property
    def ultimo(self):
        return self[-1]

    ult = ultimo
