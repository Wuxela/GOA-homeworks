
correct_login = "leqso"
correct_password = "aba tu gamoicnob"
user_login = input("შეიყვანეთ ლოგინი: ")
user_password = input("შეიყვანეთ პაროლი: ")
login_success = (user_login == correct_login) and (user_password == correct_password)
print(login_success)