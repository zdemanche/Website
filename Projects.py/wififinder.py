import subprocess
import re

def get_wifi_networks():
    try:
        # Specify the full path to the airport utility
        airport_path = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
        command = [airport_path, "scan"]
        
        # Execute the command to scan for WiFi networks
        output = subprocess.check_output(command)
        
        # Decode the output from bytes to string
        output = output.decode('utf-8').split('\n')
        networks = []
        
        # Debug print to see what the output looks like
        print("Debug: Output from airport command", output)
        
        # Process each line in the output
        for line in output:
            if line.strip():  # Make sure the line isn't empty
                parts = re.split(r'\s{2,}', line.strip())  # Split on two or more spaces
                if len(parts) > 1:
                    ssid = parts[0]  # Assuming the first column is the SSID
                    networks.append(ssid)
                
        return networks
    
    except subprocess.CalledProcessError as e:
        print(f"Command error: {e}")
        return []
    except Exception as e:
        print(f"General error: {e}")
        return []

def main():
    networks = get_wifi_networks()
    if networks:
        print("Available WiFi networks:")
        for network in networks:
            print(network)
    else:
        print("No WiFi networks available")

if __name__ == '__main__':
    main()
