user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

# Challenge1
# 1. Create new dict
# 2. keep only pairs with string values
# 3. Convert values to uppercase
# 4. Elegant & short solution
cleaned_user = {
    # Transformation
    key: value.upper()
    # Iterate
    for key, value in user.items()
    # Filter
    if isinstance(value, str)
}
print(user)
print(cleaned_user)
