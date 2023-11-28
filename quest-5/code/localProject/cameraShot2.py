#!/usr/bin/python3

# Capture a JPEG while still running in the preview mode. When you
# capture to a file, the return value is the metadata for that image.

import time

from picamera2 import Picamera2, Preview
from libcamera import controls

picam2 = Picamera2()
picam2.options["compress_level"] = 6

picam2.camera_controls
picam2.configure(picam2.create_preview_configuration())

preview_config = picam2.create_preview_configuration(main={"size": (3000, 2000)})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

metadata = picam2.capture_file("QR.jpg")
print(metadata)
time.sleep(1)

picam2.close()
