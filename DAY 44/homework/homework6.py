def sumInRange(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total
start = int(input("შეიყვანეთ შუალედის დასაწყისი: "))
end = int(input("შეიყვანეთ შუალედის დასასრული: "))
result = sumInRange(start, end)
print(f"რიცხვების ჯამი {start}-დან {end}-მდე არის: {result}")