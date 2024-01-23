lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Jimmy"]
friends.insert(1, "Kelly")

print(friends)
print("---"*15)

friends.remove("Jim")
friends.insert(3, "Jimmy")

print(friends)
print("---"*15)

print(friends.index("Jimmy"))

print("---"*15)

print(friends.count("Jimmy"))

print("---"*15)

friends.sort
lucky_numbers.sort

print(friends)
print(lucky_numbers)

print("---"*15)

friends2 = friends.copy()

print(friends2)