#include <python.h>

/**
 * print_python_list_info - print info about py object
 * @p: A pointer to the object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
