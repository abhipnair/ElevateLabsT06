import string
import secrets

def knuth_shuffle(characters: str) -> str:
    chars = list(characters)
    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)

def secure_password_gen(length=16):
    if not (16 <= length <= 256):
        raise ValueError("Password length must be between 16 and 256")

    password_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_length = length - 4
    password_chars.extend(secrets.choice(all_chars) for _ in range(remaining_length))


    shuffled_password = knuth_shuffle(''.join(password_chars))
    return shuffled_password


if __name__ == "__main__":
    for _ in range(5):

        length = secrets.randbelow(23 - 16 + 1) + 16

        with open("sample_passwords.txt", "a") as pass_file:
            passwrd = secure_password_gen(length)
            pass_file.write(f"Password{_+1}: {passwrd}, length: {len(passwrd)}\n")