from time import sleep
import os

class Viewer:
    def __init__(self, frames, fps, **meta):
        self.frames = frames

        for attr in meta.keys():
            self.__dict__[attr] = meta[attr]

    def _view_frame(frame):
        os.system('cls')

        body = ''

        for row in frame:
            body += '\n' + ''.join(row)

        print(body)

    def view():
        for frame in frames:
            self._view_frame(frame)
            sleep(1/fps)
