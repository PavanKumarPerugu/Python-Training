def temp_cal():
    # Ask the user for the input temperature unit.
    # strip() removes extra spaces, lower() ensures case-insensitive comparison.
    choice_of_input_unit = input(
        "Select the Unit of Input (celsius, kelvin, fahrenheit): "
    ).strip().lower()

    # Ask the user for the desired output temperature unit.
    # Normalizing input avoids errors due to capitalization or spacing.
    choice_of_output_unit = input(
        "Select the Unit of Output (celsius, kelvin, fahrenheit): "
    ).strip().lower()

    # Read the temperature value and convert it to float
    # Assumes the user enters a valid numeric value.
    input_temp = float(input("Enter the Temperature reading in digits: "))

    # If input and output units are the same, no conversion is needed
    if choice_of_input_unit == choice_of_output_unit:
        return "Entered the same Units of Input & Output!!"

    # Conversions when the input unit is Celsius
    elif choice_of_input_unit == "celsius":
        if choice_of_output_unit == "kelvin":
            # Celsius to Kelvin conversion
            return f"Temperature in Kelvin is {input_temp + 273.15} K"
        elif choice_of_output_unit == "fahrenheit":
            # Celsius to Fahrenheit conversion
            return f"Temperature in Fahrenheit is {32 + input_temp * (9/5)} F"
        else:
            # Invalid output unit entered
            return "Enter the right choice of Output Unit!!"

    # Conversions when the input unit is Kelvin
    elif choice_of_input_unit == "kelvin":
        if choice_of_output_unit == "celsius":
            # Kelvin to Celsius conversion
            return f"Temperature in Celsius is {input_temp - 273.15} C"
        elif choice_of_output_unit == "fahrenheit":
            # Kelvin to Fahrenheit conversion
            return f"Temperature in Fahrenheit is {32 + (input_temp - 273.15) * (9/5)} F"
        else:
            # Invalid output unit entered
            return "Enter the right choice of Output Unit!!"

    # Conversions when the input unit is Fahrenheit
    elif choice_of_input_unit == "fahrenheit":
        if choice_of_output_unit == "celsius":
            # Fahrenheit to Celsius conversion
            return f"Temperature in Celsius is {(input_temp - 32) * (5/9)} C"
        elif choice_of_output_unit == "kelvin":
            # Fahrenheit to Kelvin conversion
            return f"Temperature in Kelvin is {273.15 + (input_temp - 32) * (5/9)} K"
        else:
            # Invalid output unit entered
            return "Enter the right choice of Output Unit!!"

    # Handles invalid input unit entries
    else:
        return "Enter the right choice of Input Unit!!"


# Call the temperature conversion function
result = temp_cal()

# Display the result to the user
print(result)
