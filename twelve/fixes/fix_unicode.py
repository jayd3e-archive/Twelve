"""

Fixer that changes all instances of 'unicode' as an object, class, function etc.
to the Six library's text_type.

"""

from lib2to3.pgen2 import token
from lib2to3 import fixer_base

class FixUnicode(fixer_base.BaseFix):

    _accept_type = token.NAME
    
    def match(self, node):
        if node.value == 'unicode':
            return True
        return False
    
    def transform(self, node, results):
        node.value = 'six.text_type'
        node.changed()