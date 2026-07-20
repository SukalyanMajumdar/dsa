import copy

# -------------------------------
# Create
# -------------------------------
student = {
    "name": "Alice",
    "age": 22,
    "marks": {
        "math": 95,
        "cs": 98
    }
}

print(student)

# -------------------------------
# Access
# -------------------------------
print(student["name"])          # Alice
print(student.get("age"))       # 22
print(student.get("city"))      # None
print(student.get("city", "Unknown"))

# -------------------------------
# Insert
# -------------------------------
student["city"] = "Kolkata"

# -------------------------------
# Update
# -------------------------------
student["age"] = 23

student.update({
    "cgpa": 9.2,
    "year": 4
})

# -------------------------------
# Membership
# -------------------------------
print("name" in student)
print("salary" in student)

# -------------------------------
# Length
# -------------------------------
print(len(student))

# -------------------------------
# Iterate keys
# -------------------------------
for key in student:
    print(key)

# -------------------------------
# Iterate values
# -------------------------------
for value in student.values():
    print(value)

# -------------------------------
# Iterate key-value pairs
# -------------------------------
for key, value in student.items():
    print(key, value)

# -------------------------------
# Delete
# -------------------------------
del student["year"]

student.pop("cgpa")

student.pop("salary", None)   # safe

# -------------------------------
# setdefault()
# -------------------------------
student.setdefault("country", "India")
student.setdefault("country", "USA")   # won't overwrite

print(student)

# -------------------------------
# Copy (Shallow)
# -------------------------------
copy1 = student.copy()

copy1["marks"]["math"] = 0

print(student["marks"]["math"])   # 0 (shared nested dict)

# -------------------------------
# Deep Copy
# -------------------------------
copy2 = copy.deepcopy(student)

copy2["marks"]["math"] = 100

print(student["marks"]["math"])   # still 0

# -------------------------------
# Keys / Values / Items
# -------------------------------
print(student.keys())
print(student.values())
print(student.items())

# -------------------------------
# Convert to list
# -------------------------------
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# -------------------------------
# Dictionary comprehension
# -------------------------------
square = {x: x*x for x in range(5)}

print(square)

# -------------------------------
# Merge
# -------------------------------
d1 = {"a": 1}
d2 = {"b": 2}

d3 = d1 | d2

print(d3)

# -------------------------------
# Clear
# -------------------------------
temp = {"x": 1, "y": 2}

temp.clear()

print(temp)