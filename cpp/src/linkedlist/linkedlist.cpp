#include <iostream>
#include "linkedlist.hpp"


ListNode::ListNode() {}


ListNode::ListNode(int value): data(value) {}


ListNode::ListNode(int value, ListNode* next): data(value), next(next) {}


LinkedList::LinkedList(int values[], int length) {
    for (int i = 0; i < length; i++) {
        this->append(values[i]);
    }
}


void LinkedList::print() {
    ListNode *current = this->head;
    while(current != nullptr) {
        std::cout << current->data << std::endl;
        current = current->next;
    }
}


void LinkedList::values(int *values, unsigned int length) {
    ListNode *current = this->head;
    unsigned int offset = 0;
    while(current != nullptr) {
        std::copy(&(current->data), &(current->data) + 1, values + offset);
        current = current->next;
        offset++;
    }
}


void LinkedList::append(int value) {
    if (this->head == nullptr) {
        this->head = new ListNode(value);
        this->tail = this->head;
        return;
    }

    ListNode* node = new ListNode(value);
    this->tail->next = node;
    this->tail = node;
    return;
}
