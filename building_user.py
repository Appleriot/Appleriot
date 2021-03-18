def build_user(first, last, **user_info):
    """Making a dictoary for everyting we know about the user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_user('jeff', 'steven',
                          location = 'New York',
                          study = 'science')
print(user_profile)
