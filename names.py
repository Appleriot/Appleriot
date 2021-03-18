from name_funtion import get_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter your first name.")
    if first == 'q':
        break
    last = input("\nEnter your last name.")
    if last == 'q':
        break

fornamted_name = get_name(first, last)
print(f"\tNeatly formatted name: {fornamted_name}.")
