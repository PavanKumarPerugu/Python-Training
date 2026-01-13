def temp_cal():

    choice_of_input_unit = input("Select the Unit of Input (celsius, kelvin, fahrenheit): ").strip().lower()
    choice_of_output_unit = input("Select the Unit of Output (celsius, kelvin, fahrenheit): ").strip().lower()
    input_temp = float(input("Enter the Temperature reading in digits: "))

    if choice_of_input_unit == choice_of_output_unit:
        return "Entered the same Units of Input & Output!!"
    
    elif choice_of_input_unit == "celsius":
        if choice_of_output_unit == "kelvin":
            return f"Temperature in Kelvin is {input_temp+273.15} K"
        elif choice_of_output_unit == "fahrenheit":
            return f"Temperature in Fahrenheit is {32+input_temp*(9/5)} F"
        else:
            return "Enter the right choice of Output Unit!!"
        
    elif choice_of_input_unit == "kelvin":
        if choice_of_output_unit == "celsius":
            return f"Temperature in Celsius is {input_temp-273.15} C"
        elif choice_of_output_unit == "fahrenheit":
            return f"Temperature in Fahrenheit is {32+(input_temp-273.15)*(9/5)} F"
        else:
            return "Enter the right choice of Output Unit!!"
        
    elif choice_of_input_unit == "fahrenheit":
        if choice_of_output_unit == "celsius":
            return f"Temperature in Celsius is {(input_temp-32)*(5/9)} C"
        elif choice_of_output_unit == "kelvin":
            return f"Temperature in Kelvin is {273.15+(input_temp-32)*(5/9)} K"
        else:
            return "Enter the right choice of Output Unit!!"
        
    else:
        return "Enter the right choice of Input Unit!!"


result = temp_cal()
print(result)