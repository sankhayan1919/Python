def Word(word):
    wrev=word[::-1]
    if word==wrev:
        print("It is a palindrome word")
    else:
        print(wrev)
        print("It is not a palindrome word")
def Number(num):
    nrev=num[::-1]
    if num==nrev:
        print("It is a palindrome number")
    else:
        print(nrev)
        print("It is not a palindrome number")
choice=input("Enter 'word' to check palindrome word or enter 'num' to check plaindrome number: ")
if(choice=='word'):       
    word=input("Enter a word: ")
    Word(word)
elif(choice=='num'):
    num=input("Enter a number: ")
    Number(num)
else:
    print("Enter valid input")