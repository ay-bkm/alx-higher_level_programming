#include <stdio.h>
#include <stddef.h>

/**
 * print_python_list_info - Prints info about Python lists
 * @p: Pointer to a Python list.
 *
 * Return: void
 */
void print_python_list_info(void *p)
{
	size_t l_size, reserved, i;
	void *l_object;


	l_size = ((size_t *)p)[-1];

	reserved = ((size_t *)p)[-3];

	printf("[*] Size of the Python List = %lu\n", l_size);
	printf("[*] reserved = %lu\n", reserved);

	for (i = 0; i < l_size; i++)
	{
		printf("Element %lu: ", i);

		l_object = ((void **)((char *)p + sizeof(size_t) * 3))[i];
		const char *type_name = "Unknown";

		if (l_object != NULL)
		{
			type_name = ((char **)l_object)[0];
		}

		printf("%s\n", type_name);
	}
}
