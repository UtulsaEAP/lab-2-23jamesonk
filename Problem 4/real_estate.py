#Kai Jameson
#Thursday @ 2pm

def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())

    price_change = current_price - last_month_price
    mortgage = float((current_price * 0.051) / 12)
    
    
    
    print('This house is $' + str(current_price) + '. The change is' + ' $' + str(price_change) + ' since last month.' + '\n' + 'The estimated monthly mortgage is' + ' $' + f'{mortgage:.2f}' + '.')
    # Your code goes here
if __name__ == "__main__":
    real_estate()