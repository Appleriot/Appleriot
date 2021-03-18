avabible_toppings = ['mushroom', 'green peppers', 'peperio', 'air']
toppings = ['mushroom', 'game', 'air']

for topping in toppings:
    if topping in avabible_toppings:
        print("Sorry, Not other toppings")
    else:
        print(f"Adding {toppings}.")

print("\nFinsihed making your pizza")
