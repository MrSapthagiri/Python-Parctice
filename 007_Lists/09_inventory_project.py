"""
MODULE 7.9: PRACTICAL PROJECT - INVENTORY REPORT

GOAL
Use lists of dictionaries to validate a small product inventory, calculate
stock value, filter low-stock items, and print a readable report.

SYNTAX USED
    products = [{"name": "Notebook", "quantity": 12, "price": 3.5}]
    filtered = [item for item in products if item["quantity"] < threshold]
    total = sum(item["quantity"] * item["price"] for item in products)
    ordered = sorted(products, key=lambda item: item["name"])

FLOWCHART: BUILD THE REPORT
    [Start with product records]
       |
       v
    [Validate required fields and values]
       |
       v
    [Calculate each product's stock value]
       |
       v
    [Filter products below the stock threshold]
       |
       v
    [Sort and print the summary]

Each product is a dictionary because its fields have names. The collection of
products is a list because it is ordered and can grow or shrink.
"""

from typing import TypedDict


class Product(TypedDict):
    name: str
    quantity: int
    price: float


def validate_products(products: list[Product]) -> None:
    """Raise ValueError if a product has invalid stock or price data."""
    for product in products:
        if not product["name"].strip():
            raise ValueError("Product names cannot be empty.")
        if product["quantity"] < 0:
            raise ValueError(f"{product['name']} has a negative quantity.")
        if product["price"] < 0:
            raise ValueError(f"{product['name']} has a negative price.")


def stock_value(product: Product) -> float:
    """Return the total value of one product's current stock."""
    return product["quantity"] * product["price"]


def print_inventory_report(
    products: list[Product], low_stock_threshold: int = 5
) -> None:
    """Print a sorted inventory summary and a low-stock list."""
    validate_products(products)
    ordered_products = sorted(products, key=lambda product: product["name"].lower())
    total_value = sum(stock_value(product) for product in ordered_products)
    low_stock = [
        product
        for product in ordered_products
        if product["quantity"] < low_stock_threshold
    ]

    print("INVENTORY")
    for product in ordered_products:
        print(
            f"- {product['name']}: {product['quantity']} units "
            f"at ${product['price']:.2f} each "
            f"(value ${stock_value(product):.2f})"
        )

    print(f"\nTotal stock value: ${total_value:.2f}")
    print(f"Low-stock threshold: fewer than {low_stock_threshold} units")
    if low_stock:
        for product in low_stock:
            print(f"  Restock {product['name']} ({product['quantity']} left)")
    else:
        print("  No products need restocking.")


if __name__ == "__main__":
    inventory: list[Product] = [
        {"name": "Notebook", "quantity": 12, "price": 3.50},
        {"name": "Marker", "quantity": 4, "price": 1.75},
        {"name": "Folder", "quantity": 8, "price": 2.25},
        {"name": "Pencil", "quantity": 3, "price": 0.80},
    ]
    print_inventory_report(inventory)

    # Try a negative quantity to see validation raise an explicit ValueError.
