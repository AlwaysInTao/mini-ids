# 🛡️ SentryPy: Lightweight Network IDS Daemon Engine

Welcome to the **SentryPy** repository! This open-source cybersecurity engine captures raw incoming network data, extracts TCP/IP socket structures, and flags malicious payloads against custom pattern signatures.

[![YouTube Video Link](https://shields.io)](YOUR_YOUTUBE_VIDEO_URL_HERE)

## 🚀 Core Security Features
* **Raw Socket Sniffing:** Hooks directly into the system network interface loop to analyze lower-level IP structures.
* **Live Threat Analysis:** Real-time matrix parsing engine checking application layers for exploit signatures.
* **Zero Dependencies:** Engineered completely via native Python standard libraries.

## ⚙️ Running Locally
Because raw network interface capture requires system administration hook-access, fire up the scanner on Linux using one of our targeted execution profiles:

### Interactive Hook Mode (Loud Out)
Streams high-contrast security indicators directly to your active terminal window:
```bash
sudo python3 sentrypy.py
```

### Production Background Mode (Silent Out)
Runs quietly while feeding analyst-grade log indicators directly to disk storage:
```bash
sudo python3 sentrypy.py --silent
```

---

## ⚙️ Persistent Deployment (Run Automatically at Boot)
To run the SentryPy engine automatically as an isolated background security daemon on Linux (without keeping a terminal window open), configure a native `systemd` service:

1. Create a service configuration file:
```bash
sudo tee /etc/systemd/system/sentrypy.service << 'SERVICE_EOF'
[Unit]
Description=SentryPy Lightweight Intrusion Detection Daemon
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/brian
ExecStart=/usr/bin/python3 /home/brian/sentrypy.py --silent
Restart=on-failure

[Install]
WantedBy=multi-user.target
SERVICE_EOF
```

2. Reload the system controller daemon, enable the service to start at boot, and fire it up immediately:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sentrypy.service
sudo systemctl start sentrypy.service
```

3. To monitor your live security threat updates or audit background daemon behaviors in real-time, run our follow tracker utility:
```bash
tail -f sentrypy.log
```

---

## 🧠 Acknowledgments
* Co-designed and documented in partnership with Gemini AI.
