# A set is a collection datatype that is unordered and mutable.
# Unlike lists or tuples, it does not allow duplicate elements.

# Can't use sets as keys in dicts because of mutability of sets.
# mh = {my_set: 1}  # TypeError: unhashable type: 'set'


def sets():
    print("SETS")
    # Created with braces like a dictionary, but just single elements separated by commas.
    my_set = {1, 2, 3, 1, 2}
    print(my_set)

    # Can use an iterable, or a string to create a set.
    my_set = set([1, 2, 3])
    print(my_set)
    # order is arbitrary because a set is unordered
    my_set = set("Hello")
    print(my_set)

    # Can't create an empty set with just braces, it creates a dictionary instead.
    # Instead, you have to use the set method
    my_set = {}
    print(my_set)
    print(type(my_set))
    my_set = set()
    print(my_set)  # notice this prints out `set()`
    print(type(my_set))

    # can mutate sets with .add(), .remove()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    my_set.remove(3)
    print(my_set)
    # Can't remove an element that's not in the set
    # my_set.remove(4)  # KeyError: 4

    # Use `discard()` method to remove safely without an error
    my_set.discard(1)
    my_set.discard(4)
    print(my_set)

    # Use the `clear` method to empty the set
    my_set.clear()
    print(my_set)

    my_set = {1, 2, 3, 4, 5}

    # pop to return the first value of the set and remove it
    print(my_set)
    my_set.pop()
    popped_element = my_set.pop()
    print("popped:", popped_element)
    print(my_set)

    # iterate over the set elements
    for i in my_set:
        print(i)

    # Check if a value is in a set. with if-in
    if 3 in my_set:
        print("yes")
    else:
        print("no")

    # Union, intersection, difference

    odds = {1, 3, 5, 7, 9}
    evens = {0, 2, 4, 6, 8}
    prime = {2, 3, 5, 7}

    u = odds.union(evens)  # union combines two sets
    print(u)

    # intersection keeps elements that exist in both sets
    i = odds.intersection(evens)
    print(i)
    i = odds.intersection(prime)
    print(i)
    i = evens.intersection(prime)
    print(i)

    # Difference only gives you the first set elements only that are not in the second set.
    set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set_b = {1, 2, 3, 10, 11, 12}
    d = set_a.difference(set_b)
    print(d)

    # Symmetric difference gives you the difference from both lists.


if __name__ == "__main__":
    sets()
