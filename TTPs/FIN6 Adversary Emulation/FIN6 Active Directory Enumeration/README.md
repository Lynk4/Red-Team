# FIN6 - Active Directory Enumeration

---

```bash
meterpreter > sysinfo
Computer        : TARGETDC
OS              : Windows Server 2019 (10.0 Build 17763).
Architecture    : x64
System Language : en_US
Domain          : MAD
Logged On Users : 13
Meterpreter     : x86/windows
meterpreter > load powershell
Loading extension powershell...Success.
meterpreter > powershell_shell
PS > pwd

Path
----
C:\Windows\system32


PS > cd C:\Users\Public
PS > pwd

Path
----
C:\Users\Public


PS >  
```

<img width="1440" height="677" alt="Screenshot 2025-07-22 at 10 19 54 PM" src="https://github.com/user-attachments/assets/67d0dff6-6a4b-4ea6-8f70-04081ecc42f9" />


---

## ACCOUNT DISCOVERY, DOMAIN ACCOUNT

```bash
C:\Users\Public


PS > dir


    Directory: C:\Users\Public


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        6/24/2020  11:10 AM                Documents
d-r---        9/15/2018  12:19 AM                Downloads
d-r---        9/15/2018  12:19 AM                Music
d-r---        12/1/2021  10:53 PM                Pictures
d-----        12/1/2021  10:58 PM                PowerSploit
d-r---        9/15/2018  12:19 AM                Videos
-a----       11/12/2021   6:10 AM           2728 add-domain-entities.ps1
-a----       11/12/2021   6:10 AM            718 create-domain.ps1
-a----       11/12/2021   6:10 AM           1909 disable-defender.ps1
-a----        4/19/2022  10:57 PM           4890 enable-PSlogging.ps1
-a----       11/12/2021   6:10 AM            216 hidden-files.ps1
-a----       11/12/2021   6:10 AM           3413 install-tools.ps1
-a----        12/1/2021  11:23 PM           8192 NTUSER.DAT
-a----       11/12/2021   6:10 AM            183 rename-dc.ps1
-a----       11/12/2021   6:10 AM           1301 set-windows-wallpaper.ps1
-a----       11/12/2021   6:10 AM           6523 setup-dc.ps1
-a----        12/1/2021  10:53 PM           1751 SetupDC.xml


PS > adfind.exe -f "objectcategory=person" > ad_users.txt
PS > type ad_users.txt  
Using server: targetDC.MAD.local:389
Directory: Windows Server 2019 (10.0.17763.1)
Base DN: DC=MAD,DC=local

dn:CN=Administrator,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Administrator
>description: Built-in account for administering the computer/domain
>distinguishedName: CN=Administrator,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20250409174152.0Z
>uSNCreated: 8196
>memberOf: CN=Group Policy Creator Owners,CN=Users,DC=MAD,DC=local
>memberOf: CN=Domain Admins,CN=Users,DC=MAD,DC=local
>memberOf: CN=Enterprise Admins,CN=Users,DC=MAD,DC=local
>memberOf: CN=Schema Admins,CN=Users,DC=MAD,DC=local
>memberOf: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 86064
>name: Administrator
>objectguid: {EA023A06-E8EB-4F83-9A94-29C7B7A42437}
>userAccountControl: 512
>badPwdCount: 3
>codePage: 0
>countryCode: 0
>badPasswordTime: 133886940394057156
>lastLogoff: 0
>lastLogon: 132829032669411365
>logonHours: FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FF
>pwdLastSet: 133886941128506269
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-500
>adminCount: 1
>accountExpires: 0
>logonCount: 12
>sAMAccountName: Administrator
>sAMAccountType: 805306368
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101181216.0Z
>lastLogonTimestamp: 132829032319083815

dn:CN=Guest,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Guest
>description: Built-in account for guest access to the computer/domain
>distinguishedName: CN=Guest,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8197
>memberOf: CN=Guests,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 8197
>name: Guest
>objectguid: {DE344362-E24B-4095-91DF-63A9F492EC78}
>userAccountControl: 66082
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>pwdLastSet: 0
>primaryGroupID: 514
>objectsid: S-1-5-21-2680507893-677197679-1321753512-501
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: Guest
>sAMAccountType: 805306368
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=cloudbase-init,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: cloudbase-init
>distinguishedName: CN=cloudbase-init,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202073855.0Z
>displayName: cloudbase-init
>uSNCreated: 8198
>memberOf: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 20513
>name: cloudbase-init
>objectguid: {772F9DEE-4FCD-49F2-AA6B-ADF7B30A08C8}
>userAccountControl: 66048
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 132829020110053038
>pwdLastSet: 132829020109587150
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1000
>adminCount: 1
>accountExpires: 9223372036854775807
>logonCount: 10
>sAMAccountName: cloudbase-init
>sAMAccountType: 805306368
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Admin,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Admin
>distinguishedName: CN=Admin,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20250409174143.0Z
>displayName: Admin
>uSNCreated: 8199
>memberOf: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 86062
>name: Admin
>objectguid: {B03FA6E0-20F4-4C02-9E1E-77E7C81A500A}
>userAccountControl: 66048
>badPwdCount: 3
>codePage: 0
>countryCode: 0
>badPasswordTime: 133886940202495399
>lastLogoff: 0
>lastLogon: 132828923537642995
>logonHours: FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FF
>pwdLastSet: 133886941035064994
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1001
>adminCount: 1
>accountExpires: 0
>logonCount: 2
>sAMAccountName: Admin
>sAMAccountType: 805306368
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=krbtgt,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: krbtgt
>description: Key Distribution Center Service Account
>distinguishedName: CN=krbtgt,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12324
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>uSNChanged: 20526
>showInAdvancedViewOnly: TRUE
>name: krbtgt
>objectguid: {FB68DFE5-CCC8-4896-A6C7-DBD1B90034B1}
>userAccountControl: 514
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>pwdLastSet: 132829027304606894
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-502
>adminCount: 1
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: krbtgt
>sAMAccountType: 805306368
>servicePrincipalName: kadmin/changepw
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z
>msDS-SupportedEncryptionTypes: 0

dn:CN=Jeniffer Tarantino,OU=Managers,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Jeniffer Tarantino
>sn: Tarantino
>givenName: Jennifer
>distinguishedName: CN=Jeniffer Tarantino,OU=Managers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12807
>uSNChanged: 12811
>name: Jeniffer Tarantino
>objectguid: {A20000E8-3136-410C-BF30-18BA73CB9F63}
>userAccountControl: 512
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>pwdLastSet: 132829032967341903
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1108
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: jtarantino
>sAMAccountType: 805306368
>userPrincipalName: jtarantino@MAD.local
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 16010101000000.0Z

dn:CN=Donald Dougherty,OU=HR,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Donald Dougherty
>sn: Dougherty
>givenName: Donald
>distinguishedName: CN=Donald Dougherty,OU=HR,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12813
>uSNChanged: 12817
>name: Donald Dougherty
>objectguid: {99DC4AEE-51B3-496F-BA6E-63E649180E2E}
>userAccountControl: 512
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>pwdLastSet: 132829032967970190
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1109
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: ddougherty
>sAMAccountType: 805306368
>userPrincipalName: ddougherty@MAD.local
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 16010101000000.0Z

dn:CN=Evelyn Gismond,OU=UserAccounts,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Evelyn Gismond
>sn: Gismond
>givenName: Evelyn
>distinguishedName: CN=Evelyn Gismond,OU=UserAccounts,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12819
>uSNChanged: 12823
>name: Evelyn Gismond
>objectguid: {FE2530FA-45C6-4600-B8F0-2A326407F202}
>userAccountControl: 512
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>pwdLastSet: 132829032968624094
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1110
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: egismond
>sAMAccountType: 805306368
>userPrincipalName: egismond@MAD.local
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 16010101000000.0Z

dn:CN=Shanon Blue,OU=UserAccounts,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: Shanon Blue
>sn: Blue
>givenName: Shanon
>distinguishedName: CN=Shanon Blue,OU=UserAccounts,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12825
>uSNChanged: 12829
>name: Shanon Blue
>objectguid: {B6905977-DA30-484F-9AE0-B885D42CB2CD}
>userAccountControl: 512
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>pwdLastSet: 132829032969167443
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1111
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: sblue
>sAMAccountType: 805306368
>userPrincipalName: sblue@MAD.local
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 16010101000000.0Z

dn:CN=madAdmin,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>cn: madAdmin
>distinguishedName: CN=madAdmin,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072137.0Z
>whenChanged: 20250721184237.0Z
>uSNCreated: 12832
>memberOf: CN=Domain Admins,CN=Users,DC=MAD,DC=local
>memberOf: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 106553
>name: madAdmin
>objectguid: {02175115-8ABC-4890-B04E-ECD42A181E4D}
>userAccountControl: 66048
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 133975947351849471
>lastLogoff: 0
>lastLogon: 133977011104199607
>logonHours: FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF FF
>pwdLastSet: 133975959589499865
>primaryGroupID: 513
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1112
>adminCount: 1
>accountExpires: 0
>logonCount: 57
>sAMAccountName: madAdmin
>sAMAccountType: 805306368
>objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 16010101000000.0Z
>lastLogonTimestamp: 133975948176744839


10 Objects returned
PS >
```

