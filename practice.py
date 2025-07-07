

temps = [36.5, 37.0, 37.8, 38.2, 36.7]

users = {
    "divine": 5,
    "grace": 0,
    "john": 3
}


def print_userinfo():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    country = input("Enter your country: ")
    print(
        f"Hello {name.title()} from {country.title()}! You are {age} years old.")


# print all above 37
for temp in temps:
    if temp > 37:
        print(temp)


# print all users that has never logged in
for user in users:
    if users[user] == 0:
        print(user)

# print_userinfo()

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = "x" * number
    print(output)

# remove duplicates
nums = [2, 2, 4, 6, 3, 4, 6, 1]

for n in nums:
    number_of_occurences = nums.count(n)
    if number_of_occurences > 1:
        nums.remove(n)
print(nums)

unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
print(unique_nums)

list = [1, 2, 3, 4, 5]  # this is a list
tuple = (1, 2, 3, 4, 5)  # this is a tuple
# tuple is immutable.. cannot be changed
# unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)

# dictionary
customer = {
    "name": "John Doe",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

emoji_converter = {
    ":)": "😊",
    ":(": "😢"
}

message = input(">")
words = message.split(" ")
output = ""
for word in words:
    output += emoji_converter.get(word, word) + " "
print(output)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person("John")
person1.talk()
