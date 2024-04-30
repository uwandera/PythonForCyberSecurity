This book comes with several code samples, demonstrating four MITRE ATT&CK techniques in each Chapter.  Before running the samples, install the required Python libraries by running pip -r requirements.txt in the folder containing requirements.txt.
The code samples (and associated files) for each Chapter are as follows:
Chapter 1
- PortScan.py
- HoneyScan.py
- DNSExploration.py
- - dns_search.txt
- HoneyResolver.py
Chapter 2
- TestDefaultCredentials.py
- - defaults.txt
- ValidAccountDetection.py
- - allowlist.txt
- - defaults.txt
- AutorunSetup.py
- - Firefox.ico
- - malicious.py
- AutorunDetection.py
Chapter 3
- WMIExecution.py
- WMIDetection.py
- TaskScheduler.py
- ScheduleTracker.py
Chapter 4
- RegAutorun.py
- - BuildExe.py
- - Firefox.ico
- - malicious.py
- DetectRegistryAutorun.py
- ChangePath.py
- DetectPathModificationRegistry.py
- DetectPathModificationEvent.py
Chapter 5
- LogonScript.py
- DetectLogonScript.py
- win32evtlog.py
- - test.py
- PythonLibraryMismatch.py
Chapter 6
- DetectAntivirusService.py
- TerminateAntivirus.py
- DecoyProcess.py
- AlternateDataStreams.py
- DetectADS.py
Chapter 7
- ChromeDump.py
- DetectLocalStateAccess.py
- NetworkCredentialSniffing.py
- - merged.pcap
- DecoyCredentials.py
Chapter 8
- UserDiscovery.py
- LastLogin.py
- DetectAdminLogin.py
- FileDiscovery.py
- - Documents\clients.csv
- - Documents\Resume.docx
- MonitorDecoyContent.py
- CreateDecoyContent.py
- - Documents\clients.csv
- - Documents\Resume.docx
Chapter 9
- RemoteServices.py
- - malicious.py
- DetectSMB.py
- - SMB.pcapng
- WebSessionCookieHijack.py
- CreateFakeCookie.py
- - CookieCleanup.py
- DetectDecoyCookies.py
- - decoyCookie.pcap
Chapter 10
- ModifyClipboard.py
- MonitorClipboard.py
- LocalEmailFiles.py
- - sample.pst
- FindEmailArchives.py
Chapter 11
- EncryptedChannelClient.py
- EncryptedChannelServer.py
- DetectEncryptedTraffic.py
- - EncryptedChannel.pcapng
- ProtocolTunnelingClient.py
- ProtocolTunnelingServer.py
- ProtocolDecoder.py
Chapter 12
- DNSExfiltrationClient.py
- DNSExfiltrationServer.py
- DetectAlternativeProtocol.py
- NonApplicationClient.py
- NonApplicationServer.py
- DetectNonApplicationProtocol.py
Chapter 13
- DataEncryption.py
- - Documents\Resume.docx
- CheckFileEntropies.py
- - Documents\Resume.docx
- AccountAccessRemoval.py
- DetectPasswordChange.py