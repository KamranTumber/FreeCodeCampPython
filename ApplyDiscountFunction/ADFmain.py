def apply_discount(price, discount):
    # 1. Check if price is an int or float (and not a boolean)
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"
    
    # 2. Check if discount is an int or float (and not a boolean)
    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
    
    # 3. Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # 4. Check if discount is between 0 and 100 (inclusive)
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # 5. Calculate and return the final price
    final_price = price - (price * (discount / 100))
    return final_price