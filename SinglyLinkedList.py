class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None

class SinglyLinkedList:
    def __init__(self):
        self.head = Node()
        
    def createList(self, arr):
        currentNode = self.head
        currentNode.setData(arr[0])
        for element in arr[1:]:
            nextNode = Node()
            currentNode.setNext(nextNode)
            currentNode = nextNode
            currentNode.setData(element)
            
    def printLinkedList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.getData())
            currentNode = currentNode.getNext()
            
    def listLength(self):
        currentNode = self.head
        count = 0
        while currentNode != None:
            count += 1
            currentNode = currentNode.getNext()
            
        return count
    
    def insertElement(self, data, pos):
        currentNode = self.head
        
        if pos==0:
            newNode = Node()
            newNode.setData(data)
            newNode.setNext(currentNode)
            self.head = newNode
            
        elif pos==self.listLength():
            while pos!=1:
                currentNode = currentNode.getNext()
                pos -= 1
            newNode = Node()
            newNode.setData(data)
            currentNode.setNext(newNode)
        
        elif pos>0 and pos<self.listLength():
            while pos!=1:
                currentNode = currentNode.getNext()
                pos -= 1
                
            newNode = Node()
            newNode.setData(data)
            newNode.setNext(currentNode.getNext())
            currentNode.setNext(newNode)
            
        else:
            raise Exception("Given index is out of bounds for insertion into the list.")
        
    def insertAtBeginning(self, data):
        
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(self.head)
        self.head = newNode
        
    def insertAtEnd(self, data):
        currentNode = self.head
        
        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
            
        currentNode.setNext(Node())
        currentNode = currentNode.getNext()
        currentNode.setData(data)
        
    def deleteFromBeginning(self):
        self.head = self.head.getNext()
        
    def deleteFromEnd(self):
        currentNode = self.head
        
        for i in range(self.listLength()-2):
            currentNode = currentNode.getNext()
            
        currentNode.setNext(None)
        
    def deleteFromPos(self, pos):
        if pos==0:
            self.deleteFromBeginning()
        elif pos==self.listLength()-1:
            self.deleteFromEnd()
        elif pos>0 and pos<self.listLength()-1:
            currentNode = self.head
            ind = 0
            while ind!=pos-1:
                ind += 1
                currentNode = currentNode.getNext()
                currentNode.setNext(currentNode.getNext().getNext())
                
    def getNode(self, pos):
        ind = 0
        currentNode = self.head
        
        while ind != pos:
            currentNode = currentNode.getNext()
            ind += 1
            
        return currentNode
            