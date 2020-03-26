import platform as pf


class OS:

    def __init__(self):
        self.platform = pf.system().lower()

    def os(self):
        if self.platform == 'linux':
            # for linux
            return self.platform

        elif self.platform == 'darwin':
            # for Mac
            return self.platform

        elif self.platform == 'windows':
            # for Windows OS
            return self.platform

        else:
            print('Only Windows is supported now.')
            raise OSError
