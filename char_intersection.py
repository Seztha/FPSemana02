sentence1 = input()
sentence2 = input()
words = ""
wordlist1 = sentence1.split(" ")
wordlist2 = sentence2.split(" ")
set = set()

for i in wordlist1:
    if i in wordlist2:
        set.add(i)
for i in set:
    words = words + " " + (i)

print(words.replace(" ", "", 1))