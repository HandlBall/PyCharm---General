print("Welcome to Build Burgers. Here you build your own burger. Let's start with a bun.")
print("What bun would you like? (plain or salted)")

bun = input()

while bun != "plain" and bun != "salted":
    print("Please, pick a kind (check for misclicks)")
    bun = input()

total_cost = 0

if bun == "plain":
    total_cost += 30
if bun == "salted":
    total_cost += 32

print("Now, let's pick a kind of meat (beef, pork, chicken or fried chicken)")

meat = input()

while meat != "beef" and meat != "pork" and meat != "chicken" and meat != "fried chicken":
    print("Please, pick a kind (check for misclicks)")
    meat = input()

if meat == "beef":
    total_cost += 100
if meat == "pork":
    total_cost += 80
if meat == "chicken":
    total_cost += 79
if meat == "fried chicken":
    total_cost += 86


print("Great choice! Would you like a slice of a cheese on it? (yes or no)")

cheese_slice = input()

while cheese_slice != "yes" and cheese_slice != "no":
    print("Please, follow the instructions (check for misclicks)")
    cheese_slice = input()

if cheese_slice == "yes":
    cheese_slice_option = "with cheese slice"
elif cheese_slice == "no":
    cheese_slice_option = "without cheese slice"

if cheese_slice == "yes":
    total_cost += 20

print("Now let's pick some vegetables (yes or no)")

print("Tomatoes?")
tomatoes = input()

while tomatoes != "yes" and tomatoes != "no":
    print("Please, pick a kind (check for misclicks)")
    tomatoes = input()

if tomatoes == "yes":
    tomatoes = "tomatoes, "
if tomatoes == "no":
    tomatoes = ""

if tomatoes == "yes":
    total_cost += 10


print("Onions?")
onions = input()

while onions != "yes" and onions != "no":
    print("Please, pick a kind (check for misclicks)")
    onions = input()

if onions == "yes":
    onions = "onions, "
if onions == "no":
    onions = ""

if onions == "yes":
    total_cost += 15


print("Lettuce?")
lettuce = input()

while lettuce != "yes" and lettuce != "no":
    print("Please, pick a kind (check for misclicks)")
    lettuce = input()

if lettuce == "yes":
    lettuce = "lettuce, "
if lettuce == "no":
    lettuce = ""

if lettuce == "yes":
    total_cost += 5


print("Pickles?")
pickles = input()

while pickles != "yes" and pickles != "no":
    print("Please, pick a kind (check for misclicks)")
    pickles = input()

if pickles == "yes":
    pickles = "pickles, "
if pickles == "no":
    pickles = ""

if pickles == "yes":
    total_cost += 5


print("Would you like any addons? (bacon, jalapenos peppers, fried onions, no)")

addons = input()

while addons != "bacon" and addons != "jalapenos peppers" and addons != "fried onions" and addons != "no":
    print("Please, follow the instructions (check for misclicks)")
    addons = input()

if addons == "yes":
    addons = "addons, "
if addons == "no":
    addons = ""

if addons == "bacon":
    total_cost += 25

if addons == "jalapenos peppers":
    total_cost += 20

if addons == "fried onions":
    total_cost += 15


print("What sauces would you like? (ketchup, mayo, BBQ, hot, ranch, honey mustard)")

sauces = input()

while sauces != "ketchup" and sauces != "mayo" and sauces != "bbq" and sauces != "hot" and \
        sauces != "ranch" and sauces != "honey mustard":
    print("Please, follow the instructions (check for misclicks)")
    sauces = input()

if sauces == "ketchup":
    total_cost += 5

if sauces == "mayo":
    total_cost += 7

if sauces == "bbq":
    total_cost += 12

if sauces == "hot":
    total_cost += 9

if sauces == "ranch":
    total_cost += 12

if sauces == "honey mustard":
    total_cost += 12

final_burger = bun + " bun, " + meat + ", " + cheese_slice_option + ", " + tomatoes + onions + lettuce + pickles + addons + sauces

print("Your burger is: " + final_burger)
print(f"Your total cost is: {total_cost}Kč")
