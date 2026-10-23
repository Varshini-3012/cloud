
class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def event(self):
        self.clock += 1
        print(f"Process {self.pid}: Event, Clock = {self.clock}")

    def send_message(self):
        self.clock += 1
        print(f"Process {self.pid}: Message sent, Clock = {self.clock}")
        return self.clock

    def receive_message(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1
        print(f"Process {self.pid}: Message received, Clock = {self.clock}")


p1 = Process(1)
p2 = Process(2)

p1.event()
timestamp = p1.send_message()
p2.event()
p2.receive_message(timestamp)
