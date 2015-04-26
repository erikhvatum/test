# The MIT License (MIT)
#
# Copyright (c) 2014-2015 WUSTL ZPLAB
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Authors: Zach Pincus

import ctypes
import sys
import os.path
import glob

def load_test():
    if sys.platform == 'win32':
        loader = ctypes.windll
        functype = ctypes.WINFUNCTYPE
    else:
        loader = ctypes.cdll
        functype = ctypes.CFUNCTYPE

    test = None
    errors = []
    possible_test_libs = glob.glob(os.path.join(os.path.dirname(__file__), '_test.*'))
    for lib in possible_test_libs:
        try:
            test = loader.LoadLibrary(lib)
            break
        except Exception:
            # Get exception instance in Python 2.x/3.x compatible manner
            e_type, e_value, e_tb = sys.exc_info()
            del e_tb
            errors.append((lib, e_value))

    if test is None:
        if errors:
            # No test library loaded, and load-errors reported for some
            # candidate libs
            err_txt = ['%s:\n%s' % (l, str(e.args[0])) for l, e in errors]
            raise RuntimeError('One or more test libraries were found, but '
                               'could not be loaded due to the following errors:\n'
                               '\n\n'.join(err_txt))
        else:
            # No errors, because no potential libraries found at all!
            raise RuntimeError('Could not find test library.')

    return test

_test = load_test()

def test():
    return _test.test()
