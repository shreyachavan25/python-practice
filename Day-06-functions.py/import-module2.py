"""Examples of importing math_utils."""

import math_utils

print(math_utils.add(2, 3))
print(math_utils.multiply(4, 5))

from math_utils import add, multiply

print(add(2, 3))
print(multiply(4, 5))

import math_utils as mu

print(mu.add(2, 3))