---

<img width="1440" height="783" alt="Screenshot 2025-07-22 at 10 25 07 PM" src="https://github.com/user-attachments/assets/0450e433-f063-44d8-840b-dec2257a7d21" />

---

```bash
PS > net user /domain > net_users_net.txt
PS > type net_users_net.txt

User accounts for \\TARGETDC

-------------------------------------------------------------------------------
Admin                    Administrator            cloudbase-init
ddougherty               egismond                 Guest
jtarantino               krbtgt                   madAdmin
sblue
The command completed successfully.

PS > 
```


<img width="1018" height="396" alt="Screenshot 2025-07-22 at 10 27 35 PM" src="https://github.com/user-attachments/assets/2eab5e66-7004-48f8-a382-3c43f0b1ccdc" />

---

## REMOTE SYSTEM DISCOVERY

```bash
PS > adfind.exe -f "objectcategory=computer" > ad_computers.txt
PS > type ad_computers.txt    

AdFind V01.57.00cpp Joe Richards (support@joeware.net) November 2021

Using server: targetDC.MAD.local:389
Directory: Windows Server 2019 (10.0.17763.1)
Base DN: DC=MAD,DC=local

dn:CN=TARGETDC,OU=Domain Controllers,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>objectClass: computer
>cn: TARGETDC
>distinguishedName: CN=TARGETDC,OU=Domain Controllers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20250721180357.0Z
>uSNCreated: 12293
>uSNChanged: 106527
>name: TARGETDC
>objectguid: {88269BEF-1398-4758-B3DE-559F1B565643}
>userAccountControl: 532480
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 133977002572360323
>localPolicyFlags: 0
>pwdLastSet: 133975946260858037
>primaryGroupID: 516
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1002
>accountExpires: 9223372036854775807
>logonCount: 58
>sAMAccountName: TARGETDC$
>sAMAccountType: 805306369
>operatingSystem: Windows Server 2019 Standard
>operatingSystemVersion: 10.0 (17763)
>serverReferenceBL: CN=TARGETDC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=MAD,DC=local
>dNSHostName: targetDC.MAD.local
>rIDSetReferences: CN=RID Set,CN=TARGETDC,OU=Domain Controllers,DC=MAD,DC=local
>servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/targetDC.MAD.local
>servicePrincipalName: ldap/targetDC.MAD.local/ForestDnsZones.MAD.local
>servicePrincipalName: ldap/targetDC.MAD.local/DomainDnsZones.MAD.local
>servicePrincipalName: TERMSRV/TARGETDC
>servicePrincipalName: TERMSRV/targetDC.MAD.local
>servicePrincipalName: DNS/targetDC.MAD.local
>servicePrincipalName: GC/targetDC.MAD.local/MAD.local
>servicePrincipalName: RestrictedKrbHost/targetDC.MAD.local
>servicePrincipalName: RestrictedKrbHost/TARGETDC
>servicePrincipalName: RPC/c343d89b-ebc9-4863-8913-2ebce172730d._msdcs.MAD.local
>servicePrincipalName: HOST/TARGETDC/MAD
>servicePrincipalName: HOST/targetDC.MAD.local/MAD
>servicePrincipalName: HOST/TARGETDC
>servicePrincipalName: HOST/targetDC.MAD.local
>servicePrincipalName: HOST/targetDC.MAD.local/MAD.local
>servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/c343d89b-ebc9-4863-8913-2ebce172730d/MAD.local
>servicePrincipalName: ldap/TARGETDC/MAD
>servicePrincipalName: ldap/c343d89b-ebc9-4863-8913-2ebce172730d._msdcs.MAD.local
>servicePrincipalName: ldap/targetDC.MAD.local/MAD
>servicePrincipalName: ldap/TARGETDC
>servicePrincipalName: ldap/targetDC.MAD.local
>servicePrincipalName: ldap/targetDC.MAD.local/MAD.local
>objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z
>lastLogonTimestamp: 133975946375676273
>msDS-SupportedEncryptionTypes: 28
>msDFSR-ComputerReferenceBL: CN=TARGETDC,CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=MAD,DC=local

dn:CN=WKST01,CN=Computers,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>objectClass: computer
>cn: WKST01
>distinguishedName: CN=WKST01,CN=Computers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12782
>uSNChanged: 12786
>name: WKST01
>objectguid: {3A8CDE02-B28F-4F6A-B7BA-91D2FD51B191}
>userAccountControl: 4096
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>localPolicyFlags: 0
>pwdLastSet: 132829032963010319
>primaryGroupID: 515
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1105
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: WKST01$
>sAMAccountType: 805306369
>objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: FALSE
>dSCorePropagationData: 16010101000000.0Z

dn:CN=WKST02,CN=Computers,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>objectClass: computer
>cn: WKST02
>distinguishedName: CN=WKST02,CN=Computers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12788
>uSNChanged: 12792
>name: WKST02
>objectguid: {85DF32E9-95FD-4D79-8BA4-606E0E10EF0B}
>userAccountControl: 4096
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>localPolicyFlags: 0
>pwdLastSet: 132829032964346618
>primaryGroupID: 515
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1106
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: WKST02$
>sAMAccountType: 805306369
>objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: FALSE
>dSCorePropagationData: 16010101000000.0Z

dn:CN=WKST03,CN=Computers,DC=MAD,DC=local
>objectClass: top
>objectClass: person
>objectClass: organizationalPerson
>objectClass: user
>objectClass: computer
>cn: WKST03
>distinguishedName: CN=WKST03,CN=Computers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12794
>uSNChanged: 12798
>name: WKST03
>objectguid: {C214BDC4-784F-4864-98F8-D2572FC3040B}
>userAccountControl: 4096
>badPwdCount: 0
>codePage: 0
>countryCode: 0
>badPasswordTime: 0
>lastLogoff: 0
>lastLogon: 0
>localPolicyFlags: 0
>pwdLastSet: 132829032965030780
>primaryGroupID: 515
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1107
>accountExpires: 9223372036854775807
>logonCount: 0
>sAMAccountName: WKST03$
>sAMAccountType: 805306369
>objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: FALSE
>dSCorePropagationData: 16010101000000.0Z


4 Objects returned
PS > 
```
<img width="1440" height="788" alt="Screenshot 2025-07-22 at 10 34 17 PM" src="https://github.com/user-attachments/assets/5d665b81-1dcc-47cd-9429-fe6c7851d6f1" />

