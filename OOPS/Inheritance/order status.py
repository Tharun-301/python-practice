from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5


class Order:

    def __init__(self, order_id: int, customer_name: str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status: OrderStatus = OrderStatus.PENDING

    def update_status(self, new_status: OrderStatus) -> None:
        if isinstance(new_status, OrderStatus):
            self.status = new_status
            print(f"Order {self.order_id} updated to {self.status.name}")
        else:
            raise ValueError("Invalid status!")

    def __str__(self):
        return (f"Order ID: {self.order_id}\n"
                f"Customer: {self.customer_name}\n"
                f"Status: {self.status.name}")


# Usage
order1 = Order(1001, "Tharun")
print(order1)
order1.update_status(OrderStatus.SHIPPED)
order2 = Order(1002, "Jason")
print(order2)
order2.update_status(OrderStatus.DELIVERED)