import commands
from devices import Light, Fan
from remote_control import RemoteControl

if __name__ == '__main__':
    light = Light('Living-room light')
    light_on = commands.LightOnCommand(light)
    light_off = commands.LightOffCommand(light)

    fan = Fan('Living-room fan')
    fan_on = commands.FanOnCommand(fan)
    fan_off = commands.FanOffCommand(fan)
    fan_faster = commands.FanFasterCommand(fan)
    fan_slower = commands.FanSlowerCommand(fan)

    remote_control = RemoteControl(num_slots=3)
    remote_control.set_command(slot_num=0, on_command=light_on, off_command=light_off)
    remote_control.set_command(slot_num=1, on_command=fan_on, off_command=fan_off)
    remote_control.set_command(slot_num=2, on_command=fan_faster, off_command=fan_slower)

    print(remote_control)

    remote_control.press_on_button(0)
    remote_control.press_on_button(1)
    remote_control.press_undo_button()
    remote_control.press_off_button(0)
    remote_control.press_undo_button()

    remote_control.press_on_button(1)
    remote_control.press_on_button(2)
    remote_control.press_on_button(2)
    remote_control.press_on_button(2)
    remote_control.press_off_button(2)
    remote_control.press_undo_button()
    remote_control.press_off_button(1)
