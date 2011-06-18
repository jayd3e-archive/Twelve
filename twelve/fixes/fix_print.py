"""Fixer for print.

Change:
    'print'          into 'print_()'
"""

from lib2to3 import fixer_base
from lib2to3.fixer_util import Name, Call, Comma, String, is_tuple

class FixPrint(fixer_base.BaseFix):   
    PATTERN = """
              print_stmt< 'print' string=any >
              """

    def transform(self, node, results):
        print_stmt = results['string']
        print_stmt.prefix = ''
        
        raise_stmt = Call(Name("six.print_"), 
                          [String(print_stmt)])
        raise_stmt.prefix = node.prefix
        print(raise_stmt)
        return raise_stmt
