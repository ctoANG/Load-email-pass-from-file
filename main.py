combo = input('name of your combo file? example combo.txt : ')
def check(user, password):
    # do what ever you need here!


with open(combo) as s:
    for line in s:
        users, passwords = line.split(':')
        check(users.strip(), passwords.strip())