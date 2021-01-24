"""
Iterator is an object with a state that knows how to fetch its next value.
Also iterators have the StopIteration exception that is thrown when there
are no more values in the iterator. This is called iterator exhaustion.

Iterables are any object that contain values that can be looped over.
Iterables have the __iter__ and __next__ methods availble. To check special
methods on any object use the special method __dir__ or dir(obj_name).
"""
# A very basic view of what iterables are and what iterators are

nums = [1, 2, 3]
# for num in nums:
#     print(num)
print(dir(nums)) # notice that nums doesnt have the __next__ special method.
print(iter(nums))
# Example using, build a mach range class to do the same
# operations as the built-in range.

class MyRange():
    def __init__(self, start, end):
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
nums = MyRange(1, 4)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums)) # Throws the exception StopIteration like we expect.

# Now using a generator, does the same thing as the above class 
# but isn't tied to the class objects. Generators work by grabbing 1 value at
# a time throughout the iteration. This can help with memory consumption for very large
# objects. Instead of reading in everything up front, data is broken apart and yielded piece by piece.

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1
        
nums = my_range(1, 4)

for num in nums:
    print(num)