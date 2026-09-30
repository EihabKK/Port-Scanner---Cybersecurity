








import socket  # Import the socket module to enable network communication using TCP/IP protocol
import termcolor  # Import termcolor for adding color to terminal output

# Function to scan a range of ports on one or more target IP addresses
def scan(targets, ports):
    print(termcolor.colored('/n' + 'Kicking off the scan for: ' + str(targets), 'cyan'))  # Announce the start of the scan in cyan
    for port in range(1, ports):  # Iterate over each port number from 1 to the specified number of ports
        scan_port(targets, port)  # Call scan_port to check if the current port is open on the target IP(s)

# Function to check if a specific port on a given IP address is open
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()  # Create a new socket object for the connection attempt
        sock.connect((ipaddress, port))  # Attempt to establish a connection to the given IP address and port
        print(termcolor.colored("[+] Port Opened: " + str(port), 'green'))  # Print a success message in green if the port is open
        sock.close()  # Close the socket connection to free up system resources
    except:
        print(termcolor.colored("[-] Port Closed or Error: " + str(port), 'red', attrs=['bold']))  # Print an error message in bright red if the port is closed or connection fails

# Main execution block to handle user input and initiate the scan
targets = input("Enter targets to scan (separate multiple targets with commas): ")  # Prompt the user for a list of target IPs
ports = int(input("How many ports do you want to scan?: "))  # Prompt the user for the number of ports to scan

if ',' in targets:
    print(termcolor.colored("[*] Multiple targets detected, scanning all listed IPs.", 'cyan'))  # Inform the user that multiple IP addresses will be scanned in cyan
    for ip_addr in targets.split(','):  # Split the input string into individual IP addresses using commas as delimiters
        scan(ip_addr.strip(' '), ports)  # Remove any extra spaces around IP addresses and initiate the scan for each address
else:
    scan(targets, ports)  # If only one target is provided, perform the scan directly on that IP address
