def username_generator(first_name, last_name):
    if len(first_name) >= 3 and len(last_name) >= 4:
        name = first_name[:3] + last_name[:4]
    else:
        name = first_name + last_name
    return name

def password_generator(username):
    password = ""
    index = -1
    for item in range(0, len(username)):
        password += username[index]
        index += 1
    return password