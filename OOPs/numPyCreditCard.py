import numpy as np

class CreditCardSystem:
    def __init__(self, customers, banks, accounts, balances, limits):
        # Store non-numeric data normally
        self.customers = np.array(customers)
        self.banks = np.array(banks)
        self.accounts = np.array(accounts)

        # Store numeric data using NumPy
        self.balances = np.array(balances, dtype=float)
        self.limits = np.array(limits, dtype=float)

    # -------------------------------
    # Charge method (vectorized)
    # -------------------------------
    def charge(self, prices):
        prices = np.array(prices)

        # Condition: allowed or not
        can_charge = (self.balances + prices) <= self.limits

        # Apply only where allowed
        self.balances = np.where(can_charge,
                                 self.balances + prices,
                                 self.balances)

        return can_charge  # Boolean array

    # -------------------------------
    # Payment method
    # -------------------------------
    def make_payment(self, amounts):
        amounts = np.array(amounts)

        # Prevent negative balance
        self.balances = np.maximum(self.balances - amounts, 0)

    # -------------------------------
    # Display method
    # -------------------------------
    def display(self):
        for i in range(len(self.customers)):
            print("Customer =", self.customers[i])
            print("Bank =", self.banks[i])
            print("Account =", self.accounts[i])
            print("Limit =", self.limits[i])
            print("Balance =", self.balances[i])
            print("----------------------------------")

    # -------------------------------
    # Check over-limit users
    # -------------------------------
    def check_over_limit(self):
        return self.balances > self.limits
    

if __name__ == "__main__":
    system = CreditCardSystem(
        ["John", "Rahul", "Anand", "Roshan"],
        ["Punjab Bank", "Indian Bank", "SBI Bank", "Punjab Bank"],
        [
            "2343 4563 0981 7789",
            "3434 4563 8888 7789",
            "8888 4563 3434 7789",
            "3434 4563 0981 8888"
        ],
        [25000, 2500, 5000, 50000],
        [5000, 1000, 2000, 3000]
    )

    # Perform multiple charges
    for val in range(1, 17):
        prices = [val, 2 * val, 3 * val, 0]
        system.charge(prices)

    # Display info
    system.display()

    # Payment loop (for first 3 users)
    for i in range(3):
        while system.balances[i] > 5000:
            system.make_payment([1000 if j == i else 0 for j in range(4)])
            print(f"New Balance of {system.customers[i]} =",
                  system.balances[i])