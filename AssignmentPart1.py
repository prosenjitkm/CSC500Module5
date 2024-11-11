class RainfallCalculator:
    def __init__(self):
        """Initialize total rainfall and months count."""
        self.totalRainfall = 0
        self.totalMonths = 0

    def isQuit(self, userInput):
        """Check if the user wants to quit the program."""
        return userInput.lower() == 'q'

    def isNumericPrompt(self, userInput):
        """Check if the user input is a valid numeric value."""
        try:
            float(userInput)
            return True
        except ValueError:
            return False

    def isPositiveNumericPrompt(self, userInput, isInteger=False):
        """Check if the user input is a positive numeric value."""
        if self.isNumericPrompt(userInput):
            value = float(userInput)
            if isInteger:
                value = int(value)
            return value > 0
        return False

    def getValidatedInput(self, prompt, isInteger=False, isPositive=True):
        """Prompt the user for input, validate it, and return the result."""
        while True:
            userInput = input(prompt)

            # Step 1: Check if the user wants to quit
            if self.isQuit(userInput):
                return None

            # Step 2: Check if the input is numeric
            if not self.isNumericPrompt(userInput):
                print("Error: You entered a non-numeric value. Please enter a valid number.")
                continue

            # Step 3: Check if the input is positive, if required
            if isPositive and not self.isPositiveNumericPrompt(userInput, isInteger):
                if isInteger:
                    print("Please enter a positive integer.")
                else:
                    print("Please enter a non-negative number.")
                continue

            # If all checks pass, return the converted input
            return int(userInput) if isInteger else float(userInput)

    def collectRainfallData(self):
        """Collects rainfall data for a specified number of years."""
        # Get the number of years
        numYears = self.getValidatedInput("Enter the number of years (or 'q' to quit): ", isInteger=True)

        # Check if the user chose to quit
        if numYears is None:
            return False  # Return False to indicate quitting

        # Outer loop for each year
        for year in range(1, numYears + 1):
            print(f"\nYear {year}")

            # Inner loop for each month (12 months in a year)
            for month in range(1, 13):
                prompt = f"Enter the inches of rainfall for month {month} (or 'q' to quit): "
                rainfall = self.getValidatedInput(prompt, isInteger=False, isPositive=True)

                # Check if the user chose to quit
                if rainfall is None:
                    return False  # Return False to indicate quitting

                # Add the rainfall to the total
                self.totalRainfall += rainfall
                self.totalMonths += 1

        return True  # Return True to indicate successful data collection

    def calculateAndDisplayResults(self):
        """Calculate the average rainfall and display the results."""
        if self.totalMonths == 0:
            print("No data to display.")
            return

        # Calculate the average rainfall per month
        averageRainfall = self.totalRainfall / self.totalMonths

        # Display the results
        print("\nResults:")
        print(f"Total number of months: {self.totalMonths}")
        print(f"Total inches of rainfall: {self.totalRainfall:.2f}")
        print(f"Average rainfall per month: {averageRainfall:.2f} inches")

    def run(self):
        """Main method to run the Rainfall Calculator."""
        # Collect data; exit if user chooses to quit
        if not self.collectRainfallData():
            print("Exiting the program. Goodbye!")
            return

        # Only display results if data collection was successful
        self.calculateAndDisplayResults()


# Run the program
if __name__ == "__main__":
    calculator = RainfallCalculator()
    calculator.run()
