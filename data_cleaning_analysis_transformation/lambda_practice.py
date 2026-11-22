#########
# DIFFERENT WAYS OF TRANSFORMING DATA. MAP vs LIST/DICT Comprehension vs Traditional in place Loops vs Generators
# MAP - Good when you don't have to use lambda or when you are only accessing 1D array for transformation. Easy on memory
# LIST/DiCt Comprehension - Fastest but uses 2x the memory as it has to make copy
# Traditional Loops - Fast and easy on memory as it modifies one item at a time not the FASTEST
# Generator - uses same syntax as List/Dict comprehension only brackets differnce uses ( ) instead of [].
# It comsumes less almost near zero memory as it is iterator and if the row is sent to db or some other
# permanent storage place almsot no memory cosnumption


from functools import reduce
import copy


def main():
    ## EXAMPLE 1
    # goal is to remove the dollar sign and convert to float
    list_dollar = ["$100.00", "$99.00", "$27.00"]
    # # METHOD 1
    # used lambda with terrtiary condition as can't use if as lambda takes expression
    remove_dollar = lambda x: float(x[1:]) if x[0] == "$" else float(x)
    print(list(map(remove_dollar, list_dollar)))

    # # MEtHOD 2
    remove_dollar2 = lambda p: float(p.replace("$", ""))
    print(list(map(remove_dollar2, list_dollar)))

    ## EXAMPLE 2
    # Goal is Filter out anything lower than 100
    list_filter = [200, 400, 600, 400.90, 200, 100, 88, 99, 330]
    my100filter = lambda x: x >= 100
    print(list(filter(my100filter, list_filter)))

    ## EXAMPLE 3
    # Goal is to filter out students with score less than 70
    students = [
        ["Adnan", 84],
        ["Mark", 89],
        ["Cathy", 68],
    ]

    print(list(filter(lambda x: x[1] >= 70, students)))

    ## EXAMPLE 4
    # GOAL is use same list of students and filter out all students except the one starting with M
    print(list(filter(lambda x: x[0][0] == "M", students)))

    # EXAMPLE 4
    # Goal lets sort student by numbers in place (means sorting by second column)
    print(students)
    students.sort(key=lambda x: x[1], reverse=True)
    print(students)

    # EXAMPLE 5
    # Goald lets sort students again by first column out of place means by generating new list
    print(list(sorted(students, key=lambda x: x)))

    # EXAMPLE 6
    # Goal lets exapand student to have few more records then sort by numbers followed by name. Means second column then first column
    students.extend(
        [["Adnan", 99], ["Mike", 78], ["Mik", 89], ["Cat", 63], ["Nina", 67]]
    )

    students.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(students)
    """
    Above statement creates a problem in case where value at index 1 is a tie in that case value at index 0 also get sorted descending while 
    we really wanted index 1 columns to be sorted desc while index 0 to be asc to fix that two methods exist. 

    Method 1 : 

    students.sort(key=lambda x: ((-x[1], x[0]))
    # Above technique really works because it inverts sorting order by first given column only but it only works if that column is number 

    Method 2: 
    # Do the second sort first then the first sort in next step so this really makes it alogorithm really O(n log n) * 2 but works for string

    students.sort(key= lambda x: x[0])
    students.sort(key= lambda x : x[1], reverse=True)
    """

    # Example 7
    # We will use MAP , REDUCE which is very famous in this example
    # Goal is to use MAP to make all student name capital
    # Goal is to use reduce to calculate the sum of all numbers

    # Lets make a deep copy of students before we mess with it
    students2 = copy.deepcopy(students)

    print(students2)
    number_of_students = len(students2)
    print(f"There are {number_of_students} in the class.")

    # This gets way too complicated. In cases where you need to approach string in nested lists LIST Comprehension or Loops,
    #  or Generator are better
    students2 = list(map(lambda item: ([str.upper(item[0]), item[1]]), students2))
    print(students2)

    # Similar above script can be done by list comprehension
    students2 = [[name.upper(), score] for name, score in students]
    print(students2)

    # lets use reduce now but I already realize issue here as I should have used it only on 1D array
    # instead of 2D anyway lets see
    # Notice 0 at the end we had to pass it so it doesn't use first column of list which has user names
    # reduce is discourages instead SUM is preferred way to use with list comprehension
    sums = reduce(lambda x, y: x + y[1], students2, 0)
    print("Sum using reduce : ", sums)

    # Alternative using GENERATOR with SUM
    sums2 = sum(score for _, score in students2)
    print("Sum using GENERATOR with SUM : ", sums2)

    # Alternative using LIST COMPREHENSION but GENERATOR is best
    sum3 = sum([score for _, score in students2])
    print("Sum using List Comprehension with SUM : ", sums2)


if __name__ == "__main__":
    main()
