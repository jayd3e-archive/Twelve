"""

Fixer that changes all instances of u''(unicode literals) to the Six library's 
u() function.

"""

import re
from lib2to3.pgen2 import token
from lib2to3 import fixer_base

_literal_re = re.compile(r"[uU][rR]?[\'\"]")

class FixUnicodeLiterals(fixer_base.BaseFix):

    _accept_type = token.STRING
    
    def match(self, node):
        if _literal_re.match(node.value):
            return True
        return False
    
    def transform(self, node, results):
        node.value = node.value[1:]
        node.value = 'u(' + node.value + ')'
        node.changed()