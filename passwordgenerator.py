import random


def generateSecurePassword(weakpassword):
    newpassword = ""
    replacements = {
        "e": [3],
        "o": [0],
        "a": [4, "@"]
    }

    for character in weakpassword:
        c = character.lower()

        if c in replacements:
            randomindex = random.randint(0, len(replacements[c]) - 1)
            rep = str(replacements[c][randomindex])
            newpassword = newpassword + rep
        else:
            newpassword = newpassword + character

    return (newpassword)


weakpassword = input("Enter your weak password:")

print(generateSecurePassword(weakpassword))