"""

Fixer that changes all instances of 'basestring' as an object, class, function etc.
to the Six library's string_types.

"""

from lib2to3.pgen2 import token
from lib2to3 import fixer_base

class FixImportRfc822(fixer_base.BaseFix):

    _accept_type = token.NAME
    
    PATTERN = "import_from< 'from' from_name='rfc822' 'import' import_as_names< 'parsedate_tz' ',' 'mktime_tz' ',' 'formatdate' > >"

    
    def transform(self, node, results):
        node = results['from_name']
        node.value = 'email.utils'
        node.changed()