source ~/peda/peda.py

define pid
        python
import sys
sys.path.append("/home/blankwall/Template")
from gdb_help import *
pid("exploit2")
            