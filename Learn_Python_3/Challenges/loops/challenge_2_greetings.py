def add_greetings(names):
    name_and_greeting = []
    for name in names:
        name_and_greeting.append("Hello, " + name)
    return name_and_greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))