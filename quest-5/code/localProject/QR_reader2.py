from PIL import Image
from pyzbar.pyzbar import decode
import time
import numpy as np

loaded_array = np.load('my_array.npy')

data = decode(loaded_array)
if(data == []):
    print("not a QR")
else:
    print(data[0].data.decode('utf-8'))
    
time.sleep(.25)
#send_udp_data(data[0].data.decode('utf-8'));




