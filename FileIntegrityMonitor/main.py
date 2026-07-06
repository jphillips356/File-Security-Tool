from monitor import *

def menu():
    print("\n=== File Integrity Monitor ===")
    print("1. Create Baseline")
    print("2. Check Integrity")
    print("3. Exit")

def main():

    while True:

        menu()

        choice = input("Choice: ")

        if choice == "1":
            directory = input("Directory to monitor: ")
            create_baseline(directory)

        elif choice == "2":
            directory = input("Directory to monitor: ")
            check_integrity(directory)

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()