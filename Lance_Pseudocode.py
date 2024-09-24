first=input("Enter the amount of your first purchase:")
second=input("Enter the amount of your second purchase:")
third=input("Enter the amount of your third purchase:")
total= float(first) + float(second) + float(third)

remo

if total < 100:
    discount=total *0.1
    new_total=total-discount 
    print("You are qualified for a discount")
    print("New total:" ,new_total)
    
else:
    new_total=total
    print("No discount. Total remains unchanged.")
    
loyalty_points=new_total *0.1
print("Loyalty points earned:" , loyalty_points) 
payment=float(input("Enter your payment:"))

if payment>=new_total:
    change=payment-new_total
    print("Change given:" , change)
    
else:
    print("Insufficent payment")