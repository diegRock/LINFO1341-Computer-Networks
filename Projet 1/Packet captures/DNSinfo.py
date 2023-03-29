import pyshark

# Open the packet capture file
capture = pyshark.FileCapture('sameWifi/audio-samewifi-1.pcapng')

# Get some general statistics about the capture
print('Number of packets:', len(capture))
#print('Capture duration:', capture.get_tshark_retcode()[0].get('capture_duration'))

# Loop through the captured packets and extract DNS information
for packet in capture:
    if 'DNS' in packet:
        print(packet)
        continue
        print('DNS Query Name:', packet.dns.qry_name)
        print('DNS Response Code:', packet.dns.resp_code)
