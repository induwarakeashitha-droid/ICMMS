def add_car(car_inventory):
    car_id = input("Enter car id: ").strip()

    if car_id == "":
        print("Please enter a car id")
        return

    for car in car_inventory:
        if car["car_id"] == car_id:
            print("The car id is already taken")
            return

    car_name = input("Enter car name: ").strip()
    if car_name == "":
        print("Please enter a car name")
        return

    price_input = input("Enter car price: ").strip()
    try:
        price = float(price_input)
    except ValueError:
        print("Please enter a valid price")
        return

    if price < 0:
        print("Please enter a valid price")
        return

    new_car = {"car_id": car_id, "car_name": car_name, "price": price}
    car_inventory.append(new_car)
    print(f"Added car {car_id} to car_inventory")


def display_cars(car_inventory):
    if len(car_inventory) == 0:
        print("There are no cars in car_inventory")
        return

    print(f"{'car_id':<10}{'name':<10}{'price':<10}")
    print("-" * 40)

    for car in car_inventory:
        print(f"{car['car_id']:<10} {car['car_name']:<10} {car['price']:<10.2f}")
    print()


def search_car(car_inventory):
    car_id = input("Enter car id: ").strip()

    for car in car_inventory:
        if car["car_id"] == car_id:
            print(f"Found car: {car['car_id']} | {car['car_name']} | {car['price']:.2f}")
            return car

    print("car not found")


def sort_by_price(car_inventory):
    sorted_list = car_inventory.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j]["price"] > sorted_list[j + 1]["price"]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


def sort_by_id(car_inventory):
    sorted_list = car_inventory.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j]["car_id"] < sorted_list[j + 1]["car_id"]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


def update_car(car_inventory):
    car_id = input("Enter Car ID to update: ").strip()

    for car in car_inventory:
        if car["car_id"] == car_id:
            new_name = input(f"New name (leave blank to keep '{car['car_name']}'): ").strip()
            new_price = input(f"New price (leave blank to keep {car['price']}): ").strip()

            if new_name != "":
                car["car_name"] = new_name

            if new_price != "":
                try:
                    price = float(new_price)
                    if price < 0:
                        print("Price cannot be negative, keeping old price.\n")
                    else:
                        car["price"] = price
                except ValueError:
                    print("Invalid price, keeping old price.\n")

            print("Car updated successfully.\n")
            return

    print("Car not found.\n")


def remove_car(car_inventory):
    car_id = input("Enter Car ID to remove: ").strip()

    for car in car_inventory:
        if car["car_id"] == car_id:
            confirm = input(f"Remove {car['car_name']} ({car_id})? (y/n): ").strip().lower()
            if confirm == "y":
                car_inventory.remove(car)
                print("Car removed successfully.\n")
            else:
                print("Removal cancelled.\n")
            return

    print("Car not found.\n")


def save_to_file(car_inventory):
    with open("car_data.txt", "w") as f:
        for car in car_inventory:
            f.write(f"{car['car_id']},{car['car_name']},{car['price']}\n")


def load_from_file():
    car_inventory = []
    try:
        with open("car_data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    car_id, car_name, price = parts
                    car_inventory.append({
                        "car_id": car_id,
                        "car_name": car_name,
                        "price": float(price)
                    })
    except FileNotFoundError:
        pass

    return car_inventory


def main_menu():
    car_inventory = load_from_file()

    while True:
        print("\n--- KITT ICMMS Menu ---")
        print("1. Add Car")
        print("2. View All Cars")
        print("3. Search Car by ID")
        print("4. Update Car")
        print("5. Remove Car")
        print("6. Sort by Price (Ascending)")
        print("7. Sort by Car ID (Descending)")
        print("8. Save & Exit")
        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            add_car(car_inventory)
        elif choice == "2":
            display_cars(car_inventory)
        elif choice == "3":
            search_car(car_inventory)
        elif choice == "4":
            update_car(car_inventory)
        elif choice == "5":
            remove_car(car_inventory)
        elif choice == "6":
            display_cars(sort_by_price(car_inventory))
        elif choice == "7":
            display_cars(sort_by_id(car_inventory))
        elif choice == "8":
            save_to_file(car_inventory)
            print("Records saved. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-8.\n")


main_menu()