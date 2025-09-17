# Задание 1. Создайте класс Обувь. Необходимо хранить следующую информацию:
# ■ тип обуви;
# ✓мужская,
# ✓женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Обувь и
# код для использования модели, контроллера и представления.

from controller import ShoeController
from view import ShoeView
from model import Shoe

# ===== MAIN / USAGE =====
if __name__ == "__main__":
    print("Задание №1\n-------------------------------------")
    # Создаём объект обуви
    shoe = Shoe(
        gender="женская",
        kind="туфли",
        color="черный",
        price=4500,
        manufacturer="ECCO",
        size=38
    )

    # Создаём представление и контроллер
    view = ShoeView()
    controller = ShoeController(shoe, view)

    # Использование
    controller.display_shoe()
    controller.change_price(4999)
    controller.display_shoe()

