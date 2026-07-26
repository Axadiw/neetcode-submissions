from dataclasses import dataclass

class BrowserNodeItem:
    url: str
    prev: BrowserNodeItem = None
    next: BrowserNodeItem = None

class BrowserHistory:

    def __init__(self, homepage: str):
        new_node = BrowserNodeItem()
        new_node.url = homepage
        self.head = new_node
        self.tail = new_node
        self.current = new_node

    # def print(self):
    #     cur = self.head
    #     ret = []
    #     while cur != None:
    #         ret.append(cur.url)
    #         cur = cur.next
        
    #     return f"{', '.join(ret)} current = {self.current.url}"

    def visit(self, url: str) -> None:
        new_node = BrowserNodeItem()
        new_node.url = url
        new_node.prev = self.current
        self.current.next = new_node
        self.tail = new_node
        self.current = new_node

        # print(f"visit {url} -> {self.print()}")

    def back(self, steps: int) -> str:
        counter = 0

        while counter < steps and self.current.prev != None:
            self.current = self.current.prev
            counter += 1
        
        # print(f"back {steps} -> {self.print()}")
        return self.current.url
        

    def forward(self, steps: int) -> str:
        counter = 0

        while counter < steps and self.current.next != None:
            self.current = self.current.next
            counter += 1
        
        # print(f"forward {steps} -> {self.print()}")
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)