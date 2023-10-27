import pandas as pd

# Input the name and password
Name = input("Enter Your Name: ")
Password = input("Enter Your Password: ")

# Read the user data from a CSV file
data = pd.read_csv("UserReport.csv")

# Initialize a flag to check if login is successful
login_successful = False
user_row = None

# Loop through the rows in the DataFrame
for index, row in data.iterrows():
    if row.iloc[0] == Name and row.iloc[16] == Password:
        login_successful = True
        user_row = row
        break

# Check if login was successful
if login_successful:
    print("Validated! Welcome, " + user_row.iloc[1])
else:
    print("Incorrect Username or Password. Please try again.")

print("============================================")

# Choose an option
case = int(input("Choose Option:\n1. See Utility Bill Breakdown\n2. Reduce Utilities Bill\n3. Exit\n"))

if case == 1:
    for index, row in data.iterrows():
        if row.iloc[0] == Name:
            print(user_row.iloc[1], "'s Utiliy Bills Breakdown Per Month: ")
            print("Electricity: £" + str(row.iloc[11]) + "\nWater: £" + str(row.iloc[12]) + "\nGas: £" + str(row.iloc[13])+ "\nTotal Per Month: £" + str(row.iloc[4]))

elif case == 2:
    goal = float(input("Enter the Ideal Payment For Utilities Per Month: "))
    for index, row in data.iterrows():
        if row.iloc[0] == Name:
            actual_water_cost = float(str(row.iloc[12]).replace(',', ''))  # Convert to string, remove comma, then convert to float
            actual_electric_cost = float(str(row.iloc[11]).replace(',', ''))  # Convert to string, remove comma, then convert to float
            actual_gas_cost = float(str(row.iloc[13]).replace(',', ''))  # Convert to string, remove comma, then convert to float

            ideal_water_cost = 37.3  # Average water cost per month
            ideal_electric_cost = 77.8  # Average electric cost per month
            ideal_gas_cost = 75.1  # Average gas cost per month

            water_difference = actual_water_cost- ideal_water_cost 
            electric_difference = actual_electric_cost - ideal_electric_cost
            gas_difference = actual_gas_cost-ideal_gas_cost

            print("Your current Utility Bill Per Month: £" + str(row.iloc[4]))
            total_difference = row.iloc[4] - goal

            if total_difference > 0:
                print("You can save £" + str(total_difference) + " per month on utilities.")
            else:
                print("You are currently spending £" + str(-total_difference) + " more than the ideal payment for utilities.")
            print("The Ideal Water Bill: £", water_difference)
            print("The Ideal Electric Bill: £", electric_difference)
            print("The Ideal Gas Bill: £", gas_difference)

elif case == 3:
    pass
