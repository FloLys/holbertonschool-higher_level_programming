#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as excp:
        print("Exception: {}".format(excp), file=sys.stderr)
        return None
