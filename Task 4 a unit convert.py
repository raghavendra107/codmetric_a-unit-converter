def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

conversion_functions = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°C", "°F"),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "°F", "°C"),
    "3": ("Kilometers to Miles", kilometers_to_miles, "km", "mi"),
    "4": ("Miles to Kilometers", miles_to_kilometers, "mi", "km"),
    "5": ("Kilograms to Pounds", kilograms_to_pounds, "kg", "lb"),
    "6": ("Pounds to Kilograms", pounds_to_kilograms, "lb", "kg"),
}

def main():
    while True:
        print("\nUnit Converter Menu:")
        for key, (desc, _, from_unit, to_unit) in conversion_functions.items():
            print(f"{key}. {desc} ({from_unit} → {to_unit})")
        print("0. Exit")

        choice = input("Select a conversion (0-6): ").strip()
        if choice == "0":
            print("Exiting Unit Converter. Goodbye!")
            break
        if choice not in conversion_functions:
            print("Invalid choice. Please try again.")
            continue

        desc, func, from_unit, to_unit = conversion_functions[choice]
        try:
            value = float(input(f"Enter value in {from_unit}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        result = func(value)
        print(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()