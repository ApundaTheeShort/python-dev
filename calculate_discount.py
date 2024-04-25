

def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount = price*(discount_percent*0.01)
    new_price = price - discount
    print("The new price is: ", new_price)
  
  else:
    new_price = price
    print("The new price is: ", new_price)
    
price = float(input("Enter the Original price: "))
discount_percent = float(input("Enter the Discount: "))
final_price = calculate_discount(price, discount_percent)
