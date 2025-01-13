# To practice understanding of linked lists I'm
# going to make a linked list to hold onto the stones
#
# Pretty obvious this doesn't work at the larger values
# and is not the most optimized way to do this.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedStones:
    def __init__(self,value,head=None,tail=None,length=1):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append_stone(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend_stone(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get_stone(self,index):
        if index <0 or index >=self.length:
            return None
        temp = self.head
        for _ in range(0,index):
            temp = temp.next
        return temp

    def replace_stone(self,index,value):
        node = self.get_stone(index)
        node.value = value
        return True

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend_stone(value)
        if index == self.length:
            return self.append_stone(value)
        new_node = Node(value)
        temp = self.head
        for _ in range(0,index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def do_blink(self,node):
        stone = node.value
        #print(f'Stone Val: {stone}, Length: {len(stone) % 2}')
        if stone == '0':
            node.value = '1'
            return False
        # If stone is engraved with the number 0, replaced by 1
        # If the stone is even, replaced by 2 stones LH and RH
        elif len(stone) % 2 == 0:
            size = len(stone)//2
            new_1 = int(stone[:size])
            new_2 = int(stone[size:])
            #print(f'{stone} - 1: {new_1} and 2: {new_2}')
            node.value = str(new_1)
            new_node = Node(str(new_2))
            new_node.next = node.next
            node.next = new_node
            self.length += 1
            return True
        # Else stone is replace by new stone - old x 2024
        else:
            new = int(stone) * 2024
            #print(f'New {new}')
            node.value = str(new)
            return False

    def blink(self):
        temp = self.head
        for _ in range(0,self.length):
            if self.do_blink(temp):
                temp = temp.next
            temp = temp.next

    def split_stones(self):
        new_len = self.length//2
        temp = self.head
        new_stones = LinkedStones(self.head.value)
        for _ in range(0,new_len):
            temp = temp.next
            new_stones.append_stone(temp.value)
            self.length -= 1
        self.head = temp
        return new_stones

    def print_stones(self):
        temp = self.head
        printer = ""
        while temp is not None:
            printer += f'{temp.value} '
            temp = temp.next
        print(printer)

#Example
stones = LinkedStones('125')
stones.append_stone('17')
#stones.print_stones()
#print()
for _ in range(0,25):
    stones.blink()
    #stones.print_stones()
print(stones.length)
print()
#27 10647 103 9 0 5524 4594227 902936
input = [10647,103,9,0,5524,4594227,902936]
stones2 = LinkedStones('27')
for i in input:
    stones2.append_stone(str(i))
stones2.print_stones()
j = 0
for _ in range(0,40):
    stones2.blink()
    print(f'at {j} = {stones2.length}')
    j+=1
print(stones2.length)
