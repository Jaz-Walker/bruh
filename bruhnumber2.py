#more strings and tests
# below we are setting the words to the words we want
x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
# below us we are putting our words into code (%s) is used for words
y = "Those who know %s and those who %s " % (binary, doNot)
# below we made it to where we can just type x and the word we want will type out
print(x)
print(y)

print("I said: %r.:" % x)

hilarious = False
jokeEvaluation = "Isn't that joke so funny?!?! %r"
print(jokeEvaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"
print(w+e)

# more printing fun
print("Mary had a little lamb")
print("It's fleece was white as %s" % 'snow')
print("And everywhere that mary went")
print(", * 10")
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1+end2+end3+end4+end5+end6)
print(end7+end8+end9+end10+end11+end12)
print("yes")

 # why do I  use %r instead of %s in the above example?

formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why does %r sometimes give me single quotes around things?

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here. 
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6
""")

print("Here are the months: %r" % months)
print("Here are the months: %s" % months)

# escape sequences redux

tabbyCat = "\tI'm tabbed in."
persianCat = "I'm spit\non a line."
backslashCat = "I'm \\ a \\ cat."
topCat = """ I'll do a list
\t cat food
\t Fishies
\t Catnip
\tGrass
"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)


# Escape Seq            What it does?
# \\                    a
# \'
# \"
# \a
# \b
# \f
# \n
# \N{Name}
# \r
# \t
# \uxxxx
# \uxxxxxxx
# \v
# \ooo
# \xhh

# what does the following code do:
#  while True:
#       for i in ["/", "-", "|", "\\", "|"]:
#           print("%s\r" % i, end='')

# can you use ''' instead of """


age = input("How old are you?")
height = input("How tall are you?")


print("So, you are %r old and %r tall." % (age,height))

# ask 4 more questions and handle those responses

length = input("How long is the box?")
width = input("How wide is the box?")

print("So the box is %r long and %r wide." % (length, width))

#2

ammo = input("What ammo does the gun fire?")
ammoAmount = input("How much ammo does the gun have?")

print("So the gun fires %r and has %r amount of ammo." % (ammo, ammoAmount))


#StoryTime

name = input("What is your name?")
feeling = input("How did you like going to Barnes and Noble?")
goAgain = input("Do you think that you would go again?")
liked = input("What did you enjoy about going?")
wantDo = input("Is there anything you wanted to do but didn't?")
favBook = input("What was your favorite book out of the whole store?")
friends = input("Did you see any friends while you were there?")


print("Jim is a 3rd grader who took a trip to Barnes and Noble. After his trip I asked him about what he saw and what he liked.")

print("Thanks Jim, I'm going to be asking some questions about your venture to the local Barnes and Noble." % (name))
print("That's good to know.")
print("I'm glad that you liked that.")
print("Oh, well that's too bad but maybe you'll be able to do it next time you go.")
print("Hey, that was my favorite book as a kid, nice choice.")
print("Well maybe you'll see more next time.")
print("")