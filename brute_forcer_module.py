import time

user_database = {
    "admin": "secret123",
    "riya": "admin@123",
    "jiya": "test"
}

def file_based_brute_forcer(username, wordlist_file):
    print("\n[+] Starting brute-force simulation using password file...")

    correct_password = user_database.get(username)

    if not correct_password:
        print(f"[ERROR] Username '{username}' not found in system.")
        return

    try:
        with open(wordlist_file, 'r') as file:
            for line in file:
                password = line.strip()
                print(f"Trying: {username}:{password}")
                time.sleep(0.3)
                if password == correct_password:
                    print(f"[SUCCESS] Password found: {password}")
                    return
    except FileNotFoundError:
        print(f"[ERROR] Wordlist file '{wordlist_file}' not found.")

    print("[FAILED] Password not found in wordlist.")
