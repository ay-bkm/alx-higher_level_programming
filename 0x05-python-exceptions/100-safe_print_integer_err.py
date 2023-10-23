#!/usr/bin/python3
def safe_print_integer_err(value):[^1^][1]
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
