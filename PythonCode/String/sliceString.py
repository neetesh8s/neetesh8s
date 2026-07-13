b = "Hello, World!"
#Slice Get the characters from position 2 to position 5 (not included):
print(b[2:5])
#Slice From the Start
#By leaving out the start index, the range will start at the first character:
#Get the characters from the start to position 5 (not included):
print(b[:5])
#Slice From the End
# Get the characters from position 2, and all the way to the end:
print(b[2:])
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
print(b[-5:-2])