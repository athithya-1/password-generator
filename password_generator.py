import random

def generate_password(length=12):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = uppercase.lower()
    special_characters = '!@#$%^&*?+'
    numbers = '1234567890'
    all_characters = uppercase + lowercase + special_characters + numbers

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(special_characters),
        random.choice(numbers)
    ]
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    random.shuffle(password)
    return "".join(password)

print(generate_password())
