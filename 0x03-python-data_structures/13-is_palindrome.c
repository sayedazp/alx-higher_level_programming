#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to list to be checked
 * Return: either 1 or 0 determining the state of the list
 */

int is_palindrome(listint_t **head)
{
	listint_t *forw;
	int len = 0;
	int *arr;
	int i = 0;

	if (head == NULL || (*head) == NULL)
		return (1);
	forw = *head;
	while (forw != NULL)
	{
		forw = forw->next;
		len++;
	}
	arr = malloc(sizeof(int) * len);
	forw = *head;
	while (forw != NULL)
	{
		arr[i] = forw->n;
		forw = forw->next;
		i++;
	}

	if (len % 2 == 0 && arr[len / 2] != arr[(len / 2) - 1])
		return (0);
	forw = *head;
	i = 0;
	while (len - (i + 1) >= i)
	{
		if (arr[i] != arr[len - (i + 1)] || len == 2 * i)
		{
			free(arr);
			return (0);
		}
		i++;
	}
	free(arr);
	return (1);
}
