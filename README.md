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
## ⚙️ Persistent Deployment (Run Automatically at Boot)

To run the Mini-IDS Engine automatically as a background security service on Linux (without keeping a terminal window open), configure a native `systemd` service:

1. Create a service configuration file:
   ```bash
   sudo nano /etc/systemd/system/mini-ids.service
   ```

2. Paste the following configuration into the file (make sure to replace `/home/brian/Documents/` with the actual path to your script):
   ```ini
   [Unit]
   Description=Mini-IDS Network Security Engine
   After=network.target

   [Service]
   Type=simple
   User=root
   WorkingDirectory=/home/brian/Documents/
   ExecStart=/usr/bin/python3 /home/brian/Documents/ids.py
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

3. Reload the system controller daemon, enable the service to start at boot, and fire it up immediately:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable mini-ids.service
   sudo systemctl start mini-ids.service
   ```

4. To monitor live security alerts or debug the engine running in the background, read the system journals:
   ```bash
   sudo journalctl -u mini-ids.service -f
   ```
