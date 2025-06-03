import random

# Generates strong, balanced, and randomized passwords of specified length (must be a multiple of 4)


def password_generator(plen):
    # Enforce that the password length is both >= 4 and divisible by 4
    if plen % 4 != 0 or plen < 4:
        raise ValueError(
            "Password length must atleast 4 or multiple of 4 i.e; 4,8,12,..."
        )

    # Define character groups: digits, lowercase, uppercase, special characters
    numList = list("0123456789")
    smallAlphaList = list("abcdefghijklmnopqrstuvwxyz")
    capitalAlphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    charList = list("!#$%&\"'()*+,-./:;<=>?@[\\]^_`{|}~")

    allCharList = [numList, smallAlphaList, capitalAlphaList, charList]

    result = []

    for i in allCharList:
        # Use sample for uniqueness if group has enough characters; else allow duplicates
        if len(i) >= int(plen / 4):
            result.extend(random.sample(i, k=int(plen / 4)))
        else:
            result.extend(random.choices(i, k=int(plen / 4)))

    # Shuffle twice for stronger randomness and less pattern predictability
    random.shuffle(result)
    random.shuffle(result)

    return "".join(result)


for i in range(0, 100):
    print(password_generator(plen=24))
