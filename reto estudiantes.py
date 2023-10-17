#https://replit.com/join/sujkrsenca-a00573991
print("what is your purchase amount")
purchase = int(input())
print("do you have a membership card?")
card = input()
if purchase >= 100:
  discount = (purchase)*.90
  print(discount)

if card == "yes" and purchase >= 100:
  discount_1 = (purchase)*.90
  discount_2 = int(discount_1)*.95
  print(discount_2)



if purchase <=100 and card == "yes":
  discount_3 = (purchase)*.95
  print(discount_3)
  
elif purchase <= 100:
  print("sorry there is no discount")
