# Web Server - Day 1

## Protocols

- A convention/agreement on how to communicate between a client and a server.

  - HTTP protocol defines the structure of communication between clients and servers
    - Application layer
    - Build a request and sends to the OS and its wrapped in a TCP header
    - OS then wraps in an IP packet
  - TCP - makes sure all of the data you send arrives in order and intact
    - Used by other protocols like HTTP
  - IP - all about routing to other machines
    - IP address is how computers are found on the internet
    - IP is responsible for taking a packet of data across the internet from one computer to another

- Ping - used to test connectivity to a server
- Traceroute - tells you all the stops on the way to a server
