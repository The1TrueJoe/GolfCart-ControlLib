# Hardware Module Tester
# Messages
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

# Direction Module: Steering
turn_left = "(1) 10 1 12 1 255 0 0 0"
turn_right = "(1) 10 1 12 2 255 0 0 0"
en_turn = "(1) 10 1 10 2 0 0 0 0"
stop_turn = "(1) 10 1 10 1 0 0 0 0"

# Direction Module: Brakes
pull_brakes = "(1) 10 2 12 1 255 0 0 0"
release_brakes = "(1) 10 2 12 2 255 0 0 0"
disable_brakes = "(1) 10 2 10 1 0 0 0 0"
enable_brakes = "(1) 10 2 10 1 0 0 0 0"

# Drive Module: Direction Control
disable = "(3) 10 10 14 1 0 0 0 0"
enable = "(3) 10 10 14 2 0 0 0 0"
forward = "(3) 10 13 1 0 0 0 0 0"
reverse = "(3) 10 13 2 0 0 0 0 0"

# Drive Module: Speed Control
accelerate = "(3) 11 10 1 0 0 0 0 0"
deccelerate = "(3) 11 10 2 0 0 0 0 0"
stop_accel = "(3) 11 10 13 0 0 0 0 0"

# Accessory Module: Accessories
right_signal_on = "(2) 10 1 1 0 0 0 0 0"
right_signal_off = "(2) 10 1 2 0 0 0 0 0"
left_signal_on = "(2) 10 2 1 0 0 0 0 0"
left_signal_off = "(2) 10 2 2 0 0 0 0 0"
tail_on = "(2) 10 4 1 0 0 0 0 0"
tail_off = "(2) 10 4 2 0 0 0 0 0"
head_on = "(2) 10 3 1 0 0 0 0 0"
head_off = "(2) 10 3 2 0 0 0 0 0"
honk = "(2) 11 1 0 0 0 0 0 0"
rear_buzz_on = "(2) 10 6 1 0 0 0 0 0"
rear_buzz_off = "(2) 10 6 1 0 0 0 0 0"