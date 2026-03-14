def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))
fahrenheit = celsiusToFahrenheit(celsius)
print("ტემპერატურა ფარენჰეიტში არის:", fahrenheit)