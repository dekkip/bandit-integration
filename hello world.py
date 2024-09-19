def insecure_function():
    # Hardcoded password (Bandit will flag this)
    password = "supersecretpassword"
    print(f"The password is: {password}")

def main():
    print("Hello World!")

if __name__ == "__main__":
    insecure_function()
    main()
