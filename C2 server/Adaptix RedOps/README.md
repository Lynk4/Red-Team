# Adaptix RedOps

---



## Install and setup Adaptix from: https://adaptix-framework.gitbook.io/adaptix-framework/adaptix-c2/getting-starting/installation
```Make sure to genereatre SSL Certificate to run Adaptix Server. Generate certificate inside the dist folder.```

---

## Adaptix Server.
### After seting up the Adaptix start the server and Client both on separate terminal, click connect.
```password:pass```

<img width="1440" height="865" alt="Screenshot 2025-08-04 at 5 31 37 AM" src="https://github.com/user-attachments/assets/aa785d49-26f6-414b-a9c0-6e17641c0200" />

---

<img width="1440" height="866" alt="Screenshot 2025-08-04 at 5 32 45 AM" src="https://github.com/user-attachments/assets/cef83bfe-1341-4b55-9872-b55ac5a128c8" />


---
### Now we are good to go............

## Create Listeners.


<img width="799" height="447" alt="Screenshot 2025-08-04 at 5 33 43 AM" src="https://github.com/user-attachments/assets/a41501ed-5f50-4488-893b-17c95d0fd9b3" />


---
### right click then create.

<img width="1029" height="804" alt="Screenshot 2025-08-04 at 5 34 13 AM" src="https://github.com/user-attachments/assets/eacedf5c-9166-421a-8a9e-fd2bfa0728ba" />

---

<img width="781" height="763" alt="Screenshot 2025-08-04 at 5 36 36 AM" src="https://github.com/user-attachments/assets/1a0e4baa-e151-4275-82ed-43fcd56530ff" />

---


## Generate Agent
### right click on the generated listener click generate agent and Save it.


<img width="493" height="530" alt="Screenshot 2025-08-04 at 5 38 25 AM" src="https://github.com/user-attachments/assets/31d1e114-ae16-4f37-939e-44ef1e29b6b9" />

---


## Transfer the agent to the target machine however you want. I'll use python server.
### open the agent.

<img width="692" height="393" alt="Screenshot 2025-08-04 at 6 39 42 AM" src="https://github.com/user-attachments/assets/332f8c5a-81c9-4250-a708-46cd83d0e4c2" />

---

## Check out the Adaptix we got something..........

<img width="1440" height="872" alt="Screenshot 2025-08-04 at 6 41 00 AM" src="https://github.com/user-attachments/assets/6498baa9-a901-41e7-adc4-279fbded4099" />

---

## Access the console....

<img width="1440" height="870" alt="Screenshot 2025-08-04 at 6 42 58 AM" src="https://github.com/user-attachments/assets/dcf30b94-a649-442c-933f-0cdec2d6a0d8" />

---
## File browser

<img width="1440" height="865" alt="Screenshot 2025-08-04 at 6 44 04 AM" src="https://github.com/user-attachments/assets/f7a5d178-3f18-48b7-9640-f47e3fc7c436" />

---

## Process browser
<img width="1440" height="869" alt="Screenshot 2025-08-04 at 6 44 40 AM" src="https://github.com/user-attachments/assets/f79dc90d-29e5-42ef-93ac-c7e227f53ef2" />

---

## Extension kit check out: https://github.com/Adaptix-Framework/Extension-Kit

```bash
┌──(lockon💀Kali)-[~/AdaptixC2]
└─$ git clone https://github.com/Adaptix-Framework/Extension-Kit.git
Cloning into 'Extension-Kit'...
remote: Enumerating objects: 979, done.
remote: Counting objects: 100% (346/346), done.
remote: Compressing objects: 100% (254/254), done.
remote: Total 979 (delta 95), reused 261 (delta 79), pack-reused 633 (from 1)
Receiving objects: 100% (979/979), 4.34 MiB | 5.23 MiB/s, done.
Resolving deltas: 100% (321/321), done.
                                                                                       
┌──(lockon💀Kali)-[~/AdaptixC2]
└─$ ls
AdaptixClient  Dockerfile     LICENSE                   pre_install_macos_client.sh
AdaptixServer  Extenders      Makefile                  README.md
dist           Extension-Kit  pre_install_linux_all.sh
                                                                                       
┌──(lockon💀Kali)-[~/AdaptixC2]
└─$ cd Extension-Kit 
                                                                                       
┌──(lockon💀Kali)-[~/AdaptixC2/Extension-Kit]
└─$ ls
AD-BOF         Execution-BOF      Injection-BOF        Makefile     README.md
Creds-BOF      extension-kit.axs  LateralMovement-BOF  Postex-BOF   SAL-BOF
Elevation-BOF  _img               LICENSE              Process-BOF  SAR-BOF
                                                                                       
┌──(lockon💀Kali)-[~/AdaptixC2/Extension-Kit]
└─$ make
=====>>  AD-BOF
creating _bin directory
[+] ldapsearch
creating _bin
[+] hash
[+] klist
[+] triage
[+] dump
[+] describe
[+] tgtdeleg
[+] ptt
[+] purge
[+] asktgt
[+] asktgs
[+] renew
[+] changepw
[+] asreproasting
[+] kerberoasting
[+] s4u
[+] cross_s4u

=====>>  Creds-BOF
```

---

## Load All the script.


### goto AxScript --> script manager --> right click load the .axs files.


<img width="1440" height="870" alt="Screenshot 2025-08-04 at 7 09 38 AM" src="https://github.com/user-attachments/assets/07bd231e-480f-414f-96bc-367f4210bc10" />

---


<img width="1220" height="742" alt="Screenshot 2025-08-04 at 7 12 25 AM" src="https://github.com/user-attachments/assets/1cd70892-0737-4453-8f57-7761f538bcfa" />

---
## Now we can do a hell lot of things...........

<img width="1440" height="868" alt="Screenshot 2025-08-04 at 7 13 58 AM" src="https://github.com/user-attachments/assets/dace2b44-b81c-4f50-9931-75cae54d6035" />

---




