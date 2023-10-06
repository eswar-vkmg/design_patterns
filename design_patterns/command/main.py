"""
Allows us to decouple the invoker from the receiver with the help of a command
invoker HAS-A command
command HAS-A receiver
"""

from receiver import PhilipsLight, IkeaLight
from command import TurnOnCommand, TurnOffCommand
from invoker import RemoteControl


if __name__ == "__main__":
    philips_light = PhilipsLight()
    ikea_light = IkeaLight()

    turn_on_cmd_1 = TurnOnCommand(philips_light)
    turn_off_cmd_1 = TurnOffCommand(philips_light)

    turn_on_cmd_2 = TurnOnCommand(ikea_light)
    turn_off_cmd_2 = TurnOffCommand(ikea_light)

    remote_1 = RemoteControl(turn_on_cmd_1, turn_off_cmd_1)
    remote_2 = RemoteControl(turn_on_cmd_2, turn_off_cmd_2)

    remote_1.click_top()
    remote_1.click_down()

    remote_2.click_top()
    remote_2.click_down()

