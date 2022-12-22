a = "Hungary"
b = "Romania"

print(type(a))
print(type(b))

print("\n")
print(b)
print("\t")

print(a)

print(a[4])
print(a[0:3])
print(a[-2])
print(a[3:])

c = "Here a sentence, god emperor"

print("All hail:", c)
print("God Emperor: %s" %c)

number = 546.876164
print(number)

print("%.4f" %number)


user = input("What is your W40K name?")
user2 = input("What is your Dune name?")

print(user+user2)
print("Your name is " + user + " " + user2)
print("Hello {} {}".format(user, user2))