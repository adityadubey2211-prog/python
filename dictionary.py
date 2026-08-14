# Creating a dictionary
student = {
    "name": "Aditya",
    "age": 20,
    "course": "B.Tech",
    "marks": 85
}

print(student)
print(student["name"])
print(student["age"])
print(student.get("course"))
print(student.get("city"))       # None
print(student.get("city", "Delhi"))  # Delhi
student["marks"] = 90

print(student)
if "name" in student:
    print("Name exists")

if "city" not in student:
    print("City does not exist")
print(student.keys())
print(student.values())
print(student.items())