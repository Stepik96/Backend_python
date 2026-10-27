"""Практика 3 (слайд 35): товары, корзина, заказы и покупатели."""

from dataclasses import dataclass
from decimal import Decimal


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


class Product:
    def __init__(self, name, price, stock, category):
        if money(price) < 0 or type(stock) is not int or stock < 0:
            raise ValueError("Цена и остаток не могут быть отрицательными.")
        self.name = name
        self.price = money(price)
        self.stock = stock
        self.category = category


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def order_history(self):
        return tuple(self.orders)


class ShoppingCart:
    def __init__(self):
        self._items = {}

    @property
    def items(self):
        """Копия содержимого защищает корзину от обхода проверки количества."""
        return self._items.copy()

    def add(self, product, quantity=1):
        self._validate_quantity(quantity)
        self.update_quantity(product, self._items.get(product, 0) + quantity)

    @staticmethod
    def _validate_quantity(quantity):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError(
                "Количество должно быть положительным целым числом."
            )

    def update_quantity(self, product, quantity):
        self._validate_quantity(quantity)
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара: {product.name}.")
        self._items[product] = quantity

    def remove(self, product):
        self._items.pop(product, None)

    def clear(self):
        self._items.clear()


@dataclass(frozen=True)
class OrderItem:
    name: str
    price: Decimal
    quantity: int


class Order:
    def __init__(self, customer, cart, discount=0, tax=0):
        """Оформить заказ; discount и tax — доли, например 0.1 = 10%."""
        discount = Decimal(str(discount))
        tax = Decimal(str(tax))
        if not 0 <= discount <= 1 or not 0 <= tax <= 1:
            raise ValueError("Скидка и налог должны быть от 0 до 1.")
        products = cart.items
        if not products:
            raise ValueError("Нельзя оформить пустую корзину.")
        for product, quantity in products.items():
            if quantity > product.stock:
                raise ValueError(f"Недостаточно товара: {product.name}.")
        self.customer = customer
        # Заказ хранит снимок цен и названий на момент покупки.
        self.items = tuple(
            OrderItem(product.name, product.price, quantity)
            for product, quantity in products.items()
        )
        self.subtotal = sum(
            (item.price * item.quantity for item in self.items), Decimal("0")
        )
        self.discount_amount = money(self.subtotal * discount)
        discounted = self.subtotal - self.discount_amount
        self.tax_amount = money(discounted * tax)
        self.total = discounted + self.tax_amount
        for product, quantity in products.items():
            product.stock -= quantity
        customer.orders.append(self)
        cart.clear()


if __name__ == "__main__":
    customer = Customer("Степан", "student@example.com")
    book = Product("Учебник Python", "1000", 10, "Книги")
    pen = Product("Ручка", "50", 20, "Канцелярия")
    cart = ShoppingCart()
    cart.add(book)
    cart.add(pen, 2)
    cart.update_quantity(book, 2)
    cart.remove(pen)
    order = Order(customer, cart, discount="0.1", tax="0.2")
    print("Покупатель:", customer.name)
    for item in order.items:
        print(f"{item.name}: {item.quantity} × {item.price} руб.")
    print("Сумма:", order.subtotal, "Скидка:", order.discount_amount)
    print("Налог:", order.tax_amount, "Итого:", order.total)
    print("Заказов в истории:", len(customer.order_history()))
    print("Остаток книг на складе:", book.stock)
