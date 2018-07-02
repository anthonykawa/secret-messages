ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

class Cipher:
    def __init__(self, message):
        self.message = message
        self.encrypted_message = ""
        self.decrypted_message = ""

class Keyword(Cipher):
    def __init__(self, message, keyword):
        super().__init__(message)
        self.keyword = keyword
    
    @property
    def cipher_key(self):
        alphabet = list(ALPHABET)
        keyword = list(self.keyword)
        cipher_key = dict()
        for char in alphabet[:]:
            if keyword:
                popped = keyword.pop(0)
                cipher_key.update({char: popped})
                alphabet.remove(popped)
            else:
                cipher_key.update({char: alphabet.pop(0)})
        return cipher_key

    @property
    def decipher_key(self):
        decipher_key = dict()
        for key, value in self.cipher_key.items():
            decipher_key.update({value: key})   
        return decipher_key

    def encrypt(self):
        for letter in list(self.message):
            if letter == " ":
                self.encrypted_message += " "
            else:
                self.encrypted_message += self.cipher_key[letter.lower()]
    
    def decrypt(self):
        List = []
        for index, char in enumerate(self.encrypted_message):
            if char != " ":
                List.append(self.decipher_key[char])
            else:
                List.append(" ")
        self.decrypted_message = "".join(List)


keyword = "friendly"
message = "This is a message"

a = Keyword(message, keyword)
print(a.cipher_key)
print(a.decipher_key)
a.encrypt()
print(a.encrypted_message)
a.decrypt()
print(a.decrypted_message)



