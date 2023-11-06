items=[["snickers",13],["lays",1],["galaxy",3],["soap",0.5],["water",0.75]] 
basket=[]
total_sum=0
total_coupon=0
def addItem():
    found=0
    print("Available items are", items)
    item_name=input("please enter item name: ")
    for i in items:
        if i[0]==item_name:
            basket.append(i)
            found=1
            break
    if(found==0):
        print('item not found')
        
def claculateTotal():
    global total_sum
    total=0
    for i in basket:
        total+=i[1]
    total_sum=total
        
def checkTotal():
    claculateTotal()
    print("the total of your bill is ", total_sum)

def addCoupon():
    global total_coupon
    coupon_value=float(input("please enter value of coupon: "))
    total_coupon+=coupon_value

def checkout():
    global total_sum
    global total_coupon
    claculateTotal()
    print('print items are')
    for i in items:
        print(i[0], basket.count(i))
    print("the total of the order (without coupons)", total_sum)
    print("total of coupons", total_coupon)
    total_pay=total_sum-total_coupon
    if(total_pay>0):
        print("the total to pay: ", total_pay , "$")
    else:
        print("no money needed")
    
def newOrder():
  choice=100
  global basket
  basket=[]
  global total_sum
  global total_coupon
  total_sum=0
  total_coupon=0
  while choice !=4:
    print("Enter")
    print("1. to add an item")
    print("2. to check total")
    print("3. to add a coupon")
    print("4. to checkout")

    choice=int(input())

    if choice==1:
      addItem()
    elif choice ==2:
      checkTotal()
    elif choice ==3:
      addCoupon()
    elif choice ==4:
      checkout()
    else:
      print("ivalid input")
  
def mainMenu():
  choice=100
  while choice !=2:
    print("Enter")
    print("1. to start a new order")
    print("2. to close the program")
    
    choice=int(input())
    
    if choice==1:
      print("starting a new order...")
      newOrder()
    elif choice ==2:
      print("bye bye")
    else:
      print("ivalid input")


mainMenu()