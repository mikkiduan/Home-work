fruit = "banana"
m = fruit[1]
print(m)

m = fruit[0]
print(m)

fruit = "banana"
list(enumerate(fruit))

prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(prime_nums[6])
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
print(friends[6])

fruit = "banana"
print(len(fruit))

sz = len(fruit)
last = fruit[sz-1]

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

for c in fruit:
    print(c)

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)


s = "Pirates of the Caribbean"
print(s[0:7])
print(s[11:14])
print(s[15:24])
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
print(friends[2:4])

fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print(fruit[3:999])


word =("F")
if word == "banana":
    print("Yes, we have no bananas!")


if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")


greeting = "Hello, world!"
new_greeting ="J"
print(new_greeting+greeting[1:])


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels

print(remove_vowels("compsci"))
print(remove_vowels("aAbEefIijOopUus"))


def find(strng, ch):
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))


def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return(count)

print(count_a("asaasad"))


def find2(strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1
print(find2("banana", "a", 3))

def find(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1
print(find("banana", "a"))

def find3(strng, ch, start=0, end=None):
    ix = start
    if end is None:
       end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

ss = "Python strings have some interesting methods."
print(find(ss, "s"))
print(find2(ss, "s", 7))
print(find2(ss, "s", 8))
print(find3(ss, "s", 8, 13))
print(find(ss, ".") == len(ss)-1)


print(ss.find("s"))
print(ss.find("s", 7))
print(ss.find("s", 8))
print(ss.find("s", 8, 13))
print(ss.find("."))

print("banana".find("nan"))
print("banana".find("na",3))