from knoten import ListNode

class SingleLinkedList:
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return

    def outputList(self):
        "outputs the list (the value of the node, actually)"
        currentNode = self.head

        while currentNode is not None:
            print (currentNode.getData())

            # jump to the linked node
            currentNode = currentNode.getNext()
        return

    def addListitem(self, item):
        "add an item at the end of the list"

        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
            else:
                tail = self.tail
                tail.next = item
            self.tail = item
        return

    def search(self, value):
        "find node with value"
        result = False # node with value not found
        currentNode = self.head
        while currentNode is not None:
            data = currentNode.getData()
            if data == value:
                result = currentNode
                break
            else:
                currentNode = currentNode.next
        return result

