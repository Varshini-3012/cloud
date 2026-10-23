
class TokenRing:
    def __init__(self, n):
        self.n = n
        self.token = 0

    def execute(self):
        for i in range(self.n):
            pid = self.token
            print(f"Token passed to Process {pid}")
            print(f"Process {pid} enters Critical Section")
            print(f"Process {pid} exits Critical Section")
            self.token = (self.token + 1) % self.n


ring = TokenRing(4)
ring.execute()


#  multiple processes arranged in a circular manner, with a single token circulating between them


import time

n = int(input("Enter number of processes: "))

if n <= 0:
    print("Number of processes must be greater than 0.")
    exit()

processes = list(range(1, n + 1))
token_holder = 0

print("\nToken Ring Algorithm")
print("Type 'exit' anytime to stop the simulation.")

for _ in range(2 * n):
    process = processes[token_holder]

    print(f"\nToken is with Process {process}")

    choice = input(
        f"Should Process {process} enter critical section? (y/n): "
    ).lower()

    if choice == "exit":
        print("Token Ring simulation stopped.")
        break

    elif choice == "y":
        print(f"Process {process} enters critical section.")
        print(f"Process {process} exits critical section.")

    else:
        print(f"Process {process} skips the critical section.")

    token_holder = (token_holder + 1) % n
    print(f"Token passed to Process {processes[token_holder]}")
    time.sleep(1)

else:
    print("\nToken Ring simulation completed.")
