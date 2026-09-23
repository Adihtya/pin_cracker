import time

# Set the secret PIN
secret_pin = input("Enter a 4-digit PIN to crack: ")

attempts = 0
start_time = time.time()

print("\nStarting brute-force attack...\n")

for number in range(10000):
    guess = f"{number:04d}"
    attempts += 1

    print(f"Trying: {guess}")

    if guess == secret_pin:
        end_time = time.time()

        print("\n" + "=" * 30)
        print("       PIN FOUND!")
        print("=" * 30)
        print(f"PIN: {guess}")
        print(f"Attempts: {attempts}")
        print(f"Time: {end_time - start_time:.4f} seconds")

        break