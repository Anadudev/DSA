class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_list(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def append_at_after(self, data, position: int):
        new_node = Node(data)
        temp = self.head
        if not temp:
            self.head = new_node
        else:
            i = 0
            while temp:
                if i == position:
                    # print("Gotten to it")
                    new_node.next = temp.next
                    temp.next = new_node
                    return
                temp = temp.next
                i += 1
            print("Position not found in linked list")

    def delete_node(self, key):
        temp = self.head
        if not temp:
            print("List is already empty")
        else:
            while temp:
                if temp.next.data and temp.next.data == key:
                    temp.next = temp.next.next
                    self.head = temp
                    temp = None
                    return
                temp = temp.next
            

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.print_list()
    my_list.append_to_list(0)
    my_list.append_to_list(1)
    my_list.append_to_list(2)
    my_list.append_to_list(3)
    my_list.append_to_list(4)
    my_list.append_to_list(51)
    my_list.append_at_after(5, 3)
    my_list.print_list()
    print('g')
    my_list.delete_node(51)
    my_list.print_list()
