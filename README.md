# MODIE_RAT_Final (Educational Only)

> ⚠️ **DISCLAIMER:**  
> This project is strictly for **educational purposes only**.  
> It is intended to demonstrate techniques used by threat actors to help cybersecurity students, ethical hackers, and researchers better understand modern Remote Access Trojan (RAT) functionality.  
> **Do not use this code in unauthorized environments or for malicious intent. Misuse of this software can lead to legal consequences.**

---

## 🔍 Overview

**MODIE_RAT_Final** is a simulated Remote Access Trojan (RAT) written in C# that demonstrates the following capabilities:

- WebSocket-based Command & Control (C2) communication
- Basic persistence using WMI event subscriptions
- Encrypted data exfiltration (AES)
- Anti-analysis techniques (anti-debugging, VM detection)
- Placeholder process injection logic
- Secure session key negotiation
- Encrypted command execution and response loop

---

## 🎓 Educational Goals

This project is created to help learners understand:

- How RATs can maintain stealth and persistence
- How secure WebSocket connections are used for C2 communication
- How encryption (AES + DPAPI) is utilized to protect payloads and exfiltrated data
- How malware authors avoid detection using virtual machine and debugger checks
- How Windows Management Instrumentation (WMI) can be abused for persistence

