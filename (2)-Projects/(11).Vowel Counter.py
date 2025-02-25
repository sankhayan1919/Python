input=input("Enter:")
vowels="aeiou"
input=input.lower()
print(input)
count={}.fromkeys(vowels,0)
for char in input:
    if char in count:
        count[char]+=1
print(count)