#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 *
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
int y, x = 0;
int arr[1025];
listint_t *tmp = *head;

while (tmp)
	{
	arr[x] = tmp->n;
	x++;
	tmp = tmp->next;
	}
for (y = 0; y < x / 2; y++)
	if (arr[y] != arr[x])
	{
	return (1);
	}
x--;
return (0);
}
