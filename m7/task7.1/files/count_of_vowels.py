
vowels = 'aeiouAEIOU'

def count_vowels(word):
    count = 0
    for i in word:
        if (vowels.find(i) != -1):
            count += 1
    print("Count of vowels: ", count)


print("==========COUNT OF VOWELS IN WORD==========\n")
print("Enter your word:")
word = input()

count_vowels(word)

#Also a want to do this task with files. So, let's start

print("\nEnter the name of your file:")
file_name = input()

file = open(file_name, "r")
count_vowels(file.read())
file.close()
