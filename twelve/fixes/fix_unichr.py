"""

Fixer that changes all instances of 'unichr' as an object, class, function etc.
to the chr type.

"""

from lib2to3.pgen2 import token
from lib2to3 import fixer_base

class FixUnichr(fixer_base.BaseFix):

    _accept_type = token.NAME
    
    def match(self, node):
        if node.value == 'unichr':
            return True
        return False
    
    def transform(self, node, results):
        node.value = 'chr'
        node.changed()