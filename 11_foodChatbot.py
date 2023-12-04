class FoodOrderingChatbot:
    def __init__(self, menu):
        self.menu = menu
        self.cart = {}

    def get_response(self, user_input):
        user_input = user_input.lower()

        if "menu" in user_input:
            response = self.display_menu()
        elif "add" in user_input and "to cart" in user_input:
            response = self.add_to_cart(user_input)
        elif "cart" in user_input:
            response = self.display_cart()
        elif "place order" in user_input:
            response = self.place_order()
        elif "exit" in user_input:
            response = "Thank you for using our food ordering system. Goodbye!"
        else:
            response = "I'm sorry, I don't understand. Please ask about the menu, add items to your cart, view your cart, place an order, or exit."

        return response

    def display_menu(self):
        menu_list = "\n".join([f"{item}: ${price}" for item, price in self.menu.items()])
        return f"Our Menu:\n{menu_list}"

    def add_to_cart(self, user_input):
        words = user_input.split()
        item = " ".join(words[1:words.index("to")])
        if item in self.menu:
            if item in self.cart:
                self.cart[item] += 1
            else:
                self.cart[item] = 1
            return f"{item} added to your cart."
        else:
            return "I'm sorry, that item is not on the menu."

    def display_cart(self):
        if not self.cart:
            return "Your cart is empty."

        cart_items = "\n".join([f"{item}: {quantity} x ${self.menu[item]:.2f} = ${self.menu[item]*quantity:.2f}" for item, quantity in self.cart.items()])
        total_cost = sum([self.menu[item] * quantity for item, quantity in self.cart.items()])
        
        return f"Your Cart:\n{cart_items}\nTotal: ${total_cost:.2f}"

    def place_order(self):
        if not self.cart:
            return "Your cart is empty. Please add items before placing an order."
        total_cost = sum([self.menu[item] * quantity for item, quantity in self.cart.items()])
        self.cart = {}  # Clear the cart after placing an order
        return f"Your order has been placed. Total cost: ${total_cost:.2f}. Thank you for ordering!"

def main():
    menu = {
        "burger": 5.99,
        "pizza": 8.99,
        "salad": 3.99,
        "pasta": 7.99,
        "drink": 1.99,
    }

    chatbot = FoodOrderingChatbot(menu)

    print("Food Ordering Chatbot:")
    print("You can ask about the menu, add items to your cart, view your cart, place an order, or exit.")

    while True:
        user_input = input("You: ")

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

        if "exit" in user_input:
            break

if __name__ == "__main__":
    main()
