#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints info about Python lists
 * @p: PyObject.
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int l_size, reserved, i;
	PyObject *l_object;S

	l_size = Py_SIZE(p);
	reserved = ((PyListObject *)p)->reserved;

	printf("[*] Size of the Python List = %d\n", l_size);
	printf("[*] reserved = %d\n", reserved);

	for (i = 0; i < l_size; i++)
	{
		printf("Element %d: ", i);

		l_object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(l_object)->tp_name);
	}
}
