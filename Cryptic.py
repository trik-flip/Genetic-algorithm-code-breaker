""""""


from random import choice


def decrypt(key: str, text: str):
    """"""
    decrypted_text = ""
    key = key_smith(key, text)
    for index, letter in enumerate(text):
        decrypted_text += chr(((ord(letter) -
                                ord(key[index]) + 26) % 26) + 65)
    return decrypted_text


def encrypt(key: str, text: str):
    """"""
    encrypted_text = ""
    key = key_smith(key, text)
    for index, letter in enumerate(text):
        encrypted_text += chr(((ord(letter) +
                                ord(key[index])) % 26) + 65)
    return encrypted_text


def key_generator(length: int = 6,
                  possibilities: list = [chr(x+65) for x in range(26)]):
    """"""
    return "".join([choice(possibilities) for _ in range(length)])


def key_smith(key, text):
    """"""
    i = 0
    new_key = ""
    for _ in text:
        if i == len(key):
            i = 0
        new_key += key[i]
        i += 1
    return new_key
