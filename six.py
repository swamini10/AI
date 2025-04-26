#Implement any one of the following Expert System I. Information management II. Hospitals and medical facilities III. Help desks management IV. Employee performance evaluation V. Stock market trading VI. Airline scheduling and cargo schedules.

class HelpDeskExpertSystem:
    def __init__(self):
        self.rules = {
            "printer not working": "Check if the printer is powered on and connected to the computer. Try restarting both.",
            "slow computer": "Check if there are too many programs running. Close unnecessary programs or restart the computer.",
            "email not working": "Check the internet connection. Verify the email server settings and credentials.",
            "cannot print from a specific application": "Ensure the application has the correct printer selected. Try reinstalling the printer driver for the app.",
            "password reset issue": "Check if the password reset email has arrived in your inbox or spam folder. If not, try requesting again.",
            "internet not working": "Ensure your router is powered on. Try restarting your modem and router. Check the cable connections.",
            "computer crash": "Try restarting the computer. If it happens frequently, check for hardware issues or software conflicts."
        }

    def get_solution(self, problem):
        """Provide a solution based on the given problem."""
        problem = problem.lower()  # Normalize input
        for key in self.rules:
            if key in problem:
                return self.rules[key]
        return "Sorry, I couldn't find a solution to your problem. Please contact technical support."

if __name__ == "__main__":
    print("Welcome to the Help Desk Expert System!")
    expert_system = HelpDeskExpertSystem()
    user_problem = input("Please describe your issue: ")
    solution = expert_system.get_solution(user_problem)
    print("\nSuggested Solution:")
    print(solution)
