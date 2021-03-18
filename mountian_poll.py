repsones = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Promt for the person name and respones
    name = input("\nPlease into your name.")
    respones = input("\nWhich mountian would you like to climb?")

    # Store the repsonive in the dictinoary.
    respones[name] = repsones

    # Find out if anyone else is going to take a poll
    repeat = input("Would you like another person to respond (yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n----Poll Results----.")
for name, repsone in repsones.items():
    print(f"{name} would liek to climb {repsones}.")
