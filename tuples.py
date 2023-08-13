def tuples():
    print("TUPLES")
    # collection ordered and immutable

    mytuple = ("Leif", 38, "Boston")
    # or
    mytuple = "Leif", 38, "Boston"
    # for a single value you need a comma for a tuple
    mytuple2 = ("Leif",)
    print("mytuple:", mytuple)
    print("mytuple2:", mytuple2)

    # tuple function to create from an iterable.
    mytuple = tuple(["Leif", 38, "Boston"])
    print(mytuple)

    # accessing items
    item = mytuple[0]
    print(item)
    # item = mytuple[3]  # IndexError: tuple index out of range
    item = mytuple[-2]
    print(item)
    # mytuple[0] = "Bob"  # TypeError: 'tuple' object does not support item assignment
    for x in mytuple:
        print(x)

    # check if something is inside of the tuple.
    if "Leif" in mytuple:
        print("yes")
    else:
        print("no")

    mytuple = ("a", "b", "c", "d", "e", "d")
    print(len(mytuple))  # 6
    print(mytuple.count("d"))
    print(mytuple.count("x"))
    print(mytuple.index("d"))  # returns index of first occurrence
    # print(mytuple.index("z"))  # ValueError: tuple.index(x): x not in tuple

    # convert back and forth between list and tuple.
    my_list = list(mytuple)
    mytuple2 = list(my_list)
    print(my_list)
    print(mytuple2)

    # slicing : access sub-parts of the tuple
    a = (1, 2, 3, 4, 5, 6)
    print(a)
    b = a[2:5]
    b = a[:5]
    b = a[3:]
    b = a[::-1]
    print(b)

    # unpacking tuples:
    my_tuple = ("Leif", 38, "Albuquerque")
    # number of elements must match number of fields you're setting
    name, age, city = my_tuple
    print(name, age, city)
    # if they don't match:
    # name, age = my_tuple  # ValueError: too many values to unpack (expected 2)

    my_tuple = (0, 1, 2, 3, 4)
    # SyntaxError: multiple starred expressions in assignment
    # actually doesn't work:
    # i1, *i2, *i3 = my_tuple
    # a single star will greedily assign values into an array
    i1, *i2, i3 = my_tuple

    print(i1)
    print(i2)
    print(i3)

    # comparing tuples and lists.
    # tuples can be more efficient than lists especially when working with large data

    import sys

    my_list = [0, 1, 2, "hello", True]
    my_tuple = (0, 1, 2, "hello", True)
    print(sys.getsizeof(my_list), "bytes")  # 104 bytes
    print(sys.getsizeof(my_tuple), "bytes")  # 80 bytes

    import timeit

    # iteration and creation are more efficient with tuples
    print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))  # 0.033294709006440826
    print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  # 0.0056836670119082555


if __name__ == "__main__":
    tuples()
