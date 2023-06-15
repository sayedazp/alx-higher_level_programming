#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints python bytes information
 * @p: Python Object
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *x;
	int size, topr, i;
	char *s;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	x = (PyBytesObject *)p;
	s = x->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", s);


	if (size >= 10)
		topr = 10;
	else
		topr = size + 1;

	printf("  first %ld bytes:", topr);

	for (i = 0; i < topr; i++)
		if (s[i] >= 0)
			printf(" %02x", s[i]);
		else
			printf(" %02x", 256 + s[i]);

	printf("\n");
}

/**
 * print_python_list - Prints python list information
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	int size = ((PyVarObject *)(p))->ob_size;
	int alloc = list->allocated;
	int i = 0;
	PyObject *x;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (; i < size; i++)
	{
		x =  ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((x)->ob_type)->tp_name);
		if (PyBytes_Check(x))
			print_python_bytes(x);

	}
}
