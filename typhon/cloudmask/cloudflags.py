"""Definition of flags used to distinguish different cloud states."""
import enum


class CloudFlags(enum.IntEnum):
    """Integer enum to distinguish different cloudy states. """
    CLEAR = 0
    CLOUDY = 1
    CONFIDENTLY_CLEAR = 2
    PROBABLY_CLEAR = 3
    PROBABLY_CLOUDY = 4
    CONFIDENTLY_CLOUDY = 5
