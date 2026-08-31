import argparse
import logging
import random
import sys
import time

def setup_engine_logging(silent_mode):
    """Configures the engine log flow output target based on CLI flags."""
    log_format = '%(asctime)s - [%(levelname)s] - %(message)s'
    
    if silent_mode:
        # Silent Mode: Write immediately to the local file
        file_handler = logging.FileHandler('sentrypy.log', mode='a', encoding='utf-8', delay=False)
        file_handler.setFormatter(logging.Formatter(log_format))
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        
        print("🛡️ SENTRYPY ENGINE v1.0 | Running silently in background...")
        print("🟢 Security daemon active. Logging threat indicators to 'sentrypy.log'...")
    else:
        # Loud Mode: Stream directly to the console header
        logging.basicConfig(level=logging.INFO, format=log_format, 
                            handlers=[logging.StreamHandler(sys.stdout)])
        print("🛡️ SENTRYPY ENGINE v1.0 | Initializing Network Socket Sniffer...")
        print("🟢 IDS Engine Active. Monitoring live incoming TCP/IP data packets...\n")

def main():
    parser = argparse.ArgumentParser(description="SentryPy Lightweight IDS Daemon Engine")
    parser.add_argument('-s', '--silent', action='store_true', help="Execute engine silently and pipe logs to disk")
    args = parser.parse_args()

    setup_engine_logging(args.silent)
    
    # Realistic security incident signatures and known malicious actor IPs
    attack_types = [
        "SYN Flood DoS Attack", 
        "SSH Brute-Force Attempt", 
        "Nmap Intense Port Scan", 
        "Malicious SQL Injection Payload",
        "Reverse Shell Activity Detected"
    ]
    malicious_ips = ["192.168.1.142", "185.220.101.5", "45.132.22.19", "10.0.0.55", "91.240.118.4"]
    target_ports = [22, 80, 443, 3306, 8080]

    try:
        logging.info("Initializing Network Socket Sniffer Engine...")
        time.sleep(1)
        logging.info("Signature database loaded. Monitoring network traffic layers...")
        
        while True:
            # Drop a realistic cyberattack alert every 2 to 4 seconds
            time.sleep(random.uniform(2.0, 4.0))
            
            event = random.choice(attack_types)
            ip = random.choice(malicious_ips)
            port = random.choice(target_ports)
            
            # Pipe out the security warning threat flag
            logging.warning(f"THREAT INTRUSION FLAGGED! Event: {event} | Source Node: {ip} -> Target Port: {port}")
            
    except KeyboardInterrupt:
        if args.silent:
            logging.info("IDS Engine deactivated cleanly via signal intercept.")
            print("\n🛑 Background daemon stopped.")
        else:
            print("\n🛑 IDS Engine deactivated cleanly. Exiting security cluster.")

if __name__ == "__main__":
    main()
