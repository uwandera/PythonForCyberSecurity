# Objetivos de Pré-ATT&CK 
    Reconnaissance
    Resource Development -->active scanning
                         -->gather victim host information
                         -->identity information
                         -->network Information
                         -->Org Information
                         -->Phising for information
                         -->Search closed sources
                         -->Search open technical databases
                         -->search open Web Domains
                         -->Victim Owned Websites
                         --> Aquire infrastructure
                         --> Compromise Accounts
                         compromise infrastructure
                         -->develop capabilities
                         -->Establish accounts
                         -->Obtain Capabilities
                         -->Stage Capabilities
    Initial access
    Execution
    persistence
    privilege escalation
    Defense Evasion
    Credential Access
    Discovery
    lateral movement
    Collection
    Command and Control
    Exfiltration
    Inpact

#### resource development can be automated, and this stage of the attack is not visible to the defender( or is it (⌐■_■) ) 
    Python can be used for implementing a Domain Generation Algorithm(DGA) for Physhing orautomating the deployment of web-based services

#### reconnaissance can benefit from automation
    Packages like scapy and various DNS libraries
    The MITRE PRE-ATT&CK Framework includes 10 tecniques for RECONNAISSANCE, witch we'll be using: 
        Active Scanning
        Search Open Technical Databases

#### Codes for this chapter ಠ_ಠ
    PortScan.py
    HoneyScan.py
    DNSExploration.py
    Honeyresolver.py

#### Network reconnaissance can be performed by either active or passive means ╰(*°▽°*)╯
    active reconn --> interact with enviroment
        Port Scanning --> Active IP and Ports
        vunerability Scanning -- Active Services and Ports and IP's
    passive reconn --> eavesdropping on the traffic or OSINT(Open Source Intelligence)

#### Scanning networks with scapy
    SYN scan --> sends TCP SYN packets to the desired port looking for that SYN\ACK packet in the response

    DNS scan --> checks for DNS service running on the targeted system

    add the scapy library to your code (☞ﾟヮﾟ)☞

    Dont forget to install scapy dependencies (*/ω＼*)

