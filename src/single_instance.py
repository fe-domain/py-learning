import os


class MusicPlayer(object):
    # record first instance of the music player
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    @classmethod
    def say_hi(self):
        print("Hi")


m = MusicPlayer()

m.say_hi()

print(__file__)
print(os.__file__)
