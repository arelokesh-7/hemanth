# Simple Python script to demonstrate basic GitHub usage

def greet_user(name):
    """
    Function to greet the user by name.
    """
    return f"Hello, {name}!"

def main():
    user_name = input("Enter your name: ")
    greeting = greet_user(user_name)
    print(greeting)

if __name__ == "__main__":
    main()
