# Allows classes to be self-referential in type hints. This must occur at the
# beginning of the file.
from __future__ import annotations

class ListNode(object):
    def __init__(self, element=None) -> None:
        self.element = element
        self.next = None
        self.prev = None

    def set_next(self, next_node: ListNode):
        self.next = next_node

    def set_previous(self, prev_node: ListNode):
        self.prev = prev_node

    def set_element(self, element):
        self.element = element

    def get_next(self) -> ListNode:
        return self.next

    def get_previous(self) -> ListNode:
        return self.prev

    def get_element(self):
        return self.element


class CircularList(object):
    def __init__(self) -> None:
        self.head = ListNode(None)

        # Point the head to itself in both directions.
        self.head.set_next(self.head)
        self.head.set_previous(self.head)
        self.length = 0

    def append(self, element):
        self.insert_at(self.length, element)

    def insert_at(self, index, element):
        if index > self.length:
            err_str = 'Add index {0} out of bounds for list size {1}'
            raise IndexError(err_str.format(index, self.length))

        current_node = self.head

        for i in range(index):
            current_node = current_node.next

        new_node = ListNode(element)
        new_node.set_previous(current_node)
        new_node.set_next(current_node.get_next())
        new_node.get_next().set_previous(new_node)
        new_node.get_previous().set_next(new_node)

        self.length += 1

    def get(self, index) -> ListNode:
        if index >= self.length:
            err_str = 'Get index {0} out of bounds for list size {1}'
            raise IndexError(err_str.format(index, self.length))

        current_node = self.head.get_next()

        for i in range(index):
            current_node = current_node.get_next()

        return current_node

    def detach_node(self, drop_node: ListNode) -> ListNode:
        # Drop the current node from the attached references. It's the
        # responsibility of the caller to update the length.
        drop_node.get_previous().set_next(drop_node.get_next())
        drop_node.get_next().set_previous(drop_node.get_previous())
        drop_node.set_next(None)
        drop_node.set_previous(None)

        return drop_node

    def set_element_at(self, index, element):
        node = self.get(index)
        node.set_element(element)

    def get_element_at(self, index):
        node = self.get(index)
        return node.get_element()

    def delete_at(self, index):
        # Macro to drop without return.
        self.detach_node(self.get(index))
        self.length -= 1

    def shift_element(self, index, count):
        shift_node = self.get(index)

        if count < 0:
            abs_count = abs(count)
            for i in range(abs_count):
                self.left_shift(shift_node)
        elif count > 0:
            for i in range(count):
                self.right_shift(shift_node)

    def right_shift(self, shift_node: ListNode):
        left = shift_node.get_next()
        right = shift_node.get_next().get_next()

        # Re-attach the node one position to the right.
        detatched = self.detach_node(shift_node)
        detatched.set_previous(left)
        detatched.set_next(right)
        left.set_next(detatched)
        right.set_previous(detatched)

        # If you shift to the Nth position from the left, shift one more time.
        if right is self.head:
            self.right_shift(detatched)

    def left_shift(self, shift_node: ListNode):
        left = shift_node.get_previous().get_previous()
        right = shift_node.get_previous()

        # Re-attach the node one position to the right.
        detatched = self.detach_node(shift_node)
        detatched.set_previous(left)
        detatched.set_next(right)
        left.set_next(detatched)
        right.set_previous(detatched)

        # If you shift to the 0th position from the right, shift one more time.
        if left is self.head:
            self.left_shift(detatched)

    def zero_index(self, index):
        if index >= self.length:
            err_str = 'Zero index {0} out of bounds for list size {1}'
            raise IndexError(err_str.format(index, self.length))

        for i in range(index):
            self.right_shift(self.head)

    def get_index_of_first_occurance(self, object):
        element_found = False
        current_node = self.head.get_next()

        for index in range(self.length):
            if object == current_node.get_element():
                element_found = True
                break

            current_node = current_node.get_next()

        if element_found:
            return index

        return None







