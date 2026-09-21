#!/bin/bash
# Clean up any lingering engine processes safely
echo "[*] Flushing mini_ids engine state..."
sudo killall php python3 2>/dev/null

# Clean iptables rules to default baseline if needed
# sudo iptables -F

echo "[+] State flushed cleanly."
