#include "list.h"
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int len = 0, i = 0, j = 0;
    int arr[10000];

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        arr[len] = current->n;
        current = current->next;
        len++;
    }

    for (i = 0, j = len - 1; i < j; i++, j--)
    {
        if (arr[i] != arr[j])
            return (0);
    }

    return (1);
}
