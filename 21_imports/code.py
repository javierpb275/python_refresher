from mymodule import divide
import mymodule
import sys

print(divide(4, 2))
print(mymodule.divide(5, 2))

print(sys.path)  # list of paths

print(sys.modules)  # {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, ...
