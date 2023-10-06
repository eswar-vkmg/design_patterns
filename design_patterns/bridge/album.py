class Album:
    def __init__(self, name, desc):
        self.album_name = name
        self.description = desc

    def get_album_name(self):
        return self.album_name

    def get_album_description(self):
        return self.description
