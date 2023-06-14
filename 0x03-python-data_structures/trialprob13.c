#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

typedef struct int_stack{
    int * arr;
    int cap;
} i_stack;

i_stack* init_stack(int size)
{
    i_stack* tmp_s;
    int* tmp_arr;

    tmp_arr = malloc(sizeof(int)*size);
    tmp_s->arr = tmp_arr;
    tmp_s->cap = 0;

    return (tmp_s);
}

int peak(i_stack *st)
{
    if (st->cap != 0)
        return st->arr[0];
    else
        return (-1);
}
int add_stack(i_stack *st, int val)
{
    st->arr[st->cap] = val;
    st->cap++;
}
int pop_stack(i_stack *st)
{
    int val;
    val = st->arr[st->cap - 1]; 
    st->arr[st->cap] = -1;
    st->cap--;

    return (val);
}

int is_palindrome(listint_t **head)
{
    listint_t *forw;
    int len = 0;
    int mid, i = 0;
    i_stack *my_s;

	if (head == NULL || (*head) == NULL || (*head)->next == NULL)
		return (1);
	forw = *head;
	while (forw != NULL)
	{
		forw = forw->next;
		len++;
	}
    my_s = init_stack(len);
	forw = *head;
    mid = len/2;
    while (forw != NULL && i < mid)
    {
        add_stack(my_s, forw->n);
        forw = forw->next;
        i++;
    }
    if (len % 2 == 0)
    {
        while(mid--)
        {
            if (pop_stack(my_s) != forw->n )
                return (-1);
            
            forw = forw->next; 
        }
    }else
    {
        forw = forw->next;
        while(mid--)
        {
            if (peak(my_s) != forw->n )
                return (-1);
            forw = forw->next; 
        }
    }
    return (1);
}