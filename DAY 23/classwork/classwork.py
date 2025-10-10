cars = ["BMW", "Mercedes", "Audi"]
print("საწყისი სია:", cars)

cars.append("Toyota")
print("append-ის შემდეგ:", cars)

cars.insert(1, "Honda")
print("insert-ის შემდეგ:", cars)

cars.remove("Audi")
print("remove-ის შემდეგ:", cars)

removed_car = cars.pop(2)
print("pop-ის შემდეგ:", cars)
print("ამოშლილი მანქანა იყო:", removed_car)

print("სიის სიგრძე:", len(cars))