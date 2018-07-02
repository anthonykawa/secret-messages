ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

def run():
    message = Affine("This is the message that I'd like you to know!!", 1, 8)
    message.encrypt()
    print(message.encrypted_message)
    message.decrypt()
    print(message.decrypted_message)

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

class Polybius(Cipher):
    def __init__(self, message):
        super().__init__(message)

class Affine(Cipher):
    def __init__(self, message, keya, keyb):
        super().__init__(message)
        self.keya = keya
        self.keyb = keyb
    
    def inverse_mod(self, keya, mod):
        for _ in range(1,mod):
            if ( mod * _ + 1) % keya == 0:
                return ( mod * _ + 1) // keya
        return None

    def encrypt(self):
        for char in self.message:
            if char.lower() in ALPHABET:
                char_index = ALPHABET.index(char.lower())
                self.encrypted_message += ALPHABET[(char_index * self.keya + self.keyb) % len(ALPHABET)]
            else:
                self.encrypted_message += char

    def decrypt(self):
        mod_inverse_keya = self.inverse_mod(self.keya, len(ALPHABET))
        for char in self.encrypted_message:
            if char.lower() in ALPHABET:
                char_index = ALPHABET.index(char.lower())
                self.decrypted_message += ALPHABET[(char_index - self.keyb) * mod_inverse_keya % len(ALPHABET)]
            else:
                self.decrypted_message += char

if __name__ == "__main__":
    run()
