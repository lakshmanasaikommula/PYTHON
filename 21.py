#import module_name
"""math  module provides us to access some common math functions"""

import math
print(math.factorial(4))
print(math.pi)

import math as m1
print(m1.factorial(5))

from math import factorial
print(factorial(6))

from math import factorial as fact
print(fact(7))

import random
random_integer = random.randint(1, 100)
print(random_integer)


import random
random_ele = random.choice(["A","B","C",'d','sqdqd','1223','hh6t','ggf'])
print(random_ele)