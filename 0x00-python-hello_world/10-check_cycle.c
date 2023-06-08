#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for a cycle in a listint_t list
 * @list: pointer to list to be checked
 * Return: an integer 0 or 1 (no cycle , tehre is a cycle)
 */

int check_cycle(listint_t *list)
{
	listint_t *needle = list;
	listint_t *tail = list;

	if (list == NULL)
	{
		return (0);
	}
	do {
		if (tail->next != NULL)
			tail = tail->next;
		else
			return (0);
		if (needle->next != NULL && needle->next->next != NULL)
			needle = needle->next->next;
		else
			return (0);
		}
	while (tail != needle);

	return (1);
}
