"""
Requirements:


- Users can add product
- Users can search product
- Registered User can add to cart and buy
- Users can add/delete/modify products in cart
- Users can checkout and buy items in shopping cart
- Users can rate/review any product
- Users should be able to specify the shipping address
- Users can cancel order
- Users should get notification of the order

- Actors in the system
  - Admin
  - Seller
  - Customer

- Classes Possible in the System

  - Amazon
    - Create / Add User
    - Search the Product
    - Add Product
    - Open Orders
  - Search Catalogue
    - Search by Title
  - Product
    - View Product
    - Add Product to Cart
  - Cart
    - View Cart
    - Add Quantity to any specific product
    - Add Shipping Address
    - Checkout
  - Orders Manager
    - View All Order
    - View Specific users order
  - Order
    - View Status
    - Moderators can set the status of the order
  - Notification
    - Send Notification to the user on status change of the order
"""
from enum import Enum
from abc import abstractmethod
import threading

# Enums 
class OrderStatus(Enum):
    InCart, Processed, Packed, UnderShipment, Shipped, Delivered = 1, 2, 3, 4, 5, 6


# Constants


# Address
class Address:
    def __init__(self, address, phone):
        self.__address = address
        self.__phone = phone


# Person Base Class
class Person:
    def __init__(self, email, phone, password):
        self.__email = email
        self.__phone = phone
        self.__password =password
        self.__cart = Cart()
    
    def view_profile(self):
        pass

    def reset_password(self):
        pass

    def add_to_cart(self, product):
        self.__cart.add_product(self, product)
        print("Product Added!")
        print("Go to Cart - Y/N")

        val = input().strip()
        if val == "Y" or val == "y":
            self.__cart.show_cart()
        return 



class Seller(Person):
    def __init__(self, email, phone, password, address):
        super().__init__(email, phone, password)
        self.__address = address
        self.__rating = 0
        self.__is_verified = False
        self.__is_admin = False

    def is_admin(self):
        return self.__is_admin

class Admin(Person):
    def __init__(self, email, phone, password, address):
        super().__init__(email, phone, password)
        self.__address = address
        self.__is_verified = True
        self.__is_admin = True


    def is_admin(self):
        return self.__is_admin

    
class Customer(Person):
    def __init__(self, email, phone, password, address):
        super().__init__(email, phone, password)
        self.__address = address
        self.__is_verified = False
        self.__is_admin = False

    def is_admin(self):
        return self.__is_admin

"""
  - Search Catalogue
    - Search by Title
"""
class SearchCatalogue:
    instance = None

    class __ONLY_ONE:
        def __init__(self):
            self.__title_to_product = {}
    
    def __init__(self):
        if not SearchCatalogue.instance:
            SearchCatalogue.instance = SearchCatalogue.__ONLY_ONE()
    
    @classmethod
    def add_product_by_title(cls, title, product):
        if title  not in cls.instance.__title_to_product:
            cls.instance.__title_to_product[title] = [product]
        else:
            cls.instance.__title_to_product[title].append(product)
        print("Product Added to Catalogue!\n")

    @classmethod
    def search_by_title(cls, title):
        self = cls.instance
        if title in self.__title_to_product:
            i = 1
            for prod in self.__title_to_product[title]:
                print(i)
                prod.show_banner()
                i += 1
            
            print("Enter the number of the product to view - ")

            i = int(input()) - 1
            if i < len(self.__title_to_product[title]):
                self.__title_to_product[title][i].view_product()
            else:
                print("Enter a Valid Index")
        else:
            print("No Product Found with this Title")


"""
  - Product
    - View Product
    - Add Product to Cart
"""
class Product:
    def __init__(self, product_title, product_desc, price):
        self.__product_title = product_title
        self.__product_desc = product_desc
        self.__price = price

    def view_product(self):
        print("\n\n\n")
        print(self.__product_title)
        print(self.__product_desc)
        print("\n\n", self.__price)

    def add_product_to_cart(self, member):
        member.add_to_cart(self)


"""
  - Cart
    - View Cart
    - Add Quantity to any specific product
    - Add Shipping Address
    - Checkout
"""
class Cart:
    def __init__(self):
        self.__products = []
        self.__total_value = 0
        self.__shipping_address = None

    def view_cart(self):
        print("\n\nCart\n\n")
        for order_item in self.__products:
            order_item.view_order()

        if not self.__shipping_address:
            print("\n\nAdd Shipping Address- ")
            choice = input().strip()
            if choice == "Y" or choice == "y":
                self.add_shipping_address()
        self.checkout()
    

    def add_shipping_address(self):
        print("Enter the Address")
        address = input().strip()
        print("Enter Phone number")
        phone = input().strip()

        self.__shipping_address = Address(address, phone)
        print("Shipping Address Added")


    def checkout(self):
        for order_item in self.__products:
            order_item.order(self.__shipping_address)

    def add_product(self, member, product):
        order = Order(member, product, 1, OrderStatus.InCart)
        self.__products.append(order)
        self.__total_value += product.price
        print("Product Added!")

"""
  - Orders Manager
    - View All Order
    - View Specific users order
"""
class OrderManager:
    instance = None

    class __ONLY_ONE:
        def __init__(self):
            self.__orders = []
            self.__orders_by_user = {}

    def __init__(self):
        if not OrderManager.instance:
            OrderManager.instance = OrderManager.__ONLY_ONE()
    
    def view_all_orders(self, member):
        if member.is_admin():
            for order_item in OrderManager.instance.__orders:
                order_item.view_order()
        else:
            print("Sorry you are not allowed!")

    def view_specific_order(self, member):
        if member in OrderManager.instance.__orders_by_user:
            for order_item in OrderManager.instance.__orders_by_user[member]:
                order_item.view_order()
        else:
            print("Sorry, No Orders Found")

    def add_order(self, member, order):
        OrderManager.instance.__orders.append(order)
        if member in OrderManager.instance.__orders_by_user:
            OrderManager.instance.__orders_by_user[member].append(order)
        else:
            OrderManager.instance.__orders_by_user[member] = [order]

"""
  - Order
    - View Status
    - Moderators can set the status of the order
"""
class Order:
    def __init__(self, member, product, quantity, status):
        self.__member = member
        self.__product = product
        self.__quantity = quantity
        self.__status = status
        
        # Adding Order into the orders manager
        order_manager = OrderManager()
        order_manager.add_order(member, self)

    def view_status(self):
        print(self.__status)
        return self.__status




"""
  - Amazon
    - Create / Add User
    - Search the Product
    - Add Product
    - Open Orders
"""
class Amazon:
    instance = None

    class __ONLY_ONE:
        def __init__(self):
            self.__users = []
            self.__search_catalogue = SearchCatalogue()

    def __init__(self):
        if not Amazon.instance:
            Amazon.instance = Amazon.__ONLY_ONE()
    
    @classmethod
    def add_user(cls, name, email, password):
        pass
    