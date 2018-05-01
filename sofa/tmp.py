import os
import sys

import pandas as pd

from past.utils import old_div as od


def get_type(o):
    t = [type(o)]
    if isinstance(o, (pd.Series)):
        t += [o.dtype]
    return t


def old_div(a, b):
    f = sys._getframe(1)
    fn = os.path.basename(f.f_code.co_filename)
    print(fn, f.f_lineno, get_type(a), get_type(b), file=sys.stderr)
    return od(a, b)
