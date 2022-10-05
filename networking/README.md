# Networking

## Network concepts and protocols

- [link](https://app.pluralsight.com/library/courses/network-concepts-protocols-cert/table-of-contents)
- **Data networking**: transferring information
- **OSI model**: open systems interconnect, categorizes protocols and order
- [skipped](https://app.pluralsight.com/course-player?clipId=15983a98-20b3-4410-af10-bd7d42d6477a)
- **Segment**: a chunk of data with a transport layer header, application is put in this
- **Packet**: a chunk of data with a network layer header
- **Frame**: a chunk of data, with a Data link layer header
- At the physical layer converted to 1/0s

### Application layer protocols

- Application layer protocols and their layer port number
- Ex. HTTP = 80

### Transport layer protocols

- **TL**: job is to build and maintain a session between 2 endpoints (client & server)
- **TCP**: 3 way handshake, process to facility communication
  1. Client send SYN
  2. Server reply SYN-ACK
  3. Client send ACK (acknowledgement)
  4. Server send FIN to indicate end
  5. Client reply FIN-ACK
  6. Client send FIN
  7. Server send FIN-ACK
- **UDP**: no handshake, reliable communication, ACKs
- Port numbers, 0-65k
- **Server port numbers**:
  - well known: 0-124
  - registered: 1024-49,151
- **Client port numbers**: ephemeral port numbers, 49,152-65,535

- Network layer 3 (IP)
- IP address
  - network portion | host portion
  - 203.0.113 | 10 <- 4 Octets
  - Host: specific device in this network
- We now use classless address only (not classful)
  - Subnet mask, network gets 1s, host gets 0s
- Skip classless addressing

### IP address types

- **Network address**: id for group of devices, network prefix
  - network address has all 0s in host portion
  - ex. 10.10.0 | 0
- **Broadcast address**: id for all devices on a network
  - sends device to all devices in network
  - Has all 1s in host portion
  - Ex. 203.0.113 | 255
- **Host address**: id unique device on a network
  - Not network address or broadcast but anywhere in between
  - Anything except all 0s or 1s
  - Ex. 203.0.113.55 <- will be host address regardless of where |
- **CIDR**
  - Classless inter-domain routing notation
  - 203.0.113.10 / 24
- **Private IP address range**: any a org could use these and won't be route to the internet
  - 10.0.0.0 - 10.255.255.255 - Class A - 10.0.0.0/8
  - 172.16.0.0 - 172.31.255.255 - Class B - 172.16.0.0/12
  - 192.168.0.0 - 192.168.255.255 - Class C - 192.168.0.0/16
- Home: 127.0.0.1, doesn't go out to network
- Devices can communicate if they are in the same network
  - Otherwise they need a router to communicate
  - Ex. 192.168.10.10/24 <-> 192.168.10.100/24
    - OK b/c network portion is "192.168.10" and they are the same
  - Ex. 192.168.10.11/24 <-> 192.168.10.10/24 NEED ROUTER

### Subnetting networks

- Ex. given 10.0.0.0/8
- 255.0.0.0 -> 2^24 -2 = 16,777,214 host addresses
- -2 as 1 for network id and another for broadcast address

<br/>

## [Network layer addressing and subnetting](https://app.pluralsight.com/library/courses/network-layer-addressing-subnetting/table-of-contents)

- Ex. ISP provides 203.0.113.0/24 and we need to subnet to 8 networks
- Network portion cannot be changed
- 203.0.113.0/24 -> /24+3, need to subnet at least 3
- Given 3 bits, 8 possible networks, 6 possible hosts, as 3^2
- ![Calc subnet](/assets/calc-subnet.png)
- 2nd N: subnet, network id
- 1st H: first host address
- 2nd H: last host address
- B: broadcast address
- Then you can convert these to decimal to show all possible ranges
- Calculating network 1 ip, the right most blue 0 becomes 1
- Then, all possible hosts of network 1 is 01| 00001 <-> 11110
- Network 2 is, 10 | green 0s. Same possible hosts

### Router

- Given 10.0.0.0/24, divide into 2 networks
- 10.0.0.0/25
- N1: 10.0.0.0 /25
- N2: 10.0.0.1 /25
- 10.0.0.[64,32,16,8,4,3,2,1] = 10.0.0.128
- Router job: move traffic between unique IP networks
- 10.0.0.0/25 <-> 10.0.0.128/25 ?

<br/>

## [Introduction to Enterprise Network Infrastructure](https://app.pluralsight.com/library/courses/network-enterprise-infrastructure-introduction-cert/table-of-contents)

### Routing IP Traffic

- ![Default gateway](/assets/default-gateway.png)
- 10.0.0.10 tries to get data from 192.168.10.8
- Pass red switch
- Into blue router with IP routes

| C - connected   | to what network |
| --------------- | --------------- |
| 10.0.0.0/24     | F0/0            |
| 192.168.10.0/24 | F0/1            |

### Building routing tables

- ![Building routing tables](/assets/build-routing-table.png)
- Router A connects green / orange
  - Add that it knows how to raech router B
  - since router B can reach router C, add that A can reach C
- Minus 1 TTL per move
- `$ tracert 8.8.8.8 # see routing table to google.com`
