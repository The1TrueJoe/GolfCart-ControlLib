# ControlLib

Python Library to enable control over the golf cart

# Usage

Usage examples

### Send Message

Sends a message directly through the CAN Adapter, bypassing the MyCart object

```python
# Import CAN Adapter
from ControlLib.ControlLib.src.can_adapter import CAN_Adapter

# Import list of raw messages
import ControlLib.ControlLib.src.raw.can_messages as msg

# Setup adapter
adapter = CAN_Adapter(serial_port="\dev\ttyACM0")

# Write same CAN Message 3 different ways
self.can.write(msg.honk)
self.can.write("(2) 11 1 0 0 0 0 0 0")
self.can.write(id = 0, data = {11, 1, 0, 0, 0, 0, 0, 0})
```