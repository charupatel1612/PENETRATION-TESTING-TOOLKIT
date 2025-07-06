from brute_forcer_module import file_based_brute_forcer
from port_scanner_module import range_port_scanner  # Make sure this is correct

def main():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner (Range Based)")
        print("2. Brute Force (password.txt)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter target IP (e.g., 127.0.0.1): ")
            start = int(input("Enter start port: "))
            end = int(input("Enter end port: "))
            range_port_scanner(target, start, end)

        elif choice == "2":
            username = input("Enter username: ")
            file_based_brute_forcer(username, "password.txt")

        elif choice == "3":
            print("Exiting toolkit.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
