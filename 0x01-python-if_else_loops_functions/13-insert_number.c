#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - adds a new node in a sorted linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *tmp;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (current->n > new->n)
	{
		tmp = current->next;
		current->next = new;
		new->next = tmp;
		return (new);

	}
	while ((current->next != NULL) && (current->next->n < new->n))
	{
		current = current->next;
	}

	tmp = current->next;
	current->next = new;
	new->next = tmp;

	return (new);
}
