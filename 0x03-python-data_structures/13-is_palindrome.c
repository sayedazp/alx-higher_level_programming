#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * flip - Reverses a singly-linked list
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *flipy(listint_t **head)
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
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to list to be checked
 * Return: either 1 or 0 determining the state of the list
 */

int is_palindrome(listint_t **head)
{
	listint_t *flip, *forw, *half;
	int len = 0;
	int i = 0;

	if (head == NULL || (*head) == NULL || (*head)->next == NULL)
		return (1);
	forw = *head;
	while (forw != NULL)
	{
		forw = forw->next;
		len++;
	}
	forw = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		forw = forw->next;

	if ((len % 2) == 0 && forw->n != forw->next->n)
		return (0);

	half = forw->next->next;
	half = flipy(&half);
	flip = half;
	forw = *head;

	while (flip)
	{
		if (forw->n != flip->n)
			return (0);
		forw = forw->next;
		flip = flip->next;
	}

	return (1);
}
