# ===== CONTROLLER =====
class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_shoe(self):
        self.view.show_shoe_info(self.model)

    def change_price(self, new_price):
        old_price = self.model.price
        self.model.update_price(new_price)
        self.view.show_price_update(old_price, new_price)