from random import randint


def generate(cLength):
    cList = []
    catches = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
    characters = list(catches)
    for c in range(0, cLength):
        char = randint(0, len(characters) - 1)
        cList.append(characters[char])
    captcha = "".join(cList)
    return captcha
