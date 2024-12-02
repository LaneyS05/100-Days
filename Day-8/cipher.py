print("Caesar Cipher")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play = True

while play:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))


    def caesar(origanal_text, shift_amount, encode_or_decode):
        output_text = ""
        
        for letter in origanal_text:
            if letter not in alphabet:
                output_text += letter
            else:
                if encode_or_decode == "decode":
                    shift_amount *= -1
            
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]

        print(f"here is the {encode_or_decode}d result: {output_text}")

    caesar(origanal_text=text, shift_amount=shift, encode_or_decode=direction)

    again = input("do you want to play again? yes or no\n").lower()
    if again == "no":
        break






"""
def encrypt(origanal_text, shift_amount):
    cipher_text = ""

    for letter in origanal_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"here is the encoded result: {cipher_text}")

    
def decrypt(origanal_text, shift_amount):
    output_text = ""

    for letter in origanal_text:
        shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"here is the decoded result: {output_text}")

encrypt(origanal_text=text, shift_amount=shift)
decrypt(origanal_text=text, shift_amount=shift)
"""