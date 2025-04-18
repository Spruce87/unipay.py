#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    int n = 4;
    struct Node* head = NULL;
    struct Node* current = NULL;

    for (int i = 0; i < n; i++) {
        struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
        printf("Enter Node Data : ");
        scanf("%d", &temp->data);
        temp->next = NULL;

        if (head == NULL) {
            head = temp;
            current = temp;
        } else {
            current->next = temp;
            current = temp;
        }
    }

    // Print the data of all nodes
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    // Free dynamically allocated memory
    temp = head;
    while (temp != NULL) {
        struct Node* nextNode = temp->next;
        free(temp);
        temp = nextNode;
    }

    return 0;
}