---

```bash
PS > 
PS > net group "Domain Computers" /domain > ad_computers_net.txt
PS > type ad_computers_net.txt
Group name     Domain Computers
Comment        All workstations and servers joined to the domain

Members

-------------------------------------------------------------------------------
WKST01$                  WKST02$                  WKST03$
The command completed successfully.

PS > 
```


<img width="1437" height="283" alt="Screenshot 2025-07-22 at 10 36 36 PM" src="https://github.com/user-attachments/assets/9658b4ac-2733-4017-9ea0-c6ab0f971216" />

---

## DOMAIN TRUST DISCOVERY
### Enumerating OU

```bash
PS > adfind.exe -f "objectcategory=organizationalUnit" > ad_ous.txt
PS > type ad_ous.txt

AdFind V01.57.00cpp Joe Richards (support@joeware.net) November 2021

Using server: targetDC.MAD.local:389
Directory: Windows Server 2019 (10.0.17763.1)
Base DN: DC=MAD,DC=local

dn:OU=Domain Controllers,DC=MAD,DC=local
>objectClass: top
>objectClass: organizationalUnit
>ou: Domain Controllers
>description: Default container for domain controllers
>distinguishedName: OU=Domain Controllers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 5804
>uSNChanged: 5804
>showInAdvancedViewOnly: FALSE
>name: Domain Controllers
>objectguid: {DF4849C2-9D7C-469B-B027-964EFAF935AF}
>systemFlags: -1946157056
>objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>gPLink: [LDAP://CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=MAD,DC=local;0]
>dSCorePropagationData: 20211202072136.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:OU=Managers,DC=MAD,DC=local
>objectClass: top
>objectClass: organizationalUnit
>ou: Managers
>distinguishedName: OU=Managers,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12799
>uSNChanged: 12801
>name: Managers
>objectguid: {974C1E17-4299-4BA1-AAE1-39409502E781}
>objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 20211202072136.0Z
>dSCorePropagationData: 20211202072136.0Z
>dSCorePropagationData: 16010101000000.0Z

dn:OU=HR,DC=MAD,DC=local
>objectClass: top
>objectClass: organizationalUnit
>ou: HR
>distinguishedName: OU=HR,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12802
>uSNChanged: 12803
>name: HR
>objectguid: {30B3356C-5D90-4D63-A68D-CDF1412ECA56}
>objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 20211202072136.0Z
>dSCorePropagationData: 16010101000000.0Z

dn:OU=UserAccounts,DC=MAD,DC=local
>objectClass: top
>objectClass: organizationalUnit
>ou: UserAccounts
>distinguishedName: OU=UserAccounts,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202072136.0Z
>whenChanged: 20211202072136.0Z
>uSNCreated: 12804
>uSNChanged: 12805
>name: UserAccounts
>objectguid: {2942CA99-12A4-4ED1-A2D2-E5EB6CBAEB60}
>objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 20211202072136.0Z
>dSCorePropagationData: 16010101000000.0Z


4 Objects returned
PS >

```
<img width="1440" height="781" alt="Screenshot 2025-07-22 at 10 40 22 PM" src="https://github.com/user-attachments/assets/1f155e25-041a-451e-a3cb-151c49988f7b" />


