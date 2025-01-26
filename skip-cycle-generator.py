"""
Design an Iterator Class/Function that cycles through a list with the following requirements:

The function should take two parameters:

A list of integers
A step size (defaulting to 1)


Each time the iterator is called, it should return three values:

The current index (starting from 0 and incrementing by 1)
The current cycle number (starting from 1, incrementing when we've traversed the entire list)
The current value from the list


The step parameter determines how many positions we move forward in the list each time:

If step=1, we move through the list sequentially
If step=2, we skip every other element
The iterator should cycle back to the beginning when reaching the end of the list



Example usage with numbers=[1,2,3] and step=2:
CopyFirst call:  returns (0, 1, 1)  // index=0, first cycle, value at position 0
Second call: returns (1, 1, 3)  // index=1, first cycle, value at position 2
Third call:  returns (2, 2, 2)  // index=2, second cycle, value at position 1
Fourth call: returns (3, 3, 1)  // index=3, third cycle, value at position 0
Follow-up: How would you implement this using Python generators?

This question tests several important concepts:

Iterator/Generator implementation
Modular arithmetic
Cycle detection
Understanding of Python's yield keyword
Edge case handling
"""

# Solution:

def skip_cycle(numbers, step=1):
    count = 0
    while True:
        position = (count * step) % len(numbers)
        # Calculate which cycle we're in by counting how many times we've gone through the list
        current_cycle = (count * step) // len(numbers) + 1
        yield count, current_cycle, numbers[position]
        count += 1

# Usage:
cycle = skip_cycle([1, 2, 3], 2).__next__

for _ in range(30):
    index, cycle_num, value = cycle()
    print(index, cycle_num, value)


# Explanation:
# For position = (count * step) % len(numbers):

# First, think about what we're trying to do: we want to move through a list in steps, and wrap around when we reach the end
# Let's work through small examples:

# With list [1,2,3] and step=2:
# count=0: we want position 0 (0×2=0)
# count=1: we want position 2 (1×2=2)
# count=2: we want position 1 (2×2=4, but need to wrap to 1)


# This "wrapping" behavior is exactly what modulo (%) does!

# 0 % 3 = 0
# 2 % 3 = 2
# 4 % 3 = 1



# For current_cycle = (count * step) // len(numbers) + 1:

# Think about when a new cycle starts - it's when we've seen all numbers
# With step=2 and length=3:

# count=0: 0×2=0 positions moved, 0//3=0+1=1st cycle
# count=1: 1×2=2 positions moved, 2//3=0+1=1st cycle
# count=2: 2×2=4 positions moved, 4//3=1+1=2nd cycle
# count=3: 3×2=6 positions moved, 6//3=2+1=3rd cycle



# Similar LeetCode problems for practice:

# "Iterator for Combination" (LC 1286) - Similar iterator pattern
# "Design Circular Queue" (LC 622) - Deals with circular wrapping using modulo
# "Peeking Iterator" (LC 284) - Practice with iterator design
# "Flatten 2D Vector" (LC 251) - Iterator implementation
# "Zigzag Iterator" (LC 281) - Custom iterator with patterns
# "Design Circular Deque" (LC 641) - More practice with circular data structures

# Interview tips for similar questions:

# Start with simple examples and write out the sequence
# Look for patterns in how numbers wrap around
# Remember modulo (%) for wrapping/cycling behavior
# Think about integer division (//) for counting complete cycles
# Test your solution with small examples first


# Class-based approach:

class SkipCycle:
    def __init__(self, numbers, step=1):
        self.numbers = numbers
        self.step = step
        self.count = 0
    
    def next(self):
        position = (self.count * self.step) % len(self.numbers)
        current_cycle = (self.count * self.step) // len(self.numbers) + 1
        value = self.numbers[position]
        
        result = (self.count, current_cycle, value)
        self.count += 1
        return result

# Usage:
iterator = SkipCycle([1, 2, 3], 2)
print(iterator.next())  # (0, 1, 1)
print(iterator.next())  # (1, 1, 3)
print(iterator.next())  # (2, 2, 2)


# Closure-based approach:

def create_skip_cycle(numbers, step=1):
    state = {'count': 0}
    
    def next_value():
        position = (state['count'] * step) % len(numbers)
        current_cycle = (state['count'] * step) // len(numbers) + 1
        value = numbers[position]
        
        result = (state['count'], current_cycle, value)
        state['count'] += 1
        return result
    
    return next_value

# Usage:
iterator = create_skip_cycle([1, 2, 3], 2)
print(iterator())  # (0, 1, 1)
print(iterator())  # (1, 1, 3)
print(iterator())  # (2, 2, 2)

"""
The main differences from the generator approach are:

We need to explicitly maintain state (count) using either class attributes or closure variables
Instead of using yield, we return values directly
For the class approach, we use a next() method
For the closure approach, we return a function that can be called repeatedly

Both approaches are functionally equivalent to the generator version. The class-based approach might be more familiar to people coming from other programming languages, while the closure approach is more functional in style.

"""
