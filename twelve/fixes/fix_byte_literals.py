"""

Fixer that changes all instances of b''(byte literals) to the Six library's 
b() function.

"""

import re
from lib2to3.pgen2 import token
from lib2to3 import fixer_base

_literal_re = re.compile(r"[bB][\'\"]")

class FixByteLiterals(fixer_base.BaseFix):

    _accept_type = token.STRING
    
    def match(self, node):
        if _literal_re.match(node.value):
            return True
        return False
    
    def transform(self, node, results):
        node.value = node.value[1:]
        node.value = 'six.b(' + node.value + ')'
        node.changed()