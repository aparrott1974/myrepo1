# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)


# run through a loop that lets teh user choose candies

for x in range(allowance):
    selected = input("which candy would you like to bring home? ")

    # add the cand at the index chosed to the candy cart list
    candyCart.append(candyList[int(selected)])

# loop through the candyCart to say what candies were brought home

print("I brought home with me ...")
for candy in candyCart:
    print(candy)
