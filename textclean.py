text = input("Enter text: ")
unwanted_char = ["\n","\t",",/","/,",","]
for char in unwanted_char:
    text = text.replace(char,"")
text = text.strip()
text = text.lower()
print(f"clean text {text}")

letter_frequency = {}
for letter in text:
     letter_frequency[letter] = text.count(letter)
print(f" Letter frequencies = {letter_frequency}")
 
words = text.split(' ')
print(f"Words = {words}")
unique = set(words)
print(f"Unique Words = {unique}")  

print(f"Total word count = {len(words)}")
print(f"unique word count = {len(words)}")

word_frequency = {}
for words in unique:
     word_frequency[words] = words.count(words)
print(f"Word frequencies = {word_frequency}")

