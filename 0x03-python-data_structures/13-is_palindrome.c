#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer to the first node
 *
 * Return: 0 if its not a palindrome,
 *	1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *second_half;
	listint_t *first_half;
	listint_t *restored;

	if ((head == NULL) || (*head == NULL) || ((*head)->next == NULL))
		return (1);
	slow = *head;
	fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
		slow = slow->next;
	second_half = reverse_list(slow);

	first_half = *head;
	restored = second_half;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			reverse_list(restored);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	reverse_list(restored);
	return (1);
}


/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the first node
 *
 * Return: pointer to the new first node
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
