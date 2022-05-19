users = [
    (0, "Bob", "password"),
    (1, "Jose", "whatever"),
    (2, "Maria", "1234"),
]

username_mapping = {user[1]: user for user in users}

print(
    username_mapping)  # {'Bob': (0, 'Bob', 'password'), 'Jose': (1, 'Jose', 'whatever'), 'Maria': (2, 'Maria', '1234')}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct")
else:
    print("Your details are incorrect!")