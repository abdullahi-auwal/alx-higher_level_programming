#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a circle in it
 * @list: the pointer to list nodes
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint *fast = list
	listint_t *slow = list;

	if (list == NULL)
		return (0);

	while ((fast != NULL) && (fast->next != NULL))
	{
		slow = slow->next;
		fast = fast->next->next;
		
		if (fast == slow)
			return (1);
	}
	return (0);
}
