users ={
    'john': {
        'first' :'luke',
        'last' : 'pawn',
        'location': 'albma',
    },
    'chok': {
        'first': 'caiden',
        'last': 'small',
        'location': 'NC',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
