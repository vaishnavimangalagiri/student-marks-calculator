pin = 1234
balance = 10000
user_pin = int(input("Enter your pin: "))
if user_pin == pin:
  print("Login successfull")
  print("your balance is:", balance)
  print("1. Check balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")
  choice = int(input("Enter your choice: "))
  if choice == 1:
      print("your check balance is:", balance)
  elif choice == 2:
      deposit = int(input("Enter your deposit amount: "))
      balance = balance + deposit
      print("your deposit amount is:", deposit)
  elif choice == 3:
      withdraw = int(input("Enter your withdraw amount: "))
      if withdraw <= balance:
         balance = balance - withdraw
         print("your withdraw amount is:", withdraw)
      else:
         print("Insufficient amount")
  elif choice == 4:
      print("Exit")
  else:
      print("Invalid choice")
else:
  print("Invalid pin")
