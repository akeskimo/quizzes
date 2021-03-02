struct ListNode {
    int data;
    ListNode *next;

    ListNode();
    ListNode(int data);
    ListNode(int data, ListNode *next);
};


class LinkedList {
public:
    LinkedList();
    LinkedList(int values[], int length);

    void append(int value);
    void values(int *values, unsigned int length);
    void print();
// private:
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
};