from typing import Optional

class Supplier:
    def __init__(self, supplier_id: int, company_name: str, phone: str):
        self.supplier_id: int = supplier_id
        self.company_name: str = company_name
        self.phone: str = phone

    def __repr__(self):
        return f"Supplier(ID={self.supplier_id}, Company='{self.company_name}')"


class Product:
    def __init__(self, sku: str, name: str, price: float, stock: int,
                 category_id: int, supplier_id: int):
        self.sku: str = sku
        self.name: str = name
        self.price: float = price
        self.stock: int = stock
        self.category_id: int = category_id
        self.supplier_id: int = supplier_id

    def __repr__(self):
        return (f"Product(SKU='{self.sku}', Name='{self.name}', "
                f"Cat_ID={self.category_id}, Supp_ID={self.supplier_id}, Stock={self.stock})")


class Category:
    def __init__(self, category_id: int, name: str, description: Optional[str] = None):
        self.category_id: int = category_id
        self.name: str = name
        self.description: Optional[str] = description

    def __repr__(self):
        return f"Category(ID={self.category_id}, Name='{self.name}')"


### usage example

if __name__ == '__main__':
    category_el = Category(category_id=1, name="Electronics", description="Consumer electronics goods")
    supplier_tech = Supplier(supplier_id=10, company_name="TechOpt", phone="555-0101")

    product = Product(
        sku="PHN001",
        name="Smartphone X10",
        price=599.99,
        stock=50,
        category_id=category_el.category_id,
        supplier_id=supplier_tech.supplier_id
    )

    print("--- product object representation")
    print(product)
    print(f"\nproduct belongs to category id: {product.category_id}")
    print(f"product supplied by supplier id: {product.supplier_id}")