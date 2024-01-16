class ATM:
  def __init__(self, balance=0):
      self.balance = balance
      self.transaction_history = []

  def check_balance(self):
      return f"Your balance is ${self.balance}"

  def deposit(self, amount):
      self.balance += amount
      self.transaction_history.append(f"Deposit: +${amount}")
      return f"${amount} deposited successfully. Your new balance is ${self.balance}"

  def withdraw(self, amount):
      if amount > self.balance:
          return "Insufficient funds"
      else:
          self.balance -= amount
          self.transaction_history.append(f"Withdrawal: -${amount}")
          return f"${amount} withdrawn successfully. Your new balance is ${self.balance}"

  def get_transaction_history(self):
      return "\nTransaction History:\n" + "\n".join(self.transaction_history)

def atm_interface():
  atm = ATM()

  while True:
      print("\nATM Menu:")
      print("1. Check Balance")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Transaction History")
      print("5. Exit")

      choice = input("Enter your choice (1-5): ")

      if choice == '1':
          print(atm.check_balance())
      elif choice == '2':
          amount = float(input("Enter the deposit amount: $"))
          print(atm.deposit(amount))
      elif choice == '3':
          amount = float(input("Enter the withdrawal amount: $"))
          print(atm.withdraw(amount))
      elif choice == '4':
          print(atm.get_transaction_history())
      elif choice == '5':
          print("Exiting ATM. Thank you!")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  atm_interface()
