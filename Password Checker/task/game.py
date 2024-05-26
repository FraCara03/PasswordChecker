import hashlib
import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Password checker with optional hash display.")
    parser.add_argument('--show-hash', action='store_true', help='Show the full hashed password in the output')
    return parser.parse_args()

def password(show_hash):
    while True:
        pw = input("Enter your password (or 'quit' or 'exit' to quit): ")
        if pw.lower() == "quit" or pw.lower() == "exit":
            print("Goodbye!")
            break
        pw_len = len(pw)
        if pw_len < 8:
            print("Your password is too short. Please enter a password of at least 8 characters.")
        else:
            hashed_pw = hashlib.sha1(pw.encode()).hexdigest().upper()
            cut_result = hashed_pw[:5]
            if show_hash:
                print(f"Your hashed password is: {hashed_pw}")
            print("Checking...")
            print(f"A request was sent to https://api.pwnedpasswords.com/range/{cut_result}")
            response = requests.get(f"https://api.pwnedpasswords.com/range/{cut_result}", headers={"Add-Padding": "True"})

            total_count = 0
            for line in response.text.splitlines():
                hash_suffix, count = line.split(':')
                if hashed_pw[5:] == hash_suffix:
                    total_count += int(count)
                    break

            if total_count > 0:
                print(f"Your password has been pwned! The password \"{pw}\" appears {total_count} times in data breaches.")
            else:
                print("Your password has not been pwned. You're good to go!")

if __name__ == "__main__":
    args = parse_args()
    password(args.show_hash)
