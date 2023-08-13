# covered:
# creating lists,
# list(),
# things you can add to a list,
# indexing lists
# looping through lists with the 'in' keyword
# determining if elements are in lists with 'if x in y'
#
def lists():
    # ordered, mutable, allows duplicate elements.
    list_example = ["1", "b", "3"]
    print(list_example)
    mylist2 = list()
    print(mylist2)
    mylist3 = [True, 2, "3", 2]
    print(mylist3)

    mylist = ["banana", "cherry", "apple"]
    item = mylist[0]  # list index out of range error if not a valid index.
    item = mylist[-1]  # negative number indices start from the end of the list

    for i in mylist:
        print(i)

    if "banana" in mylist:
        print("yes")
    else:
        print("no")

    print(len(mylist))

    mylist.append("lemon")
    print(mylist)

    mylist.insert(1, "blueberry")
    print(mylist)
    item = mylist.pop()
    print(item, mylist)
    mylist.remove("cherry")
    print(mylist)
    mylist.append("blueberry")
    print(mylist)
    mylist.remove("blueberry")  # removes first occurrence
    print(mylist)
    # mylist.remove("notInList")  # ValueError: list.remove(x): x not in list
    mylist.reverse()
    print(mylist)
    mylist.clear()  # remove all elements
    print(mylist)

    mylist = [1, 5, 3, 0, -1, 10, -7, -4]
    # mylist.sort()  # mutates the list
    print(mylist)
    new_list = sorted(mylist)  # does not mutate the list
    print(new_list)

    mylist = [0] * 5  # create a new list with 5 0's
    another_list = [1, 2, 3, 4, 5]
    another_list2 = mylist + another_list
    print(another_list2)

    # slicing
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = mylist[1:5]
    print(a)
    a = mylist[:5]
    print(a)
    a = mylist[5:]
    print(a)

    # specify the step amount
    a = mylist[::2]  # beginning to end with step 2
    print(a)
    a = mylist[::-2]  # reverse the list with step 2
    print(a)

    # copying
    list_org = ["banana", "cherry", "apple"]
    list_cpy = list_org
    list_cpy.append("lemon")
    print(
        list_cpy
    )  # copy of the reference to org_list, so you modify both if you modify one.
    print(list_org)
    list_clone = (
        list_org.copy()
    )  # an actual copy of the original list, not a reference.
    list_clone.append("orange")
    print(list_clone, list_org)
    another_clone = list(list_org)
    another_clone2 = list_org[:]

    # list comprehensions
    a = [1, 2, 3, 4, 5, 6]
    b = [i * i for i in a]  # square each element.
    print(b)


if __name__ == "__main__":
    lists()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
