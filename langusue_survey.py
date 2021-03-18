from surey import AnnonymousSurevy

# Define a question, and make a surey
question = "What langues did you first speak?"
my_surey = AnnonymousSurevy(question)

# Show the question, and store repones to the question
my_surey.show_question()
print("Enter 'q' to stop.\n")
while True:
    repones = input("Langues:")
    if repones == 'q':
        break
    my_surey.store_respones(repones)

# Show the results
print("\nThank you to everyone who particated in the surevy!")
my_surey.show_results()
