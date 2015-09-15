__author__ = 'Vicente'

from MetaClases import *


class Person (metaclass=RestrictedAccess):
    attributes = [" name ", " lastname ", " alias "]

p = Person(" Bruce ", " Wayne ", " Batman ")


print(p.name, p.lastname, "es", p.alias, "!")
## Bruce Wayne es Batman !

p.alias = " Robin "
## AttributeError : cant set attribute