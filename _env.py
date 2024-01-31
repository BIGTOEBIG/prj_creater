import sys
import os
lib_dir = os.path.realpath("Lib/site-packages")
assert os.path.exists(lib_dir)
if not lib_dir in sys.path:
    sys.path.insert(0, lib_dir)
    print(f"Adding {lib_dir} to sys.path")
