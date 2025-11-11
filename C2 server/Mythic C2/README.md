# Mythic C2

# **Implementation and Analysis of the Mythic C2 Framework**


## **1. Introduction**

### **1.1. Overview of Mythic C2**

Mythic is a sophisticated, modular Command and Control (C2) framework written in Python and JavaScript, designed for red team operations and penetration testing.

### **1.2. Objective**

The primary objective of this task was to implement the Mythic Command and 
Control (C2) framework in a controlled lab environment, create a 
functional agent, establish a callback from a target system, and analyze
 the framework's capabilities, strengths, and operational 
characteristics from a red team perspective.

## **2. Methodology: Implementation**

### **2.1. Lab Environment Setup**

The following infrastructure was established for this task:

| Component | Specifications | Role |
| --- | --- | --- |
| **C2 Server** | OS: [Kali linux VERSION="2025.3"]  Resources: [2vCPU, 4GB RAM, 50GB Disk] | Hosts the Mythic Framework |
| **Target Machine** | OS: [Windows 10  VM]  Resources: [2vCPU, 4GB RAM] | Simulates a victim endpoint |
| **Network** | [Bridge Network] | Allows connectivity between VMs |

### **2.2. Mythic Framework Installation**

The installation was performed using the standard Docker-based method for simplicity and reproducibility.

Steps Taken:

1. Cloned the official Mythic repository.
    
    ```bash
    git clone https://github.com/its-a-feature/Mythic --depth 1 --single-branch
    cd Mythic 
    ```
    
2. Ran the installation script, which handles Docker installation and container setup.
    
    ```bash
    sudo ./install_docker_kali.sh  
    ```
    
3. Generate Mythic cli tool
    
    ```bash
    sudo make
    ```
    
    ![Screenshot 2025-10-09 at 9.15.22 PM.png](Mythic%20C2/Screenshot_2025-10-09_at_9.15.22_PM.png)
    
4. Started the Mythic services.
    
    ```bash
    sudo ./mythic-cli start
    ```
    
    ![Screenshot 2025-10-09 at 9.17.31 PM.png](Mythic%20C2/Screenshot_2025-10-09_at_9.17.31_PM.png)
    
    check status: 
    
    ```bash
    sudo ./mythic-cli status
    ```
    
    ![Screenshot 2025-10-09 at 9.23.36 PM.png](Mythic%20C2/Screenshot_2025-10-09_at_9.23.36_PM.png)
    
