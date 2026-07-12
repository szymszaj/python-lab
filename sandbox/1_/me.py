person = {
    "name": "Szymon", 
    "age": 28,
    "hobby": "games",
    "job": "frontend",
}
print(person["name"])
print(person["age"])

print(f"My name is {person['name']}, I work as a {person['job']}, "
      f"I am {person['age']} years old and I like {person['hobby']}.")



def describe(data):
    return (f"My name is {data['name']}, I work as a {data['job']}, "
            f"I am {data['age']} years old and I like {data['hobby']}.")

print(describe(person))

second = {"name": "Ala", "age": 25, "hobby": "running", "job": "backend"}
print(describe(second))

def describe2(name, age, hobby, job):
    return (f"My name is {name}, I work as a {job}, "
            f"I am {age} years old and I like {hobby}.")

print(describe2("Kuba", 30, "music", "designer"))
