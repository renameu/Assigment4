from rent_service import RentService
from file_operations import load_from_csv
import json

def main():
    service = RentService()

    # Add users
    service.add_user("007", 50000)



    initial_data = load_from_csv("datapack.csv")
    initial_data2 = load_from_csv("datapack2.csv")
    for item in initial_data:
        service.add_stuff(item)
    for item2 in initial_data2:
        service.add_stuff(item2)

    while True:
        print("\nWelcome to Krysha.kz")
        print("\n1. List all items")
        print("2. Search for items")
        print("3. Rent an item")
        print("4. View purchase history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service.list_all_items()

        elif choice == "2":
            keyword = input("Enter a keyword to search for: ")
            found_stuff = service.search_stuff(keyword)
            if found_stuff:
                print("Found items:")
                for stuffs in found_stuff:
                    stuffs.display_info()
            else:
                print("Nothing found.")

        elif choice == "3":
            user_id = input("Enter your user_id: ")
            item_name = input("Enter the name of the item you want to rent: ")
            service.buy_item(user_id, item_name)

        elif choice == "4":
            user_id = input("Enter your id: ")
            service.view_purchase_history(user_id)

        elif choice == "5":
            print("Thank you for using our service. Good luck")
            break

        else:
            print("Error.")


if __name__ == "__main__":
    main()
