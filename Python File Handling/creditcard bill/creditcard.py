import json
import os

FILENAME = "cc.json"



def load_data():
    if not os.path.exists(FILENAME):
        return []    # no cards yet
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def add_card():
    username = input("Enter username: ")
    password = input("Enter password: ")
    ccnum = input("Enter credit card number: ")
    cclimit = int(input("Enter credit card limit: "))

    card = { 
        "username": username,
        "password": password,
        "ccnum": ccnum,
        "cclimit": cclimit,
        "outstanding": 0
    }

    data = load_data()
    data.append(card)
    save_data(data)

    print("\nCard Added Successfully ✔\n")


def display_cards():
    data = load_data()

    if not data:
        print("No credit cards found.")
        return

    print("\n--- All Credit Cards ---")
    for card in data:
        print(card)



def spend_money():
    cc = input("Enter credit card number: ")
    amount = int(input("Enter spend amount: "))

    data = load_data()

    for card in data:
        if card["ccnum"] == cc:
            if amount > (card["cclimit"] - card["outstanding"]):
                print("Limit exceeded!")
                return

            card["outstanding"] += amount
            print("Spend Successful")
            save_data(data)
            return

    print("Card not found.")



def pay_bill():
    cc = input("Enter credit card number: ")
    amount = int(input("Enter payment amount: "))

    data = load_data()

    for card in data:
        if card["ccnum"] == cc:
            if amount > card["outstanding"]:
                print("Overpayment not allowed")
                return

            card["outstanding"] -= amount
            print("Payment Successful ✔")
            save_data(data)
            return

    print("Card not found.")


def main_menu():
    

  while True:
      print("\n-------- Credit Card Management --------")
      print("1. Add Credit Card")
      print("2. Display All Cards")
      print("3. Spend Money")
      print("4. Pay Outstanding")
      print("5. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
          add_card()
      elif choice == "2":
          display_cards()
      elif choice == "3":
          spend_money()
      elif choice == "4":
          pay_bill()
      elif choice == "5":
          print("Exiting...")
          break
      else:
          print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()        
