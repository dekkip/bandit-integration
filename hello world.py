import os

def insecure_function():
    # Hardcoded password (Bandit will flag this)
    password = "supersecretpassword"
    print(f"The password is: {password}")

def main():
    # Use of os.system (Bandit will flag this)
    os.system('echo Hello, World!')
    print("Good morning, World!")

if __name__ == "__main__":
    insecure_function()
    main()
