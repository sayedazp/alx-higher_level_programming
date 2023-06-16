#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * print_dlistint - a func to print some int in doubly ll
 * @h: a pointer to the head of the linked list
 * Return: unsigned int i determining the size
 * **/
size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		i++;
	}

	return (i);
}
