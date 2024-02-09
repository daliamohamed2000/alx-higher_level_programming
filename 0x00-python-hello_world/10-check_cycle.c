#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if cycle is cyclical
 * #list: pointer to list to check
 * Return: 1 if cyclical, 0 otherwise
 */

int check_cycle(listing_t *list)
{
	listing_t *x = list, *y = list;

	while (fast && fast->next)
	{
		x = x->next;
		y = y->next->next;
		if (x == y)
			return (1);
	}
	return (0);
}