---

```bash
PS > Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name, DistinguishedName -A > ad_ous_ps.txt
PS > type ad_ous_ps.txt

Name               DistinguishedName
----               -----------------
Domain Controllers OU=Domain Controllers,DC=MAD,DC=local
Managers           OU=Managers,DC=MAD,DC=local
HR                 OU=HR,DC=MAD,DC=local
UserAccounts       OU=UserAccounts,DC=MAD,DC=local


PS > 
```

<img width="1440" height="348" alt="Screenshot 2025-07-22 at 10 46 51 PM" src="https://github.com/user-attachments/assets/caef78ba-ef20-4d72-9e01-c8ef4d76303b" />


```bash
PS > adfind.exe -subnets -f "objectcategory=subnet" > ad_subnet.txt

PS > Get-ADReplicationSubnet -Filter * > ad_subnets_ps.txt

```


---


```bash
PS > adfind.exe -f "objectcategory=group" > ad_group.txt
PS > type ad_group.txt

AdFind V01.57.00cpp Joe Richards (support@joeware.net) November 2021

Using server: targetDC.MAD.local:389
Directory: Windows Server 2019 (10.0.17763.1)
Base DN: DC=MAD,DC=local

dn:CN=Administrators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Administrators
>description: Administrators have complete and unrestricted access to the computer/domain
>member: CN=madAdmin,CN=Users,DC=MAD,DC=local
>member: CN=Domain Admins,CN=Users,DC=MAD,DC=local
>member: CN=Enterprise Admins,CN=Users,DC=MAD,DC=local
>member: CN=Admin,CN=Users,DC=MAD,DC=local
>member: CN=cloudbase-init,CN=Users,DC=MAD,DC=local
>member: CN=Administrator,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 8201
>uSNChanged: 20520
>name: Administrators
>objectguid: {2BC82A2C-819D-487B-AAE4-07170DED7F59}
>objectsid: S-1-5-32-544
>adminCount: 1
>sAMAccountName: Administrators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Users,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Users
>description: Users are prevented from making accidental or intentional system-wide changes and can run most applications
>member: CN=Domain Users,CN=Users,DC=MAD,DC=local
>member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=MAD,DC=local
>member: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=MAD,DC=local
>distinguishedName: CN=Users,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 8206
>uSNChanged: 12381
>name: Users
>objectguid: {B199B822-F3BA-4570-9A65-6D96432E5519}
>objectsid: S-1-5-32-545
>sAMAccountName: Users
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Guests,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Guests
>description: Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted
>member: CN=Domain Guests,CN=Users,DC=MAD,DC=local
>member: CN=Guest,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Guests,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 8212
>uSNChanged: 12383
>name: Guests
>objectguid: {F2774B74-7965-4E4B-AAD9-1F0C29DF37E3}
>objectsid: S-1-5-32-546
>sAMAccountName: Guests
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Print Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Print Operators
>description: Members can administer printers installed on domain controllers
>distinguishedName: CN=Print Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 8215
>uSNChanged: 20523
>name: Print Operators
>objectguid: {B8ADE35C-DE42-4FDA-AA6C-42DC1050A601}
>objectsid: S-1-5-32-550
>adminCount: 1
>sAMAccountName: Print Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Backup Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Backup Operators
>description: Backup Operators can override security restrictions for the sole purpose of backing up or restoring files
>distinguishedName: CN=Backup Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 8216
>uSNChanged: 20516
>name: Backup Operators
>objectguid: {B23F9719-3978-4BFA-9F75-84E8E05C5224}
>objectsid: S-1-5-32-551
>adminCount: 1
>sAMAccountName: Backup Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Replicator,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Replicator
>description: Supports file replication in a domain
>distinguishedName: CN=Replicator,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 8217
>uSNChanged: 20518
>name: Replicator
>objectguid: {10582A22-A71E-4A3C-8FA0-0C4F342578A7}
>objectsid: S-1-5-32-552
>adminCount: 1
>sAMAccountName: Replicator
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Remote Desktop Users,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Remote Desktop Users
>description: Members in this group are granted the right to logon remotely
>distinguishedName: CN=Remote Desktop Users,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8218
>uSNChanged: 8218
>name: Remote Desktop Users
>objectguid: {4932A008-1527-44CC-A2F3-65FAAB42DEB6}
>objectsid: S-1-5-32-555
>sAMAccountName: Remote Desktop Users
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Network Configuration Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Network Configuration Operators
>description: Members in this group can have some administrative privileges to manage configuration of networking features
>distinguishedName: CN=Network Configuration Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8219
>uSNChanged: 8219
>name: Network Configuration Operators
>objectguid: {604E76C4-54E0-4713-8943-CECA0AC4FC69}
>objectsid: S-1-5-32-556
>sAMAccountName: Network Configuration Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Performance Monitor Users,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Performance Monitor Users
>description: Members of this group can access performance counter data locally and remotely
>distinguishedName: CN=Performance Monitor Users,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8220
>uSNChanged: 8220
>name: Performance Monitor Users
>objectguid: {1FD11E61-D8B2-4128-90A3-F9AD93E19DBF}
>objectsid: S-1-5-32-558
>sAMAccountName: Performance Monitor Users
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Performance Log Users,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Performance Log Users
>description: Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer
>distinguishedName: CN=Performance Log Users,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8221
>uSNChanged: 8221
>name: Performance Log Users
>objectguid: {5318E1BF-F07D-49F7-80D2-F26776BC5C46}
>objectsid: S-1-5-32-559
>sAMAccountName: Performance Log Users
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Distributed COM Users,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Distributed COM Users
>description: Members are allowed to launch, activate and use Distributed COM objects on this machine.
>distinguishedName: CN=Distributed COM Users,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8222
>uSNChanged: 8222
>name: Distributed COM Users
>objectguid: {F87D58A0-EC18-418A-B4F0-FC5E2F347EF0}
>objectsid: S-1-5-32-562
>sAMAccountName: Distributed COM Users
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=IIS_IUSRS,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: IIS_IUSRS
>description: Built-in group used by Internet Information Services.
>member: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=MAD,DC=local
>distinguishedName: CN=IIS_IUSRS,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8223
>uSNChanged: 8226
>name: IIS_IUSRS
>objectguid: {D9A42D48-2C22-4429-8879-9DD6D5EE4B9A}
>objectsid: S-1-5-32-568
>sAMAccountName: IIS_IUSRS
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Cryptographic Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Cryptographic Operators
>description: Members are authorized to perform cryptographic operations.
>distinguishedName: CN=Cryptographic Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8227
>uSNChanged: 8227
>name: Cryptographic Operators
>objectguid: {AF55F8C0-7A39-4572-9AC3-82182A3074B4}
>objectsid: S-1-5-32-569
>sAMAccountName: Cryptographic Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Event Log Readers,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Event Log Readers
>description: Members of this group can read event logs from local machine
>distinguishedName: CN=Event Log Readers,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8228
>uSNChanged: 8228
>name: Event Log Readers
>objectguid: {E660E978-EEF6-4458-9171-0DBB8DD83284}
>objectsid: S-1-5-32-573
>sAMAccountName: Event Log Readers
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Certificate Service DCOM Access,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Certificate Service DCOM Access
>description: Members of this group are allowed to connect to Certification Authorities in the enterprise
>distinguishedName: CN=Certificate Service DCOM Access,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8229
>uSNChanged: 8229
>name: Certificate Service DCOM Access
>objectguid: {2600BB51-77C2-4474-B8ED-82E56E51DF11}
>objectsid: S-1-5-32-574
>sAMAccountName: Certificate Service DCOM Access
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=RDS Remote Access Servers,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: RDS Remote Access Servers
>description: Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.
>distinguishedName: CN=RDS Remote Access Servers,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8230
>uSNChanged: 8230
>name: RDS Remote Access Servers
>objectguid: {A1160EEB-914B-4F10-A99E-CD84364925EF}
>objectsid: S-1-5-32-575
>sAMAccountName: RDS Remote Access Servers
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=RDS Endpoint Servers,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: RDS Endpoint Servers
>description: Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.
>distinguishedName: CN=RDS Endpoint Servers,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8231
>uSNChanged: 8231
>name: RDS Endpoint Servers
>objectguid: {916209F2-FC99-47B3-897C-C08D75E1B7B8}
>objectsid: S-1-5-32-576
>sAMAccountName: RDS Endpoint Servers
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=RDS Management Servers,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: RDS Management Servers
>description: Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.
>distinguishedName: CN=RDS Management Servers,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8232
>uSNChanged: 8232
>name: RDS Management Servers
>objectguid: {2EB4A140-ED2A-4418-9735-46746C537FF5}
>objectsid: S-1-5-32-577
>sAMAccountName: RDS Management Servers
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Hyper-V Administrators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Hyper-V Administrators
>description: Members of this group have complete and unrestricted access to all features of Hyper-V.
>distinguishedName: CN=Hyper-V Administrators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8233
>uSNChanged: 8233
>name: Hyper-V Administrators
>objectguid: {8A08D269-2BE8-4E82-BE77-D51AF4B1FF5F}
>objectsid: S-1-5-32-578
>sAMAccountName: Hyper-V Administrators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Access Control Assistance Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Access Control Assistance Operators
>description: Members of this group can remotely query authorization attributes and permissions for resources on this computer.
>distinguishedName: CN=Access Control Assistance Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8234
>uSNChanged: 8234
>name: Access Control Assistance Operators
>objectguid: {CD090024-8DC1-4A00-A2C6-F8CFE06D7625}
>objectsid: S-1-5-32-579
>sAMAccountName: Access Control Assistance Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Remote Management Users,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Remote Management Users
>description: Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.
>distinguishedName: CN=Remote Management Users,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8235
>uSNChanged: 8235
>name: Remote Management Users
>objectguid: {E98542ED-2083-4250-B315-1DBB52AB56A9}
>objectsid: S-1-5-32-580
>sAMAccountName: Remote Management Users
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Storage Replica Administrators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Storage Replica Administrators
>description: Members of this group have complete and unrestricted access to all features of Storage Replica.
>distinguishedName: CN=Storage Replica Administrators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202070852.0Z
>whenChanged: 20211202070852.0Z
>uSNCreated: 8236
>uSNChanged: 8236
>name: Storage Replica Administrators
>objectguid: {59ABE566-EFA6-4AFA-B0CD-C2459C4D6C14}
>objectsid: S-1-5-32-582
>sAMAccountName: Storage Replica Administrators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Domain Computers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Domain Computers
>description: All workstations and servers joined to the domain
>distinguishedName: CN=Domain Computers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12330
>uSNChanged: 12332
>name: Domain Computers
>objectguid: {7578FE3D-0D7B-48CC-8278-9E8C3C55F112}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-515
>sAMAccountName: Domain Computers
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Domain Controllers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Domain Controllers
>description: All domain controllers in the domain
>distinguishedName: CN=Domain Controllers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12333
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>uSNChanged: 20527
>name: Domain Controllers
>objectguid: {C93B0C49-4273-45E7-A16A-A0443CBB56AB}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-516
>adminCount: 1
>sAMAccountName: Domain Controllers
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Schema Admins,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Schema Admins
>description: Designated administrators of the schema
>member: CN=Administrator,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Schema Admins,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12336
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>uSNChanged: 20505
>name: Schema Admins
>objectguid: {05728F12-F074-4901-9B22-C7889E7926CE}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-518
>adminCount: 1
>sAMAccountName: Schema Admins
>sAMAccountType: 268435456
>groupType: -2147483640
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Enterprise Admins,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Enterprise Admins
>description: Designated administrators of the enterprise
>member: CN=Administrator,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Enterprise Admins,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12339
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>memberOf: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 20508
>name: Enterprise Admins
>objectguid: {4FDDD640-BE1C-49D3-82AC-9CDAA077CF18}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-519
>adminCount: 1
>sAMAccountName: Enterprise Admins
>sAMAccountType: 268435456
>groupType: -2147483640
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Cert Publishers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Cert Publishers
>description: Members of this group are permitted to publish certificates to the directory
>distinguishedName: CN=Cert Publishers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12342
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>uSNChanged: 12344
>name: Cert Publishers
>objectguid: {0400C2D4-7AB2-49B4-8C2A-7747237909E6}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-517
>sAMAccountName: Cert Publishers
>sAMAccountType: 536870912
>groupType: -2147483644
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Domain Admins,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Domain Admins
>description: Designated administrators of the domain
>member: CN=madAdmin,CN=Users,DC=MAD,DC=local
>member: CN=Administrator,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Domain Admins,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12345
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>memberOf: CN=Administrators,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 20509
>name: Domain Admins
>objectguid: {7091ACDD-E875-4208-BDC4-20C9D6D2F842}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-512
>adminCount: 1
>sAMAccountName: Domain Admins
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Domain Users,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Domain Users
>description: All domain users
>distinguishedName: CN=Domain Users,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12348
>memberOf: CN=Users,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 12350
>name: Domain Users
>objectguid: {1E318236-94AB-441C-8F41-8E3FF65A1656}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-513
>sAMAccountName: Domain Users
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Domain Guests,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Domain Guests
>description: All domain guests
>distinguishedName: CN=Domain Guests,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12351
>memberOf: CN=Guests,CN=Builtin,DC=MAD,DC=local
>uSNChanged: 12353
>name: Domain Guests
>objectguid: {E7FA1F48-C4C7-4372-A47A-9B2590509813}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-514
>sAMAccountName: Domain Guests
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Group Policy Creator Owners,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Group Policy Creator Owners
>description: Members in this group can modify group policy for the domain
>member: CN=Administrator,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Group Policy Creator Owners,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12354
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>uSNChanged: 12391
>name: Group Policy Creator Owners
>objectguid: {21018033-1E6D-4101-AD30-42220A9D10BA}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-520
>sAMAccountName: Group Policy Creator Owners
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=RAS and IAS Servers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: RAS and IAS Servers
>description: Servers in this group can access remote access properties of users
>distinguishedName: CN=RAS and IAS Servers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12357
>uSNChanged: 12359
>name: RAS and IAS Servers
>objectguid: {68DA7E84-797A-48BC-9D68-D89DD14F13E6}
>>sAMAccountName: RAS and IAS Servers
>sAMAccountType: 536870912
>groupType: -2147483644
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Server Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Server Operators
>description: Members can administer domain servers
>distinguishedName: CN=Server Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12360
>uSNChanged: 20521
>name: Server Operators
>objectguid: {629B503D-F5BE-4DBB-BEE5-17220549D3A6}
>objectsid: S-1-5-32-549
>adminCount: 1
>sAMAccountName: Server Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Account Operators,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Account Operators
>description: Members can administer domain user and group accounts
>distinguishedName: CN=Account Operators,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12363
>uSNChanged: 20524
>name: Account Operators
>objectguid: {D21A8BE3-C07F-4971-8C7E-DB2ECC3CE4D1}
>objectsid: S-1-5-32-548
>adminCount: 1
>sAMAccountName: Account Operators
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Pre-Windows 2000 Compatible Access
>description: A backward compatibility group which allows read access on all users and groups in the domain
>member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=MAD,DC=local
>distinguishedName: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12366
>uSNChanged: 12393
>name: Pre-Windows 2000 Compatible Access
>objectguid: {1A4607E6-0767-4E95-AFBF-ED3D701647D0}
>objectsid: S-1-5-32-554
>sAMAccountName: Pre-Windows 2000 Compatible Access
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Incoming Forest Trust Builders,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Incoming Forest Trust Builders
>description: Members of this group can create incoming, one-way trusts to this forest
>distinguishedName: CN=Incoming Forest Trust Builders,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12369
>uSNChanged: 12371
>name: Incoming Forest Trust Builders
>objectguid: {49FD8EA2-85E7-4810-9BD5-5B0A17DC9CBA}
>objectsid: S-1-5-32-557
>sAMAccountName: Incoming Forest Trust Builders
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Windows Authorization Access Group,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Windows Authorization Access Group
>description: Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects
>member: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=MAD,DC=local
>distinguishedName: CN=Windows Authorization Access Group,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12372
>uSNChanged: 12396
>name: Windows Authorization Access Group
>objectguid: {3AE04F1D-D8AC-4213-BAE8-4083AE344AC2}
>objectsid: S-1-5-32-560
>sAMAccountName: Windows Authorization Access Group
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Terminal Server License Servers,CN=Builtin,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Terminal Server License Servers
>description: Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage
>distinguishedName: CN=Terminal Server License Servers,CN=Builtin,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12375
>uSNChanged: 12377
>name: Terminal Server License Servers
>objectguid: {0D0B329C-8C1E-4665-8A49-D398094CED47}
>objectsid: S-1-5-32-561
>sAMAccountName: Terminal Server License Servers
>sAMAccountType: 536870912
>systemFlags: -1946157056
>groupType: -2147483643
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Allowed RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Allowed RODC Password Replication Group
>description: Members in this group can have their passwords replicated to all read-only domain controllers in the domain
>distinguishedName: CN=Allowed RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12402
>uSNChanged: 12404
>name: Allowed RODC Password Replication Group
>objectguid: {6CE5BC7A-AB3E-442C-88AD-C3D073909036}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-571
>sAMAccountName: Allowed RODC Password Replication Group
>sAMAccountType: 536870912
>groupType: -2147483644
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Denied RODC Password Replication Group
>description: Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain
>member: CN=Read-only Domain Controllers,CN=Users,DC=MAD,DC=local
>member: CN=Group Policy Creator Owners,CN=Users,DC=MAD,DC=local
>member: CN=Domain Admins,CN=Users,DC=MAD,DC=local
>member: CN=Cert Publishers,CN=Users,DC=MAD,DC=local
>member: CN=Enterprise Admins,CN=Users,DC=MAD,DC=local
>member: CN=Schema Admins,CN=Users,DC=MAD,DC=local
>member: CN=Domain Controllers,CN=Users,DC=MAD,DC=local
>member: CN=krbtgt,CN=Users,DC=MAD,DC=local
>distinguishedName: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12405
>uSNChanged: 12433
>name: Denied RODC Password Replication Group
>objectguid: {F03FC28B-79FD-4919-8650-670E2F0CBC14}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-572
>sAMAccountName: Denied RODC Password Replication Group
>sAMAccountType: 536870912
>groupType: -2147483644
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Read-only Domain Controllers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Read-only Domain Controllers
>description: Members of this group are Read-Only Domain Controllers in the domain
>distinguishedName: CN=Read-only Domain Controllers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12419
>memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MAD,DC=local
>uSNChanged: 20528
>name: Read-only Domain Controllers
>objectguid: {323EE0FA-9DA4-4091-AF82-C74F20FE9D8E}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-521
>adminCount: 1
>sAMAccountName: Read-only Domain Controllers
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Enterprise Read-only Domain Controllers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Enterprise Read-only Domain Controllers
>description: Members of this group are Read-Only Domain Controllers in the enterprise
>distinguishedName: CN=Enterprise Read-only Domain Controllers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12429
>uSNChanged: 12431
>name: Enterprise Read-only Domain Controllers
>objectguid: {94C16964-3459-4A14-86E9-5E222B171832}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-498
>sAMAccountName: Enterprise Read-only Domain Controllers
>sAMAccountType: 268435456
>groupType: -2147483640
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Cloneable Domain Controllers,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Cloneable Domain Controllers
>description: Members of this group that are domain controllers may be cloned.
>distinguishedName: CN=Cloneable Domain Controllers,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12440
>uSNChanged: 12442
>name: Cloneable Domain Controllers
>objectguid: {E44A50D3-46F4-4181-A063-07241B2A930C}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-522
>sAMAccountName: Cloneable Domain Controllers
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Protected Users,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Protected Users
>description: Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.
>distinguishedName: CN=Protected Users,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202071210.0Z
>uSNCreated: 12445
>uSNChanged: 12447
>name: Protected Users
>objectguid: {58653703-A189-4F66-9D25-DCFE3C902891}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-525
>sAMAccountName: Protected Users
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000001.0Z

dn:CN=Key Admins,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Key Admins
>description: Members of this group can perform administrative actions on key objects within the domain.
>distinguishedName: CN=Key Admins,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12450
>uSNChanged: 20514
>name: Key Admins
>objectguid: {8334E4FA-A269-482E-9F9A-EF55B2389FBA}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-526
>adminCount: 1
>sAMAccountName: Key Admins
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=Enterprise Key Admins,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: Enterprise Key Admins
>description: Members of this group can perform administrative actions on key objects within the forest.
>distinguishedName: CN=Enterprise Key Admins,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071210.0Z
>whenChanged: 20211202073855.0Z
>uSNCreated: 12453
>uSNChanged: 20507
>name: Enterprise Key Admins
>objectguid: {D3709F1C-6E19-4B71-AFB6-50E25889ED65}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-527
>adminCount: 1
>sAMAccountName: Enterprise Key Admins
>sAMAccountType: 268435456
>groupType: -2147483640
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>isCriticalSystemObject: TRUE
>dSCorePropagationData: 20211202073855.0Z
>dSCorePropagationData: 20211202071210.0Z
>dSCorePropagationData: 16010101000416.0Z

dn:CN=DnsAdmins,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: DnsAdmins
>description: DNS Administrators Group
>distinguishedName: CN=DnsAdmins,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071250.0Z
>whenChanged: 20211202071250.0Z
>uSNCreated: 12486
>uSNChanged: 12488
>name: DnsAdmins
>objectguid: {799CEAE4-7D52-4918-B948-F303A4F403E3}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1103
>sAMAccountName: DnsAdmins
>sAMAccountType: 536870912
>groupType: -2147483644
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 16010101000000.0Z

dn:CN=DnsUpdateProxy,CN=Users,DC=MAD,DC=local
>objectClass: top
>objectClass: group
>cn: DnsUpdateProxy
>description: DNS clients who are permitted to perform dynamic updates on behalf of some other clients (such as DHCP servers).
>distinguishedName: CN=DnsUpdateProxy,CN=Users,DC=MAD,DC=local
>instanceType: 4
>whenCreated: 20211202071250.0Z
>whenChanged: 20211202071250.0Z
>uSNCreated: 12491
>uSNChanged: 12491
>name: DnsUpdateProxy
>objectguid: {7B355651-2F8B-44C9-97FF-E52BE446E718}
>objectsid: S-1-5-21-2680507893-677197679-1321753512-1104
>sAMAccountName: DnsUpdateProxy
>sAMAccountType: 268435456
>groupType: -2147483646
>objectCategory: CN=Group,CN=Schema,CN=Configuration,DC=MAD,DC=local
>dSCorePropagationData: 16010101000000.0Z


48 Objects returned
```

<img width="1440" height="654" alt="Screenshot 2025-07-22 at 11 02 59 PM" src="https://github.com/user-attachments/assets/0159bf90-ff88-4f25-be27-b7b08d5749bc" />


---

```bash
PS > type ad_group_net.txt

Group Accounts for \\TARGETDC

-------------------------------------------------------------------------------
*Cloneable Domain Controllers
*DnsUpdateProxy
*Domain Admins
*Domain Computers
*Domain Controllers
*Domain Guests
*Domain Users
*Enterprise Admins
*Enterprise Key Admins
*Enterprise Read-only Domain Controllers
*Group Policy Creator Owners
*Key Admins
*Protected Users
*Read-only Domain Controllers
*Schema Admins
The command completed successfully.

PS > 
```

<img width="1440" height="638" alt="Screenshot 2025-07-22 at 11 04 08 PM" src="https://github.com/user-attachments/assets/d3c7f435-7082-4ea1-b59c-5f6e21e7b36d" />

---










