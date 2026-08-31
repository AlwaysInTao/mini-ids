import argparse
import logging
import socket
import struct
import sys

def setup_engine_logging(silent_mode):
    """Configures the engine log flow output target based on CLI flags."""
    log_format = '%(asctime)s - [%(levelname)s] - %(message)s'
    
    if silent_mode:
        file_handler = logging.FileHandler('sentrypy.log', mode='a', encoding='utf-8', delay=False)
        file_handler.setFormatter(logging.Formatter(log_format))
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        print("🛡️ SENTRYPY ENGINE v1.0 | Running silently in background...")
        print("🟢 Security daemon active. Logging threat indicators to 'sentrypy.log'...")
    else:
        logging.basicConfig(level=logging.INFO, format=log_format, 
                            handlers=[logging.StreamHandler(sys.stdout)])
        print("🛡️ SENTRYPY ENGINE v1.0 | Initializing Network Socket Sniffer...")
        print("🟢 IDS Engine Active. Monitoring live incoming TCP/IP data packets...\n")

def main():
    parser = argparse.ArgumentParser(description="SentryPy Lightweight IDS Daemon Engine")
    parser.add_argument('-s', '--silent', action='store_true', help="Execute engine silently and pipe logs to disk")
    args = parser.parse_args()

    setup_engine_logging(args.silent)

    try:
        # Initialize a raw socket to capture all incoming IP packets (Linux exclusive)
        # ETH_P_ALL (0x0003) captures all link-layer protocols
        sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    except PermissionError:
        print("❌ Error: Root privileges required. Run with 'sudo'.")
        sys.exit(1)

    logging.info("Raw network interface hook established. Sniffing live traffic layers...")

    try:
        while True:
            # Capture the raw binary packet payload from the network interface buffer
            raw_packet, _ = sniffer.recvfrom(65535)
            
            # Extract the Ethernet Header (first 14 bytes: Destination MAC, Source MAC, EtherType)
            eth_header = raw_packet[:14]
            eth_data = struct.unpack('!6s6sH', eth_header)
            eth_type = eth_data[2]

            # Protocol 0x0800 indicates IPv4 traffic
            if eth_type == 0x0800:
                # Extract the IP Header (bytes 14 to 34)
                ip_header = raw_packet[14:34]
                ip_data = struct.unpack('!BBHHHBBH4s4s', ip_header)
                
                protocol = ip_data[6]
                src_ip = socket.inet_ntoa(ip_data[8])
                dest_ip = socket.inet_ntoa(ip_data[9])

                # Filter specifically for TCP protocol (Protocol number 6)
                if protocol == 6:
                    # Calculate IP header length to locate the start of the TCP header
                    version_ihl = ip_data[0]
                    ihl = (version_ihl & 0xF) * 4
                    tcp_start = 14 + ihl
                    
                    # Extract the TCP Ports (first 4 bytes of the TCP block)
                    tcp_header = raw_packet[tcp_start:tcp_start+4]
                    if len(tcp_header) == 4:
                        src_port, dest_port = struct.unpack('!HH', tcp_header)
                        
                        # --- EXPLICIT IDS SIGNATURE DETECTION BLOCK ---
                        
                        # Signature A: Detect sensitive SSH scanning attempts
                        if dest_port == 22:
                            logging.warning(f"SECURITY ALERT! Potential SSH Scanning | Source Node: {src_ip} -> Target Port: {dest_port}")
                        
                        # Signature B: Detect suspicious unencrypted web application tracking
                        elif dest_port == 80 or dest_port == 8080:
                            logging.info(f"Traffic Logged: Standard Web Request | Source: {src_ip} -> Port: {dest_port}")
                            
    except KeyboardInterrupt:
        if args.silent:
            logging.info("IDS Engine deactivated cleanly via signal intercept.")
            print("\n🛑 Background daemon stopped.")
        else:
            print("\n🛑 IDS Engine deactivated cleanly. Exiting security cluster.")

if __name__ == "__main__":
    main()