5. Accessed the Mythic web interface at [https://127.0.0.1:7443/](https://127.0.0.1:7443/) and created an initial user account: `[mythic_admin]` and password is in the .env file.

 

Mythic login panel

![Screenshot 2025-10-09 at 9.28.59 PM.png](Mythic%20C2/Screenshot_2025-10-09_at_9.28.59_PM.png)

Mythic Dashboard

![Screenshot 2025-10-09 at 9.29.38 PM.png](Mythic%20C2/Screenshot_2025-10-09_at_9.29.38_PM.png)

## **3. Installing Agents and C2 Profiles**

To install an agent, simply run the script and provide an argument of the path to the agent on GitHub:

```bash
sudo ./mythic-cli install github https://github.com/MythicAgents/apfell
```

Same for for installing C2 Profiles:

```bash
sudo ./mythic-cli install github https://github.com/MythicC2Profiles/http
```

Installing AGENTS: Apollo and Athena

Installing WRAPPER: scarecrow_wrapper

```bash
sudo ./mythic-cli install github https://github.com/MythicAgents/Apollo  
sudo ./mythic-cli install github https://github.com/MythicAgents/Athena
sudo ./mythic-cli install github https://github.com/MythicAgents/scarecrow_wrapper
```

![Screenshot 2025-10-09 at 9.41.39 PM.png](Mythic%20C2/Screenshot_2025-10-09_at_9.41.39_PM.png)

## 4. **Payload Generation and Configuration**

### **4.1. Agent Selection Rationale**

The **Apollo** agent was selected for this engagement due to its robust feature set, native Windows compatibility, and active development within the Mythic  ecosystem. As a .NET-based agent, Apollo provides comprehensive post-exploitation capabilities and seamless integration with Mythic's modular architecture.

Head over to payload generation:

![p-1-select-target-os.png](Mythic%20C2/p-1-select-target-os.png)

---

Configure payload:

![p-2-configure-payload.png](Mythic%20C2/p-2-configure-payload.png)

---

Select commands:

![p-3-select-commands.png](Mythic%20C2/p-3-select-commands.png)

---

Select C2:

![p-4-selct-c2.png](Mythic%20C2/p-4-selct-c2.png)

---

**C2 Profile Configuration:**

- **C2 Profile:** `http`
- **Callback Host:** `http://10.71.194.163`
- **Callback Port:** `80`
- **Kill Date:** `[None]`
- **Callback Interval:** `10` seconds
- **Callback Jitter:** `23%`

![p-5-c2-config.png](Mythic%20C2/p-5-c2-config.png)

---

Payload preview:

![p-6-build.png](Mythic%20C2/p-6-build.png)

---

Payload build successfully:

![p-7-build-success.png](Mythic%20C2/p-7-build-success.png)

## 5. Payload Transfer

As we are Performing this on a local network. Let’s transfer this payload to windows machine using python http server

![p-8-http-server.png](Mythic%20C2/p-8-http-server.png)

---

### 5.1. Download payload in the targeted machine:

![p-9-download.png](Mythic%20C2/p-9-download.png)

---

### 5.2. Execution

The generated `apollo.exe` payload was transferred to the Windows 10 target machine and executed with standard user privileges.

![agent-exeution.png](Mythic%20C2/agent-exeution.png)

---

## 6. Command and Control

Upon execution, the agent successfully established a beacon to the Mythic server within seconds.

*Mythic dashboard showing a new active callback from the target.*

![call-back.png](Mythic%20C2/call-back.png)

---

Basic post-exploitation commands were issued to validate control and functionality:

- **Command:**  `shell whoami`
    - **Output:** `desktop-9u105a4\redteam`

![interact.png](Mythic%20C2/interact.png)

---

---

---

# **Discord C2 Profile Configuration**

## **1. Discord C2 Overview**

Discord C2 leverages Discord's legitimate infrastructure as a command and 
control channel, providing enhanced stealth by blending with normal web 
traffic. This approach offers several advantages for operational 
security:

- **Traffic Obfuscation:** C2 traffic appears as normal Discord API calls
- **Infrastructure Blending:** Uses legitimate Discord servers, avoiding suspicious domains
- **Resilience:** Benefits from Discord's robust infrastructure and uptime
- **Evasion:** Bypasses traditional domain/IP-based blocking
- **TLS Encryption:** All communications are encrypted by default via HTTPS

### **1.1. Discord Server Configuration**

 Turn on Developer option on discord.

### **1.2. Discord Application Creation**

1. Accessed Discord Developer Portal: `https://discord.com/developers/applications`
2. Created new application: `[MC2]`
3. Navigate to “Bot” section and click reset token. Store the newly generated token.
4. Scroll down a bit and enable these options:
    1. PRESENCE INTENT
    2. SERVER MEMBERS INTENT
    3. MESSAGE CONTENT INTENT

Now click save changes.

1. BOT Permissions: 
    - [x]  Administrator
2. Navigated to "OAUTH2" section 
    
    OAuth2 URL Generator scopes:
    
    - [x]  bot
    
    BOT PERMISSIONS:
    
    - [x]  Administrator
3. At the bottom you will get a link copy it and open it on a new tab. 
    
    Authenticate your bot with your discord server.
    
    Now copy the channel id:
    
    we have saved two things:
    
    - TOKEN ID
    - CHANNEL ID
    
    ![Screenshot 2025-10-11 at 6.10.03 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_6.10.03_PM.png)
    

## **2. Mythic Discord C2 Profile Setup**

### **2.1. Profile Installation**

```bash
# Navigate to Mythic directory
cd Mythic

# Install Discord C2 profile
sudo ./mythic-cli install github https://github.com/MythicAgents/discord
```

### **2.2. Profile Configuration Parameters**

Accessed Mythic Web UI → C2 Profiles → Discord Configuration:

![Screenshot 2025-10-11 at 6.18.50 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_6.18.50_PM.png)

Edit config.json:

![Screenshot 2025-10-11 at 6.20.34 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_6.20.34_PM.png)

Add Bot token and channel id we stored earlier and click submit.

![Screenshot 2025-10-11 at 6.24.00 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_6.24.00_PM.png)

### **2.3. Payload Generation with Discord C2**

### **2.3.1. Athena Agent with Discord C2**

**Configuration:**

1. **Select Operating System: Windows**
2. **Select Payload Type: Athena**
3. Select C2 profile Discord:
    
    Add Bot token and channel id
    
    ![bot-token.png](Mythic%20C2/bot-token.png)
    
    ![channel-id.png](Mythic%20C2/channel-id.png)
    
    Click next type file name of your choice then click create payload.
    
- **Payload Type:** Athena
- **C2 Profile:** Discord
- **Operating System:** Windows
- **Architecture:** x64
- **Format:** Windows Executable (.exe)

Download the payload and transfer it to the target using any server.

for now i’ll use python http server.

> **Will add Cloud Flare, ngrok or other port forwarding services later ON………**
> 

![Screenshot 2025-10-11 at 6.59.10 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_6.59.10_PM.png)

---

---

## **3. Discord C2 Communication Flow**

### 3.1. How discord c2 profile works.

![Pi7_Gif.gif](Mythic%20C2/Pi7_Gif.gif)

- Mythic Discord C2 uses Discord as a hidden messaging app between you and your implanted agent
- **Mythic handles the encoding** all messages are automatically encoded to look like normal Discord messages
- **All traffic goes to [Discord.com](https://discord.com/)** - looks like regular Discord bot traffic, not suspicious C2 calls

---

## **4. Agent Execution and Check-in**

- Executed Discord-configured Athena agent on target Windows system
    
    ![Screenshot 2025-10-11 at 7.00.47 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_7.00.47_PM.png)
    

- Observed bot joining Discord server within 30 seconds
    
    ![Screenshot 2025-10-11 at 7.11.03 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_7.11.03_PM.png)
    

- Verified agent check-in in Mythic web interface
    
    ![Screenshot 2025-10-11 at 7.11.53 PM.png](Mythic%20C2/Screenshot_2025-10-11_at_7.11.53_PM.png)
    

### **4.1. Command Execution via Discord**

**Test Commands Executed:**

1. `hostname` - User context enumeration
2. `screenshot` - Capturing screenshot
3. `cat` - Reading a file on desktop of the target system.
4. `ls, pwd`  - File system exploration
    
    ![Screenshot 2025-10-12 at 10.34.21 AM.png](Mythic%20C2/Screenshot_2025-10-12_at_10.34.21_AM.png)
    

![Screenshot 2025-10-12 at 10.34.46 AM.png](Mythic%20C2/Screenshot_2025-10-12_at_10.34.46_AM.png)

---

---

---
