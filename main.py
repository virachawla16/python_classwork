print("Hello world")
print()

print("My name is Vira")

age = 15
isalive = True
name = "Vira"

print()
print("My age is", age)

print()


users_age = int(input("Please enter your age: "))

print()

print("Wow", users_age, "its a pretty terrible age to be I think")

print()


if users_age > 18:
  print("GO VOTE")


elif users_age < 18:
  print("You need to 18 to vote")

elif users_age == 21:
  print("You can vote and drink!")

elif users_age == 25:
  print("You can vote, drink and rent a car!")

else:
  print("wowowo 18, time to vote!")

print("Thanks for playing!")

print()


long_sentance = "hello my name is vira and i like music"
broken_sentance = long_sentance.split(" ")
print(broken_sentance[5])