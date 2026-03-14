def sumDigits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total
number = int(input("შეიყვანეთ რიცხვი: "))
result = sumDigits(number)
print("რიცხვის ციფრების ჯამი არის:", result)