# ==========================================
#       SHOPPING CART MANAGEMENT SYSTEM
# ==========================================

products = {
    1: ("Rice", 60),
    2: ("Milk", 30),
    3: ("Bread", 40),
    4: ("Eggs", 70),
    5: ("Oil", 150),
    6: ("Sugar", 45)
}

cart = {}


def display_products():
    print("\n========== AVAILABLE PRODUCTS ==========")
    print(f"{'ID':<5}{'Product':<15}{'Price'}")
    print("-" * 35)

    for pid, (name, price) in products.items():
        print(f"{pid:<5}{name:<15}₹{price}")


def add_to_cart():
    display_products()

    pid = int(input("\nEnter Product ID: "))

    if pid not in products:
        print("❌ Invalid Product ID")
        return

    qty = int(input("Enter Quantity: "))

    if qty <= 0:
        print("❌ Quantity must be greater than 0")
        return

    if pid in cart:
        cart[pid] += qty
    else:
        cart[pid] = qty

    print("✅ Product added to cart successfully.")


def view_cart():

    if not cart:
        print("\n🛒 Your cart is empty.")
        return

    print("\n============= YOUR CART =============")
    print(f"{'Product':<15}{'Qty':<8}{'Price':<10}{'Total'}")
    print("-" * 45)

    grand_total = 0

    for pid, qty in cart.items():
        name, price = products[pid]
        total = price * qty
        grand_total += total

        print(f"{name:<15}{qty:<8}₹{price:<9}₹{total}")

    print("-" * 45)
    print(f"Grand Total : ₹{grand_total}")


def remove_product():

    if not cart:
        print("\nCart is empty.")
        return

    view_cart()

    pid = int(input("\nEnter Product ID to remove: "))

    if pid in cart:
        del cart[pid]
        print("✅ Product removed successfully.")
    else:
        print("❌ Product not found in cart.")


def checkout():

    if not cart:
        print("\n🛒 Cart is empty.")
        return

    subtotal = 0

    print("\n============= FINAL BILL =============")
    print(f"{'Product':<15}{'Qty':<8}{'Amount'}")
    print("-" * 35)

    for pid, qty in cart.items():
        name, price = products[pid]
        amount = price * qty
        subtotal += amount

        print(f"{name:<15}{qty:<8}₹{amount}")

    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    gst = (subtotal - discount) * 0.05

    final_amount = subtotal - discount + gst

    print("-" * 35)
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"Discount : ₹{discount:.2f}")
    print(f"GST (5%) : ₹{gst:.2f}")
    print(f"Final Bill: ₹{final_amount:.2f}")

    print("\n🎉 Thank you for shopping with us!")

    cart.clear()


while True:

    print("\n========== SHOPPING CART SYSTEM ==========")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Checkout")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        remove_product()

    elif choice == "5":
        checkout()

    elif choice == "6":
        print("\nThank you! Visit Again.")
        break

    else:
        print("❌ Invalid Choice.")