import sys
import os

is_dev = sys.argv[1] == "dev" if len(sys.args) > 1 else False

if sys.version_info >= (3, 7):
    requirements = "requirements.txt"
elif(2, 6) <= sys.version_info < (3, 0):
    if is_dev:
        requirements = "py2-requirements.txt"
    else:
        requirements = "requirements.txt"
else:
    raise AssertionError("only support 2.6, 2.7, 3.7")


