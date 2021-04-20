class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def getData(self):
        "method to return the value of the node"
        return self.data

    def setData(self, value):
        "method to save or modify the node value"
        self.data = value
        return

    def getNext(self):
        "method to return the node reference"
        return self.next

    def hasValue(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

    def status(self):
        "print node status"
        print("Wert:", self.getData())
        print("Link:", self.getNext())
        return
