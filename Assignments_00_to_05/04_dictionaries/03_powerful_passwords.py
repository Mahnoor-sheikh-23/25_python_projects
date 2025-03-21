import hashlib

# Function to generate a hashed password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Sample stored logins with hashed passwords
stored_logins = {
    "user1@example.com": hash_password("securePass123"),
    "user2@example.com": hash_password("mySecret!"),
    "admin@example.com": hash_password("admin@123")
}

# Function to verify login
def login(email: str, password_to_check: str) -> bool:
    hashed_input = hash_password(password_to_check)  # Hash user input
    return stored_logins.get(email) == hashed_input  # Compare with stored hash

# Simulating login attempts
email_input = input("Enter your email: ")
password_input = input("Enter your password: ")

if login(email_input, password_input):
    print("Login successful!")
else:
    print("Invalid credentials.")
