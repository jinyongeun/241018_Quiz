import random

def lotto():
    result = []

    while len(result) < 6:
        number = random.randint(1,45)
        if number not in result:
            result.append(number)
    return result

lotto_num = lotto()
print(lotto_num)