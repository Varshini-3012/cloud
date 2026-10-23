
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
