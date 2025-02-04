import constants

def login():
    pass

def apply_discount(user_type):
    if user_type == 'member':
        return constants.member_discount
    elif user_type == 'new_user':
        return constants.new_user_discount
    else:
        return constants.guest_discount