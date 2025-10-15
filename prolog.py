# Simple Prolog-like program in Python

# Facts
facts = {
    "parent": [
        ("john", "mary"),
        ("mary", "susan"),
        ("susan", "lily")
    ]
}

# Rule: grandparent(X, Z) :- parent(X, Y), parent(Y, Z)
def grandparent(x, z):
    for y1, y2 in facts["parent"]:
        if y1 == x:
            for a, b in facts["parent"]:
                if a == y2 and b == z:
                    return True
    return False

# Query system
def query():
    print("Facts:")
    for rel, pairs in facts.items():
        for a, b in pairs:
            print(f"{rel}({a}, {b}).")
    print("\nQuery examples:")
    print("grandparent(john, lily)? ->", grandparent("john", "lily"))
    print("grandparent(mary, lily)? ->", grandparent("mary", "lily"))
    print("grandparent(john, susan)? ->", grandparent("john", "susan"))

# Run program
if __name__ == "__main__":
    query()
