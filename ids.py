import socket
import struct
import sys

# Define simple attack signatures to look out for
THREAT_SIGNATURES = [
    b"DEBUG",      # Potential administrative bypass attempt
    b"ADMIN",      # Unauthorized privilege escalation attempt
    b"EXPLOIT",    # Common payload injection signature
]

def analyze_packet(payload):
    # Check raw data payload against our signature list
    for signature in THREAT_SIGNATURES:
        if signature in payload:
            return f"⚠️ ALERT! Found Malicious Signature: '{signature.decode(errors='ignore')}'"
    return None

def start_sniffing():
    print(" 🛡️ MINI-IDS ENGINE v1.0 | Initializing Network Socket Sniffer...")
    
    # Initialize a raw network socket to monitor low-level IP traffic
    try:
        # Works out of the box on Linux systems (requires sudo privileges)
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sniffer.bind(("0.0.0.0", 0))
    except PermissionError:
        print("\n❌ Error: Root/Sudo privileges required to capture raw network packets.")
        print("Please execute using: sudo python3 ids.py\n")
        sys.exit(1)

    print(" 🟢 IDS Engine Active. Monitoring live incoming TCP/IP data packets...\n")

    try:
        while True:
            # Capture raw network packet chunk
            raw_packet, addr = sniffer.recvfrom(65565)
            
            # Extract basic IP Header length (standard first 20 bytes)
            ip_header = raw_packet[0:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            
            src_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])
            
            # Isolate the remaining application data payload
            payload = raw_packet[20:]
            
            # Analyze payload data for anomalies
            threat_alert = analyze_packet(payload)
            
            if threat_alert:
                print(f"{threat_alert} | Origin: {src_ip} -> Dest: {dest_ip}")
            else:
                # Log general clean packet matrix stats for the channel stream
                if len(payload) > 0:
                    print(f"📡 Safe Packet Captured: {len(payload)} bytes from {src_ip}")

    except KeyboardInterrupt:
        print("\n 🛑 IDS Engine deactivated cleanly. Exiting security cluster.")

if __name__ == "__main__":
    start_sniffing()

