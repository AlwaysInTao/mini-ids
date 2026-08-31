# 🛡️ Mini-IDS Engine: Python Network Sniffer from Scratch

Welcome to the **Mini-IDS Engine** repository! This open-source cyber security engine captures raw incoming network data, extracts TCP/IP socket structures, and flags malicious payloads against custom pattern signatures.

## 🚀 Core Security Features
* **Raw Socket Sniffing:** Hooks directly into the system network interface loop to analyze lower-level IP structures.
* **Live Threat Analysis:** Real-time matrix parsing engine checking application layers for exploit signatures.
* **Zero Dependencies:** Engineered completely via native Python `socket` and `struct` libraries.

## ⚙️ Running Locally
Because raw network interface capture requires system administration hook-access, fire up the scanner on Linux using:
```bash
sudo python3 ids.py
```

## 🧠 Acknowledgments
* Co-designed and documented in partnership with Gemini AI.
