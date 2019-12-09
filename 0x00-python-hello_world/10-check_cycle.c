#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - writes the character n to stdout
 * @list: list for check the cycle
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */

int check_cycle(listint_t *list)
{
listint_t *tmp = list;

if (list == NULL)
	{
	return (0);
	}
while (tmp->next)
	{
	if (tmp->next == list)
		{
		return (1);
		}
	tmp = tmp->next;
	}
return (0);
}
