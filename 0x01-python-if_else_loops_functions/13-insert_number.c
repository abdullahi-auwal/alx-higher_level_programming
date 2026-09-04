#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node and a numberinto a sorted singly linked list,
 *	to a position that depends on the number passed
 * @head: pointer to the pointer to the first node
 * @number: the node data (a number)
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *nextl;
	listint_t *new;

	if (current == NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->next = NULL;
		new->n = number;
		*head = new;
		return (new);
	}
	if (number < current->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = current;
		*head = new;
		return (new);
	}
	if ((current->next) == NULL)
	{
		if ((current->n) > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->next = current;
			new->n = number;
			*head = new;
			return (new);
		}
		else
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = NULL;
			current->next = new;
			return (new);
		}
	}
	while ((current->next != NULL) && (current->next->next != NULL))
	{
		if ((current->next->n) > number)
		{
			nextl = current->next;
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			current->next = new;
			new->next = nextl;
			return (new);
		}
		current = current->next;
	}
	if (current->next->next == NULL)
	{
		if ((current->next->n) > number)
		{
			nextl = current->next;
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->next = nextl;
			current->next = new;
			new->n = number;
			return (new);
		}
		nextl = current->next;
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->next = NULL;
		nextl->next = new;
		new->n = number;
		return (new);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next = NULL;
	new->n = number;
	current->next = new;
	return (new);
}
