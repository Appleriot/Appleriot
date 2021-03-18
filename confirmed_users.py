# Start ith users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'jose', 'steven']
confiremed_users = []

# Verify each user until there are no more unconfiremed users.
#  Move each verfried user into the list of confiremed users.
while unconfirmed_users:
    current_users = confiremed_users

    print(f"Verifying user: {confiremed_users.title()}")
    confiremed_users.append(current_users)
# Display all confirmed users
print("\nThe following users have been confirmed")
for confiremed_user in confiremed_users:
    print(confiremed_user.title())
