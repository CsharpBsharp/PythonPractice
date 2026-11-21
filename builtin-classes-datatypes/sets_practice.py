# set is mutable, unordered, hashed, nonindex, unique means duplicates will be ignored silently and O(1) for lookup vs list O(n)
# set allows set operations like union, intersection, difference, symmetric_difference

"""
List vs. Set (Ordered Array vs. Hash Table)

Both are mutable and hold multiple items, but they use completely different underlying data structures.

Feature	list ([1, 2, 2])	set ({1, 2})
Ordering & Indexing	Ordered; supports indexing (my_list[0])	Unordered; no indexing (my_set[0] raises TypeError)
Duplicates	Allowed ([1, 2, 2] stays [1, 2, 2])	Automatically removed ({1, 2, 2} becomes {1, 2})
Element Requirement	Can hold any Python object	Elements must be hashable (immutable)
Lookup Speed (x in col)	Slow — O(n) (scans item by item)	Instant — O(1) (uses a hash table)
Special Operations	Concatenation (+), slicing ([1:3])	Math set operations: union (`
"""

# As said above sets are mutable, hashed by default so therefore unordered even when printing or inserting
# sets cannot be used with indexes unlike list
# They are not subclasses of each other they are ihereted from python absract base classes called collections.abc

# • list and set are both Mutable Collections (collections.abc.Collection). You can add or remove items after creation,
# iterate over them (Iterable), check their length (Sized), and check membership with in (Container).

# list and tuple are both Sequences (collections.abc.Sequence). They are ordered collections accessible by integer
# index (obj[0]). list is specifically a MutableSequence.


def main():
    seta = {10, 12, 14, 16, 18, 22, 20}
    setb = {10, 11, 12, 13, 14, 15, 16}
    setc = {9, 7, 8, 4, 5, 6, 3, 2, 1, 0}
    setd = {4, 6, 3}

    # set has 4 operations as follows,
    # Union gives output as new set with combination of both but keep values unique
    # Union : - seta.union(setb)
    #         - seta | setb
    # Intersection just gives you what is common between two sets. Symmetric difference is opposite of this.
    # Intersection : - seta.intersection(setb)
    #              : - seta & setb
    # Difference gives you what is present in first set but not in second
    # Difference :- seta.difference(setb)
    #             - seta - setb
    #             - setb.difference(seta)
    #             - setb - seta
    # Symmetric Difference is exact opposite of Intersection it gives you what values are not common between two sets
    # Symmetric Difference : - seta.symmetric_difference(setb)
    #                        - seta ^ setb

    print(isinstance(seta, set))
    print(isinstance(seta, list))
    print(isinstance(seta, dict))
    print(isinstance(seta, tuple))
    print(issubclass(set, list))
    print(type(set) is list)

    # setting first section for Set Operations
    # prints equal n times without linebreak
    print_section("SET OPERATIONS DEMO")

    # sets we started with
    print("Sets we started with:")
    print("seta: " + str(seta))
    print("setb: " + repr(setb))
    # Union demo
    print("Union Demo:")
    print(seta.union(setb))
    print(setb | seta)

    # Intersection demo
    print("Intersection Demo:")
    print(seta.intersection(setb))
    print(setb & seta)

    # difference demo
    # - there are 2 cases for it as a - b would be different from b - a
    print("Difference Demo:")
    print(seta.difference(setb))
    print(seta - setb)
    print(setb.difference(seta))
    print(setb - seta)

    # Symmetric Difference demo
    print("Symmetric Differnce Demo:")
    print(seta.symmetric_difference(setb))
    print(setb ^ seta)

    # Methods which should not be used with sets
    print_section("METHOD THAT SHOULD NOT BE USED WITH SET")
    print(
        "POP: Because set is unordered due to being hash table instead of sequence like list pop may "
        "pop random item"
    )

    # Method that can cause exception
    print_section("METHOD THAT CAN CAUSE EXCEPTION")
    print(
        "REMOVE: Use discard instead. Remove will cause exceptionn if item is not in set"
    )

    # Method that can be used safely and commonly

    print_section("METHOD THAT CAN BE USED SAFELY AND COMMONLY")

    print(
        ""
        "add - to add SINGLE item to set\n"
        "update - to add multiple items and input can be any iterable\n"
        "discard - to remove item\n"
        "clear - to empty set\n"
        "union - to union two sets or | can be used\n"
        "intersection - to find common items between two sets or & can be used\n"
        "differnce - to find difference between sets order matters or - (minus) can be used\n"
        "symmetric_difference - to find exact opposite of intersection or ^ can be used\n"
        "issuperset - to find if this set has **ALL** items of other set means its a superset\n"
        "issubset - to find if this set has **ALL** items from other set\n"
        "isdisjoint - to find no items overlap between two sets. NOTHING IN COMMON"
    )

    # Method demo
    print_section("METHOD_DEMO")

    # superset demo
    print("SUPERSET Demo:")
    print(f"seta: {seta}")
    print(f"setb: {setb}")
    print(f"Is seta superset of setb? :{seta.issuperset(setb)}")
    print(f"Is setb superset of seta? :{setb.issuperset(seta)}")

    print(f"setc: {setc}")
    print(f"setd: {setd}")
    print(f"Is setc superset of setd? :{setc.issuperset(setd)}")
    print(f"Is setd superset of setc? :{setd.issuperset(setc)}")

    # subset demo
    print()
    print("SUBSET Demo:")
    print(f"seta: {seta}")
    print(f"setb: {setb}")
    print(f"Is seta subset of setb? :{seta.issubset(setb)}")
    print(f"Is setb subset of seta? :{setb.issubset(seta)}")

    print(f"setc: {setc}")
    print(f"setd: {setd}")
    print(f"Is setc subset of setd? :{setc.issubset(setd)}")
    print(f"Is setd subset of setc? :{setd.issubset(setc)}")

    # disjoint demo
    print()
    print("DISJOINT Demo:")
    print(f"seta: {seta}")
    print(f"setb: {setb}")
    print(f"Is seta disjoint from setb? :{seta.isdisjoint(setb)}")
    print(f"Is setb disjoint from seta? :{setb.isdisjoint(seta)}")

    print(f"setc: {setc}")
    print(f"setd: {setd}")
    print(f"Is setc disjoint from setd? :{setc.isdisjoint(setd)}")
    print(f"Is setd disjoint fron setc? :{setd.isdisjoint(setc)}")
    print(f"Is seta disjoint fron setc? :{seta.isdisjoint(setc)}")

    # add demo
    print()
    print("ADD Demo:")
    print(f"setd: {setd} in next step we will add 9 in that set")
    setd.add(9)
    print(f"setd: {setd}")
    print("Now we will add 9 one more time")
    setd.add(9)
    print(
        f"setd: {setd}. \nAs seen 9 is only added once even though we tried adding it twice it silently rejects it."
    )

    # update demo
    print()
    print("UPDATE Demo:")
    print(
        f"setd: {setd}\nWe will add 1,2,3,4,5,6 to it using update method and using LIST\nAny iterrable can be used even STRING"
    )
    setd.update([1, 2, 3, 4, 5, 6])
    print(f"setd: {setd} \nNow we will update again using SET {1,2,3,4,5,6,7}")
    setd.update({1, 2, 3, 4, 5, 6, 7})
    print(f"setd: {setd}. \nAs seen same values are silently ignored while 7 is added.")

    print()
    print("REMOVE Demo")
    print(f"setd {setd} \nNow we will REMOVE 9 from this setd")
    setd.remove(9)
    print(
        f"setd: {setd}\nNow if we try to remove again it will cause exception KeyError: 9."
    )

    print()
    print("DISCARD Demo:")
    print(f"setd: {setd}\nNow we will discard 7.")
    setd.discard(7)
    print(
        f"setd: {setd}\nNow we will discard 7 again and it will ignore it WITHOUT EXCEPTION!"
    )
    setd.discard(7)

    print()
    print("CLEAR Demo:")
    print(f"setd: {setd}\nNow we will clear setd")
    setd.clear()
    print(f"setd: {setd}")

    print()
    print("CHECK if single item in set?")
    print(f"9 in setc? {9 in setc}")
    print(f"19 in setc? {19 in setc}")

    print()
    print(f"setc: {setc}")
    print("Loop through setc order is not guaranteed:")
    for i in setc:
        print(i)
    print(f"setc: {setc}")


# Method to printout sections
def print_section(section_title, num_of_equal_signs=15):
    print()
    print("=" * num_of_equal_signs, end="")
    print(f"{section_title}:", end="")
    print("=" * num_of_equal_signs)


if __name__ == "__main__":
    main()
