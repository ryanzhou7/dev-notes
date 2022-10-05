## AWS networking

- [Skill up](https://explore.skillbuilder.aws/learn/public/learning_plan/view/89/networking-learning-plan?la=sec&sec=lp)
- [Ramp up](https://d1.awsstatic.com/training-and-certification/ramp-up_guides/Ramp-Up_Guide_Networking-Content-Delivery.pdf)

  - Intro CIDR
  - [Intro VPC](https://explore.skillbuilder.aws/learn/course/79/play/445/introduction-to-amazon-virtual-private-cloud-vpc)
    - VPC: use software to do isolated
    - Create VPC
      - VPC and more
      - public subnet and private
  - [VPC GS](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html?pg=ln&sec=hs)
    - Default VPC
      - Create a VPC with a size /16 IPv4 CIDR block (172.31.0.0/16). This provides up to 65,536 private IPv4 addresses.
      - Create a size /20 default subnet in each Availability Zone. This provides up to 4,096 addresses per subnet, a few of which are reserved for our use.
      - Create an internet gateway and connect it to your default VPC.
      - Add a route to the main route table that points all traffic (0.0.0.0/0) to the internet gateway.
      - Create a default security group and associate it with your default VPC.
      - ![Default VPC](/assets/ex-default-vpc.png)
  - [Glossary](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  - [Tutorials](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenarios-cli.html)

### Understanding CIDR Notation

- [Lab](https://explore.skillbuilder.aws/learn/course/35/play/463/understanding-cidr-notation)
- [DO](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking)

  - 123 = 1 X 100 + 2 X 10 X 2, base 10 -> base 2
  - **CIDR**: "add a specification in the IP address itself as to the number of significant bits that make up the routing or networking portion."
  - "The decimal value that comes after the slash is the number of bits consisting of the routing prefix. This in turn can be translated into a netmask, and also designates how many available addresses are in the block."
  - https://cidr.xyz/
  - ![CIDR](/assets/cidr.png)

- [DO intro to networking](https://www.digitalocean.com/community/tutorials/an-introduction-to-networking-terminology-interfaces-and-protocols)

- [Github devops resources](https://github.com/bregman-arie/devops-resources)
- [DevOps](https://github.com/Tikam02/DevOps-Guide)
- [Book of knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)
- [DevOps interview questions](https://github.com/bregman-arie/devops-exercises)

###

- [AWS VPC & Subnets For Beginners](https://www.youtube.com/watch?v=TUTqYEZZUdc)

  - How do resources communication with each other and the internet?
  - ![VPC](/assets/vpc.png)
    - 10.0.0.0/16 <- specify private IP range for the vpc, which is in a region (us-west-2). First 16 bits for network routing
  - Create subnets with CIDR blocks, ex. 10.0.1.0/24 place in AZ (us-west-2a)
  - Each resource (ec2, rds) assigned private IP address
  - All resources within the 10.0.0.0/16 VPC can communicate with each other even across AZ (ex. 2a 10.0.1.10 <-> 2b 10.0.6.0)
  - Internet gateway: how the VPC connects to the internet, you'd only give 1.10 / 4.10 access to the gateway
  - Nat gateway: to allow ec2 access out of the VPC with public access to it

- (Subnet Mask - Explained)[https://www.youtube.com/watch?v=s_Ntt6eTn94]

- [subnetting is simple] https://www.youtube.com/watch?v=ecCuyq-Wprc&list=PLSNNzog5eydueOR_p6dezKr2tosjGvdNH&index=1
  - ![Host ip range](/assets/host-id-range.png)
  - Subnet = number of subnets
  - Host = number of hosts
- [Subnetting a subnet --sunny way](https://www.youtube.com/watch?v=aVTEZHC2wdA&list=PLSNNzog5eydueOR_p6dezKr2tosjGvdNH&index=2)
- NexGenT - IPv4 Addressing
  - [Lesson 1: Binary and the IP Address MADE EASY](https://www.youtube.com/watch?v=ddM9AcreVqY)
    - Base 10 vs base 2
  - [Lesson 2: Network IDs and Subnet Masks](https://www.youtube.com/watch?v=XQ3T14SIlV4)
    - 192.168.1.0 / 24 = 24 left / most significant bits for subnet mask
    - 255.255.255.0 subnet mask = /24
    - 255.255.248.0 subnet mask = /21, = 8+8+5
      - 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
      - 128 + 64 + 32 + 16 + 8 = 248, or 255 - 7
- [Networking](https://www.youtube.com/watch?v=s_Ntt6eTn94)
  - IP address: unique ID for device in a network
  - Networking address: unique across networks has group of hosts
  - Host address: unique within the network it's in
  - ![Subnet](/assets/subnet.png)
  - ![Mask](/assets/mask.png)
  - **Subnetting**: breaking down large network into smaller ones
  - ![Why subnet](/assets/why-subnet.png)
    - If top left computer asks "who is 192.168.1.30" without subnetting all devices will receive this inquiry. With subnetting this will route to the subnet (via the router) and only those devices in that subnet will receive that message.
  - What is the minimum CIDR if you want 3 subnets?
  - ![Number of networks vs hosts](/assets/num-networks-vs-hosts.png)
    - Top most means /24, bottom most is /31
    - All 1's and 0's are reserved for the broadcast and network address hence with bottom CIDR /31 there are 0 hosts
    - Network = routing
  - ![Example subnetting](/assets/ex-subnetting.png)
    - With minimum of 3 subnet and 4 hosts in each see chart for compatible answers
  - ![Default subnetting mask](/assets/default-subnet-marks.png)
    - Default subnetting masks
