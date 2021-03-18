# Start with some designs that need to be printed
unprinted = ['phone case', 'case', 'stick', 'lamp']
complted_models = []
# Keeps going until all requests are done
# Move each desgin to complete when done
while unprinted:
    current_model = unprinted.pop()
    print(f'Working: {current_model}')
    complted_models.append(current_model)

# Display all models that are complete
print("\nThis model is complete:")
for done in complted_models:
    print(done)
