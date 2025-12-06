import json

x = {
    "name": "John",
    "age": 35,
    "city": "New York"
}

y = json.dumps(x)      # dump → convert into JSON

print(y)

print(json.dumps(["Ganga", "Narmada"]))

print(json.dumps(("apple", "grapes")))

print(json.dumps("Welcome"))

print(json.dumps(42))

print(json.dumps((42,53)))

print(json.dumps(True))

print(json.dumps(False))

print(json.dumps(None))




























