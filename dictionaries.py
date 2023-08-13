def dictionaries():
    print("DICTIONARIES")

    # unordered and mutable collection data type
    # key value pairs.
    mydict = {"name": "Leif", "age": 38, "city": "Albuquerque"}
    print("mydict:", mydict)
    # Don't have to use quotes for keys with dict() constructor
    # keys are auto-converted to strings.
    mydict2 = dict(name="Mary", age="27", city="Boston")
    print("mydict2:", mydict2)

    value = mydict["name"]
    # value = mydict["poo"]  # KeyError: 'poo'
    print(value)

    # You can add or change items after creation (mutable)
    mydict["email"] = "max@xyz.com"
    print(mydict)
    # setting a value again overwrites it.
    mydict["email"] = "leif@xyz.com"
    print(mydict)

    # use 'del' keyword to remove elements or 'pop' or 'popitem'
    del mydict["name"]
    print(mydict)

    mydict.pop("age")
    print(mydict)
    mydict["name"] = "bob"
    mydict["age"] = "42"
    print(mydict)

    mydict.popitem()  # after python 3.7 removes last inserted item
    print(mydict)

    # check if key is in dictionary using if x in y
    if "name" in mydict:
        print(mydict["name"])

    # try catch, basically.
    try:
        print(mydict["name"])
    except:
        print("Error")

    # looping through a dictionary
    for key in mydict:
        print(key)

    for key in mydict.keys():
        print(key)

    for value in mydict.values():
        print(value)

    for key, value in mydict.items():
        print(key, ":", value)

    # copying with dictionaries.
    mydict_cpy = mydict
    print(mydict_cpy)

    mydict_cpy["email"] = "max@xyz.com"
    print(mydict, mydict_cpy)  # both dictionaries have the same key value pair.

    # use built-in function to make an actual copy or the dict() constructor
    mydict_cpy = mydict.copy()
    mydict_cpy = dict(mydict)

    # merge two dictionaries with update method
    my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
    my_dict2 = dict(name="Mary", age=27, city="boston")
    my_dict.update(my_dict2)
    print(my_dict)
    # notice collisions are overwritten by the argument to update. everything else gets merged
    # non-collisions are not lost.

    my_dict = {3: 9, 6: 36, 8: 81}
    print(my_dict)
    # You can index the keys
    # Be careful not to try array indices my_dict[0] will throw an error
    # value = my_dict[0]  # KeyError: 0
    value = my_dict[3]
    print(value)

    # you can use tuples as keys
    mytuple = (8, 7)
    mydict = {mytuple: 15}
    print(mydict)

    # mylist = [8, 7]
    # mydict = {mylist: 15}  # TypeError: unhashable type: 'list'

    # Lists are mutable and can be changed after creation, so they are not hashable.
    # They are not hashable, so they cannot be used as a key.


if __name__ == "__main__":
    dictionaries()
