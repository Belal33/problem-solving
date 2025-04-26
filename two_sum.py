# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
def two_sum(numbers, target):
    """Write a function that takes an array of numbers (integers for the tests) and a target number.
    It should find two different items in the array that, when added together,
    give the target value."""

    for i, el in enumerate(numbers):
        for j, e in enumerate(numbers):
            if e + el == target and i != j:
                return [i, j]


print(two_sum([1, 2, 3], 4))
