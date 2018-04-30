

# initial varible to check shopping status

shopping = 'y'

# list to track pie purchases

pie_purchases = []

# pie list

pie_list = ["pecan","apple crisp","bean","banoffee","black bun","blueberry","buko","apple","blueberry","meat"]

#message
print("welcome to the house of pies!  here are our pies: ")

while shopping == "y":  # as long as shopping remains a yes

   # for pie_name in pie_list:
    #    print("["+str(pie_list.index(pie_name)) + "]" + pie_name)  # puts square brackets around the index number of the pie
        # if you only use here up, you have an infinite loop

    print("(1)pecan","(2)apple crisp","(3)bean","(4)banoffee","(5)black bun","(6)blueberry","(7)buko","(8)apple","(9)blueberry","(10)meat")
    pie_choice = input("which would you like? ")

    #add choice to list
    pie_purchases.append(pie_choice)

    print("great! we'll have that " + pie_list[int(pie_choice) - 1] + " right out for you")

    #provide exit optoni

    shopping = input(" would you like to make another purchase?  (y or n) ")

# once the buying is done because shopping <> y
print("you purchases a total of " + str(len(pie_purchases)) + ".")