# 🎯 DLL Hijacking

---

## 🚀 One-line summary

DLL hijacking is when Windows loads an unexpected (often attacker-controlled) DLL because of the way it searches for DLLs. This repo demonstrates the concept with a tiny safe demo and explains how defenders can detect, investigate, and mitigate such abuse.


## 🧠 What is DLL Hijacking?

When an application requests a DLL (explicitly via LoadLibrary or implicitly via imports), Windows searches several locations in order to find that DLL. If an attacker can place a malicious DLL in a directory that appears earlier in that search order, the OS may load the malicious DLL instead of the legitimate one — causing the attacker's code to run inside the victim process.

This behavior is rooted in legacy compatibility and historical Windows search-order choices.

---

## 🛠️ Why this matters (defensive view)

A trusted executable can be turned into an execution vector if an unexpected DLL is placed nearby.

Attackers can avoid writing new files (or may write them temporarily) to run code under another program’s privileges.

Properly configured systems and secure coding practices can prevent most hijack scenarios.

---

## hello.c

```c
#include <windows.h>
#include <stdio.h>
int main(void) {
	HINSTANCE hDll;

	//load dll
	hDll = LoadLibrary(TEXT("lockon.dll"));

	//if dll was loaded
	if (hDll != NULL) {
		printf("DLL found..");
	} else {
		printf("DLL not found");
	}
	return 0;
}
```
---

- **LoadLibrary("lockon.dll") asks Windows to locate and load lockon.dll using the system search order.**

- **If a lockon.dll exists in a higher-priority location (e.g., the EXE's directory), Windows will load that copy.**


## dll.c

```c
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpREserved) {
	switch (dwReason)
	{
	case DLL_PROCESS_ATTACH:
		MessageBox(NULL, "Hey baby.....", "from kant", MB_ICONERROR | MB_OK);
		break;
	}
	return TRUE;
}
```

---

- **DllMain executes when the DLL is loaded. Here we show a MessageBox for visible confirmation that the DLL ran. In real incidents, attackers might run far more dangerous code —hence the need for caution.**


---


## 🔁 Detection example: Procmon filter

Filter: Operation == Load Image

Add condition: Process Name == hello.exe

Inspect Path column — if it resolves to C:\Users\... or a temp folder, investigate.

What you'll see in Procmon: when you run hello.exe with Procmon recording, you'll observe a sequence of Load Image events as Windows searches for lockon.dll across different locations — for example the application folder, the current working directory, system directories (like C:\Windows\System32), and entries in PATH. Procmon shows the attempted path in the Path column for each lookup, which makes it easy to spot if the DLL was resolved from an unexpected (user-writable) location. 🔎

---


<img width="950" height="562" alt="proc-mon" src="https://github.com/user-attachments/assets/d4077ea6-fb67-4aa5-b6c0-d87e3cdf089f" />

---

## now let's give it what it wants.........

### Compilation......

<img width="920" height="505" alt="compile-dll" src="https://github.com/user-attachments/assets/5317129c-01e9-4870-9583-269f8a66df18" />


---

<img width="925" height="326" alt="Screenshot 2025-09-25 at 10 23 54 AM" src="https://github.com/user-attachments/assets/b3078b71-72e0-43e4-ab34-08d833df046d" />


---

## Execution.

---

<img width="804" height="525" alt="executing" src="https://github.com/user-attachments/assets/a258d7f0-76e7-4cbf-a566-6f43ef5a277e" />

