"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    temp = input("Enter the temperature: ")
        unit = input("Farenheit or Celsius? ")
        if unit.lower() == "farenheit":
            celsius = int(temp) - 32
            celsius = celsius * 5/9
            print("The temperature in Celsius is: " + str(celsius))
        elif unit.lower() == "celsius":
            farenheit = int(temp) * 9/5
            farenheit = farenheit + 32
            print("The temperature in Farenheit is: " + str(farenheit))
    

if __name__ == "__main__":
    
main()
