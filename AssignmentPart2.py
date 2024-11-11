class BookClubPoints:
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

    def isPositiveNumericPrompt(self, userInput):
        """Check if the user input is a positive integer."""
        if self.isNumericPrompt(userInput):
            value = int(userInput)
            return value >= 0
        return False

    def getValidatedInput(self, prompt):
        """Prompt the user for input, validate it, and return the result."""
        while True:
            userInput = input(prompt)

            # Check if the user wants to quit
            if self.isQuit(userInput):
                print("Exiting the program. Goodbye!")
                return None

            # Check if the input is numeric
            if not self.isNumericPrompt(userInput):
                print("Error: You entered a non-numeric value. Please enter a valid number.")
                continue

            # Check if the input is a positive integer
            if not self.isPositiveNumericPrompt(userInput):
                print("Please enter a non-negative integer.")
                continue

            # Return the valid input as an integer
            return int(userInput)

    def calculatePoints(self, booksPurchased):
        """Calculate points based on the number of books purchased."""
        if booksPurchased < 2:
            return 0
        elif booksPurchased < 4:
            return 5
        elif booksPurchased < 6:
            return 15
        elif booksPurchased < 8:
            return 30
        else:
            return 60

    def run(self):
        """Main method to run the Book Club Points Calculator."""
        # Get the number of books purchased from the user
        booksPurchased = self.getValidatedInput("Enter the number of books you purchased this month (or 'q' to quit): ")

        # Check if the user chose to quit
        if booksPurchased is None:
            return

        # Calculate the points based on the number of books purchased
        points = self.calculatePoints(booksPurchased)

        # Display the number of points awarded
        print(f"You have earned {points} points this month.")


# Run the program
if __name__ == "__main__":
    bookClub = BookClubPoints()
    bookClub.run()
