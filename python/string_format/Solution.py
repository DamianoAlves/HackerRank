def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")
    print(f"Hello {a} {b}! You just delved into python.")


if __name__ == '__main__':
    first_name = input("Enter your name : ")
    last_name = input("Enter your last name: ")
    print_full_name(first_name, last_name)
