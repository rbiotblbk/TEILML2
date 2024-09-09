

user = {
    "first_name": "Thomas",
    "last_name": "Meier",
    "age": 55,
    "kids": ["Julia", "Lena"],
    "kids2": [
        {"id": 100, "first_name": "Julia", "friends": ["Max", "Frank"]},
        {"id": 101, "first_name": "Lena", "friends": ["Sara", "Mike"]},


    ]
}


print(user["age"])
print(user["kids"])
print(user["kids"][0])
print(user["kids"][1])
print(user["kids"][-1])

print(user["kids2"][0])
print(user["kids2"][0]["first_name"])

print(user["kids2"][1]["friends"][1])  # Mike
print(user["kids2"][1]["friends"][-1])  # Mike
print(user["kids2"][-1]["friends"][-1])  # Mike
