#include <Python.h>

static PyMethodDef NoMethods[] =
{
     {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION < 3

PyMODINIT_FUNC
init_test(void)
{
    Py_InitModule("_test", NoMethods);
}

#else

static struct PyModuleDef testmodule = {
   PyModuleDef_HEAD_INIT,
   "_test",
   NULL,
   -1,
   NoMethods
};

PyMODINIT_FUNC
PyInit__test(void)
{
    return PyModule_Create(&testmodule);
}
#endif
