sentence = input("Enter the Sentence:")
sentence = sentence.lower()
count = 0
for i in sentence:
    if i in ("a","e","i","o","u"):
        count += 1
print(count)        