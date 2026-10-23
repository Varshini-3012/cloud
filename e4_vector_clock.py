
class Process:
    def __init__(self, pid, n):
        self.pid = pid
        self.vector = [0] * n

    def event(self):
        self.vector[self.pid] += 1
        print(f"Process {self.pid}: Event, Vector = {self.vector}")

    def send_message(self):
        self.vector[self.pid] += 1
        print(f"Process {self.pid}: Message sent, Vector = {self.vector}")
        return self.vector.copy()

    def receive_message(self, received):
        self.vector = [
            max(self.vector[i], received[i])
            for i in range(len(self.vector))
        ]
        self.vector[self.pid] += 1
        print(f"Process {self.pid}: Message received, Vector = {self.vector}")


p1 = Process(0, 2)
p2 = Process(1, 2)

p1.event()
message = p1.send_message()
p2.event()
p2.receive_message(message)
