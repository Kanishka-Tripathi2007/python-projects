print("Welcome to the love calculator!")
name_1 = input("What is your name?\n")
name_2 = input("what is their name ?\n")
connected_names = name_1 + name_2
lower = connected_names.lower()
t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
true = t + r + u + e 

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
    print(f"your love score is {love_score} and relationship would be like coke and mentos ")
elif love_score >= 45 and love_score <= 55 :
    print(f"your love score is {love_score} it is okay")
else :
    print(f"your love score is {love_score}")

