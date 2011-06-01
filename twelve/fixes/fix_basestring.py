"""

Fixer that changes all instances of 'basestring' as an object, class, function etc.
to the Six library's string_types.

"""

import re
from lib2to3.pgen2 import token
from lib2to3 import fixer_base

class FixBasestring(fixer_base.BaseFix):

    _accept_type = token.NAME
    
    def match(self, node):
        if node.value == 'basestring':
            return True
        return False
    
    def transform(self, node, results):
        node.value = 'six.string_types'
        node.changed()