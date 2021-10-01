from commands import NoCommand


class RemoteControl:
    def __init__(self, num_slots):
        self.num_slots = num_slots
        self.on_commands = [NoCommand() for _ in range(num_slots)]
        self.off_commands = [NoCommand() for _ in range(num_slots)]
        self.last_performed_command = NoCommand()

    def set_command(self, slot_num, on_command, off_command):
        self.on_commands[slot_num] = on_command
        self.off_commands[slot_num] = off_command

    def press_on_button(self, slot_num):
        self.last_performed_command = self.on_commands[slot_num]
        self.on_commands[slot_num].execute()

    def press_off_button(self, slot_num):
        self.last_performed_command = self.off_commands[slot_num]
        self.off_commands[slot_num].execute()

    def press_undo_button(self):
        self.last_performed_command.undo()

    def __repr__(self):
        response = ''
        for current_slot in range(self.num_slots):
            response += f'{current_slot} -> {self.on_commands[current_slot]}, {self.off_commands[current_slot]}\n'
        return response
