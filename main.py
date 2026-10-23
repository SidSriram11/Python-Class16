def calculate( paid_amount , actual_price):
    balance_amount = paid_amount - actual_price

    return balance_amount

snack_price = 15

print("------Snack Vending Machine------")
print(f"The value of the snack is : ${snack_price} - per unit")
print("Accepted coins are  -  $1 , $5 , $10 , $15")
total_inserted = 0 
coins_inserted = 0

while True:
    coin = int(input("Insert a coin of  -  $1 , $5 , $10 , $15  : $"))

    if coin != 1 and coin != 5 and coin != 10 and coin != 15:
        print("Invalid coin inserted. TRY AGAIN")

        continue

    total_inserted += coin
    coins_inserted += 1

    print(f"Inserted ${coin} total coins inserted so far is {total_inserted}")

    if total_inserted >= snack_price:
        print(f"Enough money has been inserted")

        break


change_due = calculate(total_inserted , snack_price)

print(f"Dispensing your snack")

if change_due == 0:
    pass

else:
    print(f"Your change is ${change_due}")


print("=======================")
print("YOUR PURCHASE SUMMARY")
print(f"SNACK PRICE : {snack_price}")
print(f"COINS INSERTED : {coins_inserted}")
print(f"TOTAL INSERTED : ${total_inserted}")
print(f"YOUR CHANGE DUE : ${change_due}")
print("=======================")



    
