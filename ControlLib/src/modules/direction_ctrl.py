import ControlLib.ControlLib.src.can_adapter as can_util
import logging

# Drive Computer Core Library
# Direction Controller Module
#
# This module controls both steering and braking
#
# Hardware definition class to store messages for this module
#
# Part of the GSSM Autonomous Golf Cart
# Written by Joseph Telaak, class of 2022

class Direction_Controller:

    def __int__(self):
        # CAN Address
        self.can_address = 1

        # Setup the message logging
        self.logger = logging.getLogger("direction_controller")
        file_handler = logging.FileHandler("logs/direction_ctrl.log")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        self.logger.addHandler(file_handler)
    
    # ----------------------------
    # Steering Motor Controller
    # ----------------------------

    # Disable Steering Motor
    def str_disable(self):
        self.logger.debug("Disabling Steering Motor")
        return f"({self.can_address}) 10 1 10 1 0 0 0 0"

    # Enable Steering Motor
    def str_enable(self):
        self.logger.debug("Enabling Steering Motor")
        return f"({self.can_address}) 10 1 10 2 0 0 0 0"

    def str_reqStatus(self):
        self.logger.debug("Requesting the Steering Motor Status")
        return f"({self.can_address}) 12 1 10 0 0 0 0"

    # Run Motor Forwards
    def str_left(self, power = 255):
        self.logger.debug(f"Running Steering Motor Forwards, Power: {power}")
        return f"({self.can_address}) 10 1 12 1 {power} 0 0 0"

    # Run Motor Backwards
    def str_right(self, power = 255):
        self.logger.debug(f"Running Steering Motor Backwards, Power: {power}")
        return f"({self.can_address}) 10 1 12 2 {power} 0 0 0"

    def str_goTo(self, postion, power = 255):
        self.logger.debug(f"Running to Postion {postion} at {power}")
        return f"({self.can_address}) 11 1 {can_util.sixteentoeight_coarse(postion)} {can_util.sixteentoeight_fine(postion)} {power} 0 0 0"

    # Request the steering motor position
    def str_reqPos(self):
        self.logger.debug("Requesting to Current Steering Motor Position")
        return f"({self.can_address}) 12 1 16 0 0 0 0"

    # ----------------------------
    # Steering Wheel Input
    # ----------------------------

    def wheel_reqPos(self):
        self.logger.info("Requesing Steering Wheel Change")
        return f"({self.can_address}) 12 1 15 0 0 0 0 0"

    # ----------------------------
    # Brake Motor Controller
    # ----------------------------

    # Disable Brake Motor
    def brk_disable(self):
        self.logger.debug("Disabling Brake Motor")
        return f"({self.can_address}) 10 2 10 1 0 0 0 0"

    # Enable Steering Motor
    def brk_enable(self):
        self.logger.debug("Enabling Brake Motor")
        return f"({self.can_address}) 10 2 10 2 0 0 0 0"

    def brk_reqStatus(self):
        self.logger.debug("Requesting the Brake Motor Status")
        return f"({self.can_address}) 12 2 10 0 0 0 0"

    # Run Motor Forwards
    def brk_pull(self, power = 255):
        self.logger.debug(f"Running Brake Motor Forwards, Power: {power}")
        return f"({self.can_address}) 10 2 12 1 {power} 0 0 0"

    # Run Motor Backwards
    def brk_push(self, power = 255):
        self.logger.debug(f"Running Brake Motor Backwards, Power: {power}")
        return f"({self.can_address}) 10 2 12 2 {power} 0 0 0"

    # Request the steering motor position
    def brk_reqPos(self):
        self.logger.debug("Requesting to Current Brake Motor Position")
        return f"({self.can_address}) 12 2 16 0 0 0 0"