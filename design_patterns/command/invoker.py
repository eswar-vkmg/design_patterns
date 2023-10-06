from command import Command


class RemoteControl:
    def __init__(self, command_top: Command, command_down: Command):
        self.command_top = command_top
        self.command_down = command_down

    def click_top(self):
        print('Clicked Top button')
        self.command_top.execute()

    def click_down(self):
        print('Clicked Down Button')
        self.command_down.execute()
