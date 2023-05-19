from MyLinkedList import MyLinkedList

linked_list = MyLinkedList()

linked_list.append(7)
linked_list.append(4)
linked_list.append(10)
linked_list.append(2)
linked_list.append(10)
linked_list.append(6)

print(linked_list)
print(linked_list.get(4))
linked_list.delete(4)
print(linked_list)
