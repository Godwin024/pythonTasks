def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


print("Celsius\tFahrenheit")

for celsius in range(0, 101):

    print(f"{celsius}\t\t{fahrenheit(celsius):.1f}")
