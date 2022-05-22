import mymodule
from mymodule import divide  # import sth specific from a file
import sys

print(divide(4, 2))
print(mymodule.divide(5, 2))

print(sys.path)  # list of paths ['C:\\sadas\\sadas\\sadsad\\ewfdef\\python_refresher\\21_imports_in_python', ...

print(sys.modules)  # {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, ...
