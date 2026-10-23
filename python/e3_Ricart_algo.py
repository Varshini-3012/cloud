
class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def request_cs(self, processes):
        self.clock += 1
        timestamp = self.clock
        replies = 0

        print(f"P{self.pid} sends REQUEST at time {timestamp}")

        for p in processes:
            if p.pid != self.pid:
                p.clock = max(p.clock, timestamp) + 1
                print(f"P{p.pid} sends REPLY to P{self.pid}")
                replies += 1

        if replies == len(processes) - 1:
            print(f"P{self.pid} enters Critical Section")
            print(f"P{self.pid} exits Critical Section")
            print(f"P{self.pid} sends RELEASE\n")


processes = [Process(i) for i in range(3)]

processes[0].request_cs(processes)
processes[1].request_cs(processes)
processes[2].request_cs(processes)
