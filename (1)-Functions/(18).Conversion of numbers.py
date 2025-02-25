decimal=int(input("enter:"))
print(bin(decimal))
print(oct(decimal))
print(hex(decimal))
character=input("enter the character:")
print(f"ASCII value of {character} is {ord(character)}")

def convert(a):
    if a>1:
        convert(a//2)
    print(a%2,end="")
a=int(input("Enter:"))
convert(a)