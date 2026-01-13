def bmi_check(bmi):
    """
    Determines BMI category based on BMI value.
    """
    if bmi <= 18.4:
        return "You are Underweight!!"
    elif 18.5 <= bmi <= 24.9:
        return "You are Normal!!"
    elif 25.0 <= bmi <= 39.9:
        return "You are Overweight!!"
    else:
        return "You are Obese!!"


def bmi_cal():
    """
    Calculates BMI based on region-specific units
    and returns BMI message and category.
    """

    # Read and normalize region input
    region = input("Are you from India/Europe or USA? : ").strip().lower()

    # Validate region first
    if region not in ("india", "europe", "usa"):
        return None, "Enter an appropriate region from the above enlisted regions!!"

    # Read weight and height (assumes valid numeric input)
    weight = float(input("Please enter your weight: "))
    height = float(input("Please enter your height: "))

    # India & Europe use kg and cm
    if region in ("india", "europe"):
        bmi = weight / (height / 100) ** 2
        category = bmi_check(bmi)

        return (
            f"Your BMI corresponding to your Weight {weight}kg and Height {height}cm is {bmi:.2f}",
            category
        )

    # USA uses lb and ft
    elif region == "usa":
        # Split height like 5.10 → 5 feet, 10 inches
        feet, inches = map(float, str(height).split("."))
        height_ft = feet + inches * 0.0833  # convert inches to feet

        # Convert lb → kg and ft → meters
        bmi = (weight * 0.45359237) / (height_ft * 0.3048) ** 2
        category = bmi_check(bmi)

        return (
            f"Your BMI corresponding to your Weight {weight}lb and Height {height}ft is {bmi:.2f}",
            category
        )


# Call the BMI calculator
bmi, category = bmi_cal()

# Display result
print(bmi)
print(category)