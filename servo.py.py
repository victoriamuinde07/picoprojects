class servo:
    def __init__(self,pin):
        self.pin=pin
        print(f"servo initialized on pin{pin}")
    def goto(self,angle):
        print(f"moving servo to angle{angle}")