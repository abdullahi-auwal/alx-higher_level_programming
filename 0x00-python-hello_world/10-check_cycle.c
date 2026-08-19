#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a circle in it
 * @list: the pointer to list nodes
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr[500];
	listint_t *next = list;
	int j = 0;
	int i = 0;

	while (next != NULL)
	{
		j = 0;
		while (j != i)
		{
			if (ptr[j] == next)
				return (1);
			j++;
		}
		ptr[i] = next;
		next = next -> next;
		i++;
	}
	return (0);
}
