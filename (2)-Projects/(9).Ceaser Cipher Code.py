alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def encryption(shift_key,plain_text):
    cipher_text=""
    for char in plain_text:
      if char in alphabets:
        position=alphabets.find(char)
        new_position=(position+shift_key)%26
        cipher_text= cipher_text + alphabets[new_position]
      else:
        cipher_text=cipher_text+char
    print(f"cipher text is: {cipher_text}")
def decryption(shift_key,cipher_text):
    plain_text=""
    for char in cipher_text:
      if char in alphabets:
        position=alphabets.find(char)
        new_position=(position-shift_key)%26
        plain_text=plain_text+alphabets[new_position]
      else:
        plain_text=plain_text+char
    print(f"plain text is: {plain_text}")
function=input("enter 'encrypt' for encryption and 'decrypt' for decryption:\n")
text=input("enter the text:")
shift=int(input("enter the shift key:"))
if function=='encrypt':
  encryption(shift,text)
else:
  decryption(shift,text)