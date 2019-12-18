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
int y, x = 0, n;
int arr[2047];
listint_t *tmp = *head;

if (!head)
	{
	return (0);
	}
while (tmp)
	{
	arr[x] = tmp->n;
	x++;
	tmp = tmp->next;
	}
n = x;
for (y = 0; y < n / 2; y++)
	{
	if (arr[y] != arr[x - 1])
	{
	return (0);
	}
x--;
	}
return (1);
}
