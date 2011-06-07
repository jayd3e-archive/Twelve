"""
Fixer for 'raise E, V, T'

raise         -> six.reraise()
raise E       -> six.reraise(E)
raise E, V    -> six.reraise(E, V)
raise E, V, T -> six.reraise(E, V, T)

"""

# Local imports
from lib2to3 import pytree
from lib2to3.pgen2 import token
from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, String

class FixRaise(fixer_base.BaseFix):

    PATTERN = """
    raise_stmt< 'raise' exc=any [',' val=any [',' tb=any]] >
    """

    def transform(self, node, results):
        exc = results['exc'].clone() if 'exc' in results else None
        val = results['val'].clone() if 'val' in results else None
        tb = results['tb'].clone() if 'tb' in results else None

        exc.prefix = ''
        
        #Change Error() to Error, if there are no arguments to pass in.
        try:
            if len(exc.children[1].children) == 2:
                exc = String(exc.children[0])
        except IndexError:
            pass
            
        args = [exc]
        if val is not None:
            args.append(String(", "))
            args.append(val)
            
            if tb is not None:
                args.append(String(", "))
                args.append(tb)
        
        raise_stmt = Call(Name("six.reraise"), args)
        raise_stmt.prefix = node.prefix
        return raise_stmt


            
