
class Coordinator:
    def __init__(self):
        self.locked = False

    def request(self, pid):
        print(f"Process {pid} requests access")

        if not self.locked:
            self.locked = True
            print(f"Coordinator grants access to P{pid}")
            print(f"Process {pid} enters Critical Section")
            print(f"Process {pid} exits Critical Section")
            self.release(pid)
        else:
            print(f"Process {pid} must wait")

    def release(self, pid):
        self.locked = False
        print(f"Process {pid} releases the lock\n")


coordinator = Coordinator()

coordinator.request(1)
coordinator.request(2)
coordinator.request(3)
