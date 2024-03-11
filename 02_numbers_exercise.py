# 1. Creating formulas
# Write the following mathematical formula in Python:

a = 2
b = 3
c = 2

# Your formula here:
result = (6 * (a ** 3)) -  ((8 * (b ** 2))/(4 * c)) + 11

assert result == 50

# 2. Floating point pitfalls
# Show that 0.1 + 0.2 == 0.3
from decimal import Decimal, getcontext

# Your solution here
print(float(0.1) + float(0.2))

# This won't work:
assert 0.1 + 0.2 == 0.3
