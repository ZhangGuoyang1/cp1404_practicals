"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

What did you see on line 1?
print(random.randint(5, 20))
an integer
What was the smallest number you could have seen, what was the largest?
Smallest: 5. Largest: 20.

What did you see on line 2?
print(random.randrange(3, 10, 2))
an integer from {3, 5, 7, 9}
What was the smallest number you could have seen, what was the largest?
Smallest: 3. Largest: 9.
Could line 2 have produced a 4?
NO.

What did you see on line 3?
print(random.uniform(2.5, 5.5))
a floating-point number.
What was the smallest number you could have seen, what was the largest?
Smallest possible: 2.5 .
Largest possible: 5.5 .

Write code, not a comment, to produce a random number between 1 and 100 inclusive.

"""

import random

print(random.randint(1,100))



