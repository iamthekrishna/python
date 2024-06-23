
#  String un three ways
# 1). Single quoted string
a = 18
b = 'Pooja'
print(a,b)
print(type(a),type(b))

# 2). double quoted string
a = "Pooja"
b = "Patel"
print(a,b)
print(type(a),type(b))

# 3). Tripal  quoted string
a = '''Pooja'''
b = '''Patel'''
print(a,b)
print(type(a),type(b))

# Use this if you have single quotes in your strings 
a = "Pooja's"
b = ''' Pooja"s and Pooja's'''
c = ''' Pooja"s and 
      Pooja's'''
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
''''''
#=====================Concatenating two string================================#

Greeting = "Good Morning"
name = "Pooja"
c = Greeting + name
print (c)
print(Greeting,name)

# ============================String Slicing==================================#
name="Pooja"
print(name[0])  # ===> The index ina string start from 0 to (length-1)
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# name[3]= "d" ===> do not work , string object does not support item assignment
print(name[0:3])  # ===> first index included and last index is not included
print(name[1:4])
print(name[0: ])  #  ===> is same as same [0:4]
print(name[ :4])  #  ===> is same as same [0:4]

# ============================Negative Index==================================#
name="Pooja"
print(name[-4:-1]) # ==> is same is same[1:4] ==> Left to Right in string

# ==========================Slicing with skip Value============================#
name="Pooja"
print(name[1:4:1])
print(name[0::2])
print(name[-4:-1:1])
print(name[::2])     # ==> acess entire string in setp 2
print(name[2::])     # ==>  acess string fromstr[2] to ending
print(name[:4:])     # ===> acess string from str[0] to str [3] in step of 1
print(name[-1::-1])  # ===> retrive from set[-1] till first element from right to left

# ==============================String Function================================#

story = "Once upon a time there was a youtuber named Pooja who uploaded python course with notes"

# string Function
#1) len()                   ==> This function return the length of the string
print(len(story))

#2) endswith()                  ==> Returns true if the string ends with the specified value
print(story.endswith("notes"))
print(story.endswith("Pooja"))

# 3) startswith()               ====> Returns true if the string starts with the specified value
print(story.startswith("Once"))
print(story.startswith("notes"))

# 4) Upper()              ==> Converts a string into upper case
print(story.upper())

# 5) lower()                ===> Converts a string into lower case
print(story.lower())

# 6) Capitalize()            ===> Converts the first character to upper case
print(story.capitalize())

# 7) find()                    ==>  if it is not present then it will give in -1 (-1 is standard value)
print(story.find("once"))
print(story.find("pooja"))

# 8) count()             ====> Returns the number of times a specified value occurs in a string
print(story.count("a")) 
print(story.count("pooja"))

# 9) replace()           ====> Returns a string where a specified value is replaced with a specified value
print(story.replace("Pooja","Mayank"))
print(story.replace("python", "java"))

# 10) index()           ==> Searches the string for a specified value and returns the position of where it was found 
print(story.index("Once"))  # ==> find and index both are similar 
print(story.index("notes"))
print(story.index("Pooja"))

# 11) casefold()       ===> Converts string into lower case  , lower and caseford is same
print(story.casefold())

# 12) rindex()       ==> Searches the string for a specified value and returns the last position of where it was found
print(story.rindex("Pooja"))
print(story.rindex("Once"))
print(story.rindex("notes"))

# ===============================Escape Sequences================================#

# \n = New line
# \t = Horizontal Tab Space
# \v = Vertical Tab Space 
# \\ = Backslash
# \a = Bell or alter 
# \b = Backspace

story = "Mayank is good.\nHe is very good"
print(story)

story = "Mayank is good.\t He is very good"
print(story)

story = "Mayank is good.\n\t He is very good"
print(story)

story = "Mayank is good.\v He is very good"
print(story)

story = "Mayank is good.\a He is very good"
print(story)

story = "Mayank is good.\b He is very good"
print(story)
