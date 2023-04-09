#%%
import pyshark

# Open the packet capture file
capture = pyshark.FileCapture('sameWifi/audio-samewifi-1.pcapng')

# Get some general statistics about the capture
print('Number of packets:', len(capture._packets))
#print('Capture duration:', capture.get_tshark_retcode()[0].get('capture_duration'))

# Loop through the captured packets and extract DNS information
count = 0
for packet in capture:
    if 'TCP' in packet:
        if 'Hypertext Transfer Protocol' in packet:
            count+=1
        continue
        print('DNS Query Name:', packet.dns.qry_name)
        print('DNS Response Code:', packet.dns.resp_code)
print("count = ", count)

# %%

# WARNING : Modification de C:\Users\Aarnor\AppData\Local\Programs\Python\Python310\Lib\site-packages\pyshark\capture\capture.py
#  Ajout du "try - except" lignes 176-183et du contenu du except pour tenir compte du changement d'asyncio.Task dans python > 3.8
#
# WARNING : Modification de C:\\Users\\Aarnor\\AppData\\Roaming\\Python\\Python310\\site-packages\\tornado\\__init__.py
#  Ajout de 
#    import nest_asyncio
#    nest_asyncio.apply()