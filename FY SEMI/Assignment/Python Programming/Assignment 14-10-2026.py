# 1. Write a program to read a file and count how many vowels are present in its content.

file = open("data.txt", "r")

content = file.read()
count = 0

for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

file.close()

# 2. Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

file = open("data.txt", "r")

lines = file.readlines()

print("Total Lines:", len(lines))

print("Second line:", lines[1].strip())
print("Fourth line:", lines[3].strip())

file.close()

# 3. Take a sentence from the user, split it into words, and store them in a list. Print the longest word.

sentence = input("Enter a sentence:")

words = sentence.split()

longest = max(words, key=len)

print("Words:", words)
print("Longest word:", longest)

# 4. Read a file, split its content into words, and store them in a list.
#    i. Print the total number of words.
 
file = open("data.txt", "r")

content = file.read()

words = content.split()

print("Total words", len(words))

file.close()

   ii. Print all unique words.file

file = open("data.txt", "r")

content = file.read()

words = content.split()

unique_words = set(words)

print("Unique Words:", unique_words)

file.close()