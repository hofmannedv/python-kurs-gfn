# Passwort testen, ob es zwei Kriterien erfuellt:
# - enthaelt Grossbuchstaben
# - enthaelt Kleinbuchstaben

# Passwort als String angeben
password = "pVdns1234"

is_upper = False
is_lower = False
is_number = False
is_symbol = False

for elements in password:
    if elements.isupper():
        is_upper = True
    elif elements.islower():
        is_lower = True
    elif elements.isnumeric():
        is_number = True
    elif not elements.isalpha() and not elements.isnumeric():
        is_symbol = True

if is_upper and is_lower and is_number and is_symbol:
    print("Password is correct")
if not is_number:
    print("Password needs numbers")
if not is_lower:
    print("Password needs lower cases")
if not is_upper:
    print("Password needs upper cases")
if not is_symbol:
    print("Password needs Symbols")
