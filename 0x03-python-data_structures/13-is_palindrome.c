#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_listint -  reverse singly-linked list
 * @head: head node pointer
 * Return: head pointer
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: head linked list pointer
 * Return: (0) or (1)
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	{
		temp = temp->next;
	}

	if ((size % 2) == 0 && temp->n != temp->next->n)
	{
		return (0);
	}

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
		{
			return (0);
		}
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
