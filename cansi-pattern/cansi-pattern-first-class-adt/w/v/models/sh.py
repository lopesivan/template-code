import errno
import os


class Sh(object):

    """Shell scripts mkdir -p dir"""

    def __init__(self, Dir):
        """TODO: to be defined1.

        :Dir: TODO

        """
        self._Dir = Dir

    def mkdir(self):
        if not os.path.exists(self._Dir):
            try:
                os.makedirs(self._Dir)
            except:
                raise OSError(
                    "Can't create destination directory (%s)!" % (self._Dir))

