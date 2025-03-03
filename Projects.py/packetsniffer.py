from scapy.all import sniff, hexdump

# Function to process each packet
def process_packet(packet):
    # Print a summary of the packet
    print(packet.summary())
    # Prints detailed packet information
    print(packet.show())
    # Prints the raw hex dump of the packet
    hexdump(packet)

# Sniff packets, specify iface if needed
sniff(prn=process_packet, store=False)
