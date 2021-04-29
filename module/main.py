# absolute import
import functions

# relative import
# from functions import add

# relative import with dot syntax, requires __init__.py file
from . import functions

x = 5
y = 6

z = functions.add(x, y)
print("5 + 6 =", z)

z = functions.sub(x, y)
print(z)