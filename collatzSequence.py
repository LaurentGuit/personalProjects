# Check if even
def IsEven(number):
    
    if number % 2 == 0:
        en = True
    else:
        en = False
    return en

def collatz(number , en):

    if en:
        a = number // 2
        return a
    else:
        b = 3 * number + 1
        return b

while True:
    print('Enter a number for Collatz sequence')
    number = int(input())

    while number != 1:
        en = IsEven(number)
        coll = collatz(number , en)
        number = coll
        print(number)
