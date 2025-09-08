# Function to calculate total and average stock
def total_and_avg(inventory):
    if not inventory:
        return 0, 0
    total = sum(qty for _, qty in inventory)
    avg = total / len(inventory)
    return total, avg
# Function to find the item with maximum stock
def max_stock_item(inventory):
    if not inventory:
        return None, None
    # Use max with key = quantity
    max_item = max(inventory, key=lambda x: x[1])
    return max_item  # returns tuple (SKU, Quantity)
# Main menu-driven program
def main():
    inventory = []  # empty list to store products
    while True:
        print("\n===== Inventory Menu =====")
        print("1. Add Product to Inventory")
        print("2. Calculate Total and Average Stock")
        print("3. Find Maximum Stock Item")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            sku = int(input("Enter SKU number: "))
            qty = int(input("Enter Quantity: "))
            inventory.append((sku, qty))
            print(f"Product with SKU {sku} and Quantity {qty} added.")
        elif choice == '2':
            total, avg = total_and_avg(inventory)
            print(f"Inventory: {inventory}")
            print(f"Total Stock: {total}")
            print(f"Average Stock: {avg:.2f}")
        elif choice == '3':
            sku, qty = max_stock_item(inventory)
            if sku is None:
                print("Inventory is empty! Add products first.")
            else:
                print(f"Item with Maximum Stock: SKU {sku}, Quantity {qty}")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
