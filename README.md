# 🛡️ Three-Tier Security Defense System

A robust, enterprise-ready web security defense system built with Flask, integrating multi-layered encryption, strong authentication controls, automated threat mitigation, and central security audit logging.

---

## Key Features

* **Multi-Factor Authentication (TOTP & RSA/ElGamal)**: Enforces time-based one-time passwords alongside hybrid asymmetric encryption for sensitive data.
* **SQL Injection Prevention**: Employs strictly parameterized database queries to sanitize inputs and mitigate parameter tampering.
* **Automated Account Lockout**: Automatically freezes access after 3 consecutive invalid authentication attempts to disrupt brute-force attacks.
* **Centralized Audit Trail**: Real-time tracking of attack payloads and rate-limit violations saved to non-volatile `logs/security.log`.

---

## 📸 System Verification & Demonstration

Below is the live execution proof demonstrating normal login handling alongside automated **SQL Injection defense (HTTP 403)** and **Account Lockout** in action:

![System Security Defense Demo](./demo.jpg)

### Execution Highlights:
* **Normal Workflow**: System correctly validates incoming credentials and returns authentication prompts.
* **Attack Suppression**: High-frequency `' OR '1'='1` payloads trigger immediate **HTTP 403 Forbidden** responses.
* **Rate Limiting**: Exceeding the 3-attempt threshold blocks subsequent requests with `Account temporarily locked due to too many failed attempts.`

---

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/xinyingyang14/Three-Tier-Security-Defense-System.git](https://github.com/xinyingyang14/Three-Tier-Security-Defense-System.git)
   cd Three-Tier-Security-Defense-System

1. Run the server:

python3 app.py

2. Trigger stress test script:

curl -s -X POST [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login) -d "username=' OR '1'='1&password=bad"

3. Save and exit nano: Press Ctrl + O $\rightarrow$ Press Enter to confirm saving, then press Ctrl + X to exit.
4. Run the following commands to push the updated README to GitHub:
   ```bash
   git add README.md
   git commit -m "docs: add comprehensive README with architecture and verification screenshot"
   git push
