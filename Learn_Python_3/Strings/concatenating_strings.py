first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
    return first_name[0:3] + last_name[0:3]

new_account = account_generator(first_name, last_name)