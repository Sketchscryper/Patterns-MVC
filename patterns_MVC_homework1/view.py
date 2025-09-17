# ===== VIEW =====
class ShoeView:
    def show_shoe_info(self, shoe):
        print("=== Информация об обуви ===")
        print(shoe)
        print("===========================")

    def show_price_update(self, old_price, new_price):
        print(f"Цена обновлена: была {old_price} руб., стала {new_price} руб.")
