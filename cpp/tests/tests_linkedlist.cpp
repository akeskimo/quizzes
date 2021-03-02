#include <catch2/catch.hpp>
#include "../src/linkedlist/linkedlist.cpp"


// FIXME LinkedList(int values[], unsigned int length) intialization segfault


TEST_CASE( "Linked list values are set", "[values]" ) {
    int values[5] = {1,2,3,4,5};
    int *output = new int[5];
    LinkedList *lst = new LinkedList(values, 5);
    lst->values(output, 5);

    for (int i = 0; i < 5; i++) {
        REQUIRE( output[i] == values[i] );
    }
}


TEST_CASE( "Linked list is iterable", "[values]" ) {
    int values[5] = {1,2,3,4,5};

    LinkedList *lst = new LinkedList(values, 5);

    ListNode *current = lst->head;
    unsigned int i = 0;
    while(current != nullptr) {
        REQUIRE( values[i] == current->data );
        current = current->next;
        i++;
    }
}
