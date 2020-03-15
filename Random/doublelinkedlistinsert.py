#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
def sortedInsert(head, data):
    t1= head
    p = DoublyLinkedListNode(data)

    while(t1!=None):
        if data<=t1.data and t1.prev==None:
            # insertion in begining
            p.next = t1
            p.prev = None
            t1.prev = p
            head = p
            return head
        elif t1.data<=data and t1.next==None:
            # insertion at the end
            p.next = None
            t1.next = p
            p.prev = t1
            return head
        elif t1.data<=data and data<t1.next.data:
            # insertion in the middle
            p.next = t1.next
            t1.next.prev = p
            t1.next = p
            p.prev = t1
            return head



if __name__ == '__main__':

# https://www.hackerrank.com/domains/data-structures/linked-lists