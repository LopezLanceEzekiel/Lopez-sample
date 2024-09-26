# program for a bank to help determine whether a customer is eligible for a loan based on their salary and loan amount requested.
salary= float(input("amount of salary"))
loan= float(input("amount of loan requested"))

#Customer is eligible for a loan if 

mimimum_salary = 30000.00
max_loan_amount = 10 * salary


if salary < mimimum_salary:
    print("sorry, you are not elegible for a loan")


if loan > max_loan_amount:
    print("sorry, you are not eleigible for a loan")
    
else:
    print("you are eligible for a loan ")
    

#if customer is eligible ask how many months to pay and add 10% interest

months_to_pay= float(input("how many months to pay"))

loan_amount= loan * 1.10


print(loan_amount , "total loan amount")
print(loan_amount / months_to_pay)
