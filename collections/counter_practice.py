from collections import Counter

# Counter collection is nothng but dictionary but it makes it easy to count list items when list with duplicates
# is being converted to dictionary


def main():
    fruits = ["appple", "banana", "apple", "pear", "Apple", "kiwi", "apple"]

    print("Section showing how to use counter: ")
    print("Printing Counter object:")
    print(count_items(fruits))
    print("Printing Dictionary object:")
    print(count_items_dict(fruits))

    # Counter special methods
    # These methods give Top N values sorted this feature doesn't exist in Dictionary
    print()
    print("Section on Counter special method:")
    count = Counter(fruits)
    print(f"Sorted by most common. {count.most_common()}")
    print(f"Top N items from Counter. Top 1 in this case {count.most_common(1)}")
    # Im regular dictionary it would throw KeyError since this key doesn't exist
    print(
        f'count["Coconut"] This should return 0 since coconut is not in the list. {count["Coconut"]}'
    )


# returns Counter object
def count_items(items):
    return Counter(item.lower() for item in items)


# In above line we have used list comprehension along with counter collection.


# returns Dictionary object
def count_items_dict(items):
    return dict(Counter(item.lower() for item in items))


if __name__ == "__main__":
    main()
