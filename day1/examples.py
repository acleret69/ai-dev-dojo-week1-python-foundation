# VARIABLES
name = "Alex"
age = 25
city = "Lyon"

# CONDITION
if age >= 18:
    print("Majeur")
else:
    print("Mineur")

# LISTE + BOUCLE
sports = ["foot", "natation", "musculation", "boxe", "yoga"]
for sport in sports:
    print(sport)


# FONCTION
def greet(name):
    return f"Bonjour {name}"


print(greet("Alex"))
