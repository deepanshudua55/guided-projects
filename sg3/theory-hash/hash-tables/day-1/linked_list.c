#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/*  
Singly Linked List Node
stores a pointer to the next node
stores a value
*/

typedef struct ListNode
{
    struct ListNode *next;
    int value;
} ListNode;

/*  
Singly Linked List
stores a pointer to the head and the tail
the size of the list
*/

typedef struct LinkedList
{
    ListNode *head;
    ListNode *tail;
    int size;
} LinkedList;

// constructor function

LinkedList *create_list(void)
{
    LinkedList *ll = malloc(sizeof(LinkedList));
    ll->head = NULL;
    ll->tail = NULL;
    ll->size = 0;

    return ll;
}

// destructor function

void free_list(LinkedList *ll)
{
    free(ll);
}

ListNode *create_node(int value, ListNode *next)
{
    ListNode *node = malloc(sizeof(ListNode));
    node->value = value;
    node->next = next;

    return node;
}

void free_node(ListNode *node)
{
    free(node);
}

// inserts at the tail of the list
void list_insert(LinkedList *ll, int value)
{
    // first, create the new node from the value
    // because this node is at the tail, it has no next pointer
    ListNode *new_node = create_node(value, NULL);

    // first, check if we have a head
    if (!ll->head)
    {
        // if a head doesn't exist
        // make our new node the head
        ll->head = new_node;
    }
    else
    {
        // if there is a head
        ll->tail->next = new_node;
    }

    // set the new node to be the tail
    ll->tail = new_node;
    // increment the size
    ll->size++;
}

// finds a value and returns it if it exists
// otherwise returns -1
int list_search(LinkedList *ll, int target)
{
    // store a variable for the current node
    ListNode *curr = ll->head;

    // while current is not null
    while (curr)
    {
        // if current is the target
        // return the value
        // otherwise set current to
        // be the next node and keep searching
        if (curr->value == target)
        {
            return curr->value;
        }
        curr = curr->next;
    }
    // if we get down here, we didn't find anything
    // so, return -1
    return -1;
}

// deletes a node if it contains the target value
// returns -1 if doesn't exist
int list_delete(LinkedList *ll, int target)
{
    // boolean for if we found the target
    bool found = false;
    // keep two pointers for previous and current
    // the previous node pointer keeps track of the
    // list node behind the one we're currently on
    // we do this because we're navigating
    // through a singly linked list and can't backtrack
    ListNode *prev = NULL;
    ListNode *curr = ll->head;

    // while curr is truthy and we haven't found
    // the target
    while (curr && !found)
    {
        if (curr->value == target)
        {
            found = true;
        }
        else
        {
            // keep searching
            // set prev to be curr
            // set curr to be curr->next
            prev = curr;
            curr = curr->next;
        }
    }
    // at this point, we've reached the end of the list
    // if curr is NULL then we've traversed the entire list
    // and found nothing
    // return -1
    if (!curr)
    {
        return -1;
    }
    // if prev is NULL, that means we stopped iterating immediately
    // so remove the head and set the next node to be the head
    if (prev == NULL)
    {
        ListNode *deleted = ll->head;
        ll->head = curr->next;
        free_node(deleted);
    }
    else
    {
        // the node isn't the head
        ListNode *deleted = curr;
        // replace next on the previous node
        // with the next node on current
        prev->next = curr->next;
        free_node(deleted);
    }
    // decrement the size
    return 0;
}

int main(void)
{

    LinkedList *ll = create_list();
    list_insert(ll, 1);
    list_insert(ll, 2);
    list_insert(ll, 3);
    printf("Should print 2: %d\n", list_search(ll, 2));
    list_delete(ll, 2);
    printf("Should print -1: %d\n", list_search(ll, 2));
    free_list(ll);

    return 0;
}