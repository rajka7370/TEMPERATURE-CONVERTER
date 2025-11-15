class TemperatureConverter:
   
    def celcius_to_fahrenheint(c):
        try: return float(c)*9/5+32
        except: return None
  
    def fahrenheit_to_celcius(f):
        try: return (float(f)-32)*5/9
        except: return None

while True:
    ch = input("1.Celcius to Fahrenhiet\n2.Fahrenheit to Celcius\n3.Exit:\nChoose an option: ")
    if ch == '1':
        c = input("C: "); r = TemperatureConverter.celcius_to_fahrenheint(c)
        print(f"{c}°C = {r:.2f}°F\n" if r is not None else "Invalid input\n")
    elif ch == '2':
        f = input("F: "); r = TemperatureConverter.fahrenheit_to_celcius(f)
        print(f"{f}°F = {r:.2f}°C\n" if r is not None else "Invalid input\n")
    elif ch == '3': 
        print("Thank You...❤️")
        break
    else: print("Pick 1, 2, or 3.\n")
