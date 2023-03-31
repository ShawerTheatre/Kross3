import ctypes

from sys import platform
if platform == "linux" or platform == "linux2":
    dll = ctypes.cdll.LoadLibrary('./MathLibrary.so')
elif platform == "win32":
    dll = ctypes.cdll.LoadLibrary('./MathLibrary.dll')

add_result = dll.add_int(4, 8)

dll.delete_float.argtypes = [ctypes.c_float, ctypes.c_float]
dll.delete_float.restype = ctypes.c_float
delete_result = dll.delete_float(10.1, 7.4)

dll.division_double.argtypes = [ctypes.c_double, ctypes.c_double]
dll.division_double.restype = ctypes.c_double
division_result = dll.division_double(2.5, 0.5)

print_result = dll.print(b"Hello world")
print(add_result)
print(delete_result)
print(division_result)
