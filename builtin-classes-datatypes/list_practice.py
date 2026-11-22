# List is ordered, nonunique , indexed, mutable, nonhashed, has lookup of O(n)
# List, Tuple and Range belong are called sequences in Python because they are ordered
def main():
    list_num = [1, 2, 5, 33, 2.5, 6]
    list_fruits = [
        "Apple",
        "Orange",
        "Banana",
        "Pineapple",
        "Orange",
        "Grapes",
        "Kiwi",
        "pineapple",
        "Coconut",
        "Apple",
    ]
    # we will build log as 2D array/List
    list_log = []
    print(list_num)
    print(list_fruits)

    # sorting by generating new list
    print()
    print("Out of line sorting by SORTED:")
    print(sorted(list_num))
    print(sorted(list_num, reverse=True))
    print(sorted(list_fruits))
    print(sorted(list_fruits, reverse=True))

    # List length or count
    print()
    print("Inline Counting: ")
    print(list_num.count(5))
    print(list_fruits.count("Apple"))

    # print all methods belonging to list
    print(dir(list))

    # print method help or docstring
    print(help(list.append))
    # append - appends 1 item at a time
    for i in range(10):
        print(i)
        list_log.append([f"user{i}", i])

    print(list_log)

    # print each item in the list 1 by 1 - common pattern in hackerrank
    for item in list_log:
        for i in item:
            print(i)

    # extend - allows multiple values to be inserted
    list_log.extend([["user10", 10], ["user11", 11]])

    print(list_log)

    # same list can have multiple datatypes lets try inserting dictionary
    list_log.append({"name": "Adnan", "value": 1})

    print(list_log)

    # in place reverse
    list_log.reverse()
    for item in list_log:
        for i in item:
            print(i)

    # out of place reverse
    print(list(reversed(list_log)))

    # clear list
    list_log.clear()

    # insert into list
    print(list_log)
    for i in range(10):
        list_log.insert(i, [f"user{i}", i])
    print(list_log)

    # remove and reinsert
    list_log.remove(["user0", 0])
    print(list_log)
    list_log.insert(0, ["user0", 0])
    print(list_log)

    # indexn searches for value within slice if slice given otherwise whole list
    # If value not found it will throw value error
    print(list_log.index(["user5", 5], 0, 6))
    print(list_log.index(["user7", 7]))

    # This below statement will throw ValueError if we ran this
    # print(list_log.index(["user5", 5], 0, 4))
    # pop


if __name__ == "__main__":
    main()
