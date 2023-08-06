import enum

# ----------------------------------------------------------------------------
# Enums for keycodes and leds
# ----------------------------------------------------------------------------

# Key Presses are reported in Input Report ID 4 as an array of 6 LE16 keycodes
# that are currently being held down. 0x0000 is no key. No auto-repeat, no hw
# detection of the 'fast double press'. Every time the set of key being held
# down changes, a new report is sent.


class SpeedEditorKey(enum.IntEnum):
    NONE = 0x00  # /

    SMART_INSRT = 0x01  # SMART INSRT [CLIP]
    APPND = 0x02  # APPND [CLIP]
    RIPL_OWR = 0x03  # RIPL O/WR
    CLOSE_UP = 0x04  # CLOSE UP [YPOS]
    PLACE_ON_TOP = 0x05  # PLACE ON TOP
    SRC_OWR = 0x06  # SRC O/WR

    IN = 0x07  # IN [CLR]
    OUT = 0x08  # OUT [CLR]
    TRIM_IN = 0x09  # TRIM IN
    TRIM_OUT = 0x0a  # TRIM OUT
    ROLL = 0x0b  # ROLL [SLIDE]
    SLIP_SRC = 0x0c  # SLIP SRC
    SLIP_DEST = 0x0d  # SLIP DEST
    TRANS_DUR = 0x0e  # TRANS DUR [SET]
    CUT = 0x0f  # CUT
    DIS = 0x10  # DIS
    SMTH_CUT = 0x11  # SMTH CUT

    SOURCE = 0x1a  # SOURCE
    TIMELINE = 0x1b  # TIMELINE

    SHTL = 0x1c  # SHTL
    JOG = 0x1d  # JOG
    SCRL = 0x1e  # SCRL

    ESC = 0x31  # ESC [UNDO]
    SYNC_BIN = 0x1f  # SYNC BIN
    AUDIO_LEVEL = 0x2c  # AUDIO LEVEL [MARK]
    FULL_VIEW = 0x2d  # FULL VIEW [RVW]
    TRANS = 0x22  # TRANS [TITLE]
    SPLIT = 0x2f  # SPLIT [MOVE]
    SNAP = 0x2e  # SNAP [=]
    RIPL_DEL = 0x2b  # RIPL DEL

    CAM1 = 0x33  # CAM1
    CAM2 = 0x34  # CAM2
    CAM3 = 0x35  # CAM3
    CAM4 = 0x36  # CAM4
    CAM5 = 0x37  # CAM5
    CAM6 = 0x38  # CAM6
    CAM7 = 0x39  # CAM7
    CAM8 = 0x3a  # CAM8
    CAM9 = 0x3b  # CAM9
    LIVE_OWR = 0x30  # LIVE O/WR [RND]
    VIDEO_ONLY = 0x25  # VIDEO ONLY
    AUDIO_ONLY = 0x26  # AUDIO ONLY
    STOP_PLAY = 0x3c  # STOP/PLAY

    WHEEL_LEFT = 0xfe  # WHEEL LEFT
    WHEEL_RIGHT = 0xff  # WHEEL RIGHT


# Setting the leds is done with SET_REPORT on Output Report ID 2
# which takes a single LE32 bitfield of the LEDs to enable

class SpeedEditorLed(enum.IntFlag):
    CLOSE_UP = (1 << 0)
    CUT = (1 << 1)
    DIS = (1 << 2)
    SMTH_CUT = (1 << 3)
    TRANS = (1 << 4)
    SNAP = (1 << 5)
    CAM7 = (1 << 6)
    CAM8 = (1 << 7)
    CAM9 = (1 << 8)
    LIVE_OWR = (1 << 9)
    CAM4 = (1 << 10)
    CAM5 = (1 << 11)
    CAM6 = (1 << 12)
    VIDEO_ONLY = (1 << 13)
    CAM1 = (1 << 14)
    CAM2 = (1 << 15)
    CAM3 = (1 << 16)
    AUDIO_ONLY = (1 << 17)


# The LEDs for the Jog mode button are on a different system ...
# Setting those leds is done with SET_REPORT on Output Report ID 4
# which takes a single 8 bits bitfield of the LEDs to enable

class SpeedEditorJogLed(enum.IntFlag):
    JOG = (1 << 0)
    SHTL = (1 << 1)
    SCRL = (1 << 2)


class SpeedEditorJogMode(enum.IntEnum):
    RELATIVE_0 = 0  # Rela
    ABSOLUTE_CONTINUOUS = 1  # Send an "absolute" position (based on the position when mode was set) -4096 -> 4096 range ~ half a turn
    RELATIVE_2 = 2  # Same as mode 0 ?
    ABSOLUTE_DEADZERO = 3  # Same as mode 1 but with a small dead band around zero that maps to 0
