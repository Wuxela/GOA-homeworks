score = int(input("შეიყვანე შენი ქულა (0-100): "))

if score >= 90 and score <= 100:
    print("შენი შეფასებაა: A - საღოლ")
elif score >= 70 and score <= 89:
    print("შენი შეფასებაა: B - კარგი")
elif score >= 50 and score <= 69:
    print("შენი შეფასებაა: C - წავა რა")
elif score >= 0 and score <= 49:
    print("შენი შეფასებაა: ჩაიჭრე")
else:
    print("შეყვანილი ქულა არასწორია! შეიყვანე რიცხვი 0-დან 100-მდე.")