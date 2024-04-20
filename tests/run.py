import argparse
import sys
import unittest

def load_tests(loader, tests, pattern):
    return loader.discover('tests')

if __name__ == '__main__':
    sys.argv = [__file__] + (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    unittest.main(argv=sys.argv[0:1])