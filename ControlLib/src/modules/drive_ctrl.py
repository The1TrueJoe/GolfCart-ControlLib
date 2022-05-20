import logging

# Drive Computer Core Library
# Speed Controller Module
#
# This module controls the cart's built-in speed controller.
# Controls:
#   Acceleration
#   Fwd/Rev
#   Motor Control Enable
#
# Hardware definition class to store messages for this module
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

class Drive_Controller:

    def __int__(self, can_address = 3, log_messages: bool = True):
        # CAN Address
        self.can_address = can_address

        self.log_messages = log_messages
        if self.log_messages:
            # Setup the message logging
            self.logger = logging.getLogger("drive_controller")
            file_handler = logging.FileHandler("logs/drive_ctrl.log")
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
            self.logger.addHandler(file_handler)

        else:
            self.logger = None

    def setAccelPos(self, pos):
        if not self.logger == None:
            self.logger.info("Setting Accelerator Pot Position")
        return f"({self.can_address}) 10 10 10 {pos} 0 0 0 0"

    def increment(self):
        if not self.logger == None:
            self.logger.info("Incrementing Accelerator")
        return f"({self.can_address}) 11 10 1 0 0 0 0 0"

    def increment(self, count):
        if not self.logger == None:
            self.logger.info(f"Incrementing Accelerator by {count}")
        return f"({self.can_address}) 11 10 1 {count} 0 0 0 0"

    def decrement(self):
        if not self.logger == None:
            self.logger.info("Decrementing Accelerator")
        return f"({self.can_address}) 11 10 1 0 0 0 0 0"

    def decrement(self, count):
        if not self.logger == None:
            self.logger.info(f"Decrementing Accelerator by {count}")
        return f"({self.can_address}) 11 10 1 {count} 0 0 0 0"

    def reqAccelPos(self):
        self.logger.info("Requesting Accelerometer Positon")
        return f"({self.can_address}) 12 10 10 0 0 0 0 0"

    def enable(self):
        if not self.logger == None:
            self.logger.info("Enabling Digital Accelerator")
        return f"({self.can_address}) 10 10 15 2 0 0 0 0"

    def disable(self):
        if not self.logger == None:
            self.logger.info("Disabling Digital Accelerator")
        return f"({self.can_address}) 10 10 15 1 0 0 0 0"

    def reqEn(self):
        if not self.logger == None:
            self.logger.info("Requesing Enable Status")
        return f"({self.can_address}) 12 10 15 0 0 0 0 0"

    def reqPedalPos(self):
        if not self.logger == None:
            self.logger.info("Requesing Accelerator Pedal Pos")
        return f"({self.can_address} 12 10 13 0 0 0 0 0"

    def __init__(self, can_address, logger = None):
        self.logger = logger
        self.can_address = can_address

    def reverse(self):
        if not self.logger == None:
            self.logger.info("Switching to Reverse")
        return f"({self.can_address}) 10 13 1 0 0 0 0 0"

    def forwards(self):
        if not self.logger == None:
            self.logger.info("Switching to Forwards")
        return f"({self.can_address}) 10 13 2 0 0 0 0 0"

    def reqDirection(self):
        if not self.logger == None:
            self.logger.info("Requesing Direction")
        return f"({self.can_address}) 10 12 0 0 0 0 0 0"
