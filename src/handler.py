from typing import List
from pynput.keyboard import Key, Controller

from enums import SpeedEditorKey, SpeedEditorJogLed, SpeedEditorJogMode, SpeedEditorLed


class SpeedEditorHandler:
    JOG = {
        SpeedEditorKey.SHTL: (SpeedEditorJogLed.SHTL, SpeedEditorJogMode.RELATIVE_2),
        SpeedEditorKey.JOG: (SpeedEditorJogLed.JOG, SpeedEditorJogMode.ABSOLUTE_CONTINUOUS),
        SpeedEditorKey.SCRL: (SpeedEditorJogLed.SCRL, SpeedEditorJogMode.ABSOLUTE_DEADZERO),
    }

    MAPPING_SPECIAL_KEY = {
        'arrowleft': Key.left,
        'arrowright': Key.right,
        'arrowup': Key.up,
        'arrowdown': Key.down,
        'backspace': Key.backspace,
        'delete': Key.delete,
        'end': Key.end,
        'enter': Key.enter,
        'escape': Key.esc,
        'home': Key.home,
        'pageup': Key.page_up,
        'pagedown': Key.page_down,
        'tab': Key.tab,
        # 'insert': Key.insert,
        'space': Key.space,
    }

    def emulate(self, binding):
        _binding = binding.split('+')
        _r_binding = _binding[::-1]
        if len(_binding) == 0:
            return
        for b in _binding:
            if b == 'cmd':
                self.keyboard.press(Key.cmd_l)
            elif b == 'ctrl':
                self.keyboard.press(Key.ctrl)
            elif b == 'alt':
                self.keyboard.press(Key.alt)
            elif b == 'shift':
                self.keyboard.press(Key.shift)
            else:
                self.keyboard.press(b if b not in self.MAPPING_SPECIAL_KEY else self.MAPPING_SPECIAL_KEY[b])
        for b in _r_binding:
            if b == 'cmd':
                self.keyboard.release(Key.cmd_l)
            elif b == 'ctrl':
                self.keyboard.release(Key.ctrl)
            elif b == 'alt':
                self.keyboard.release(Key.alt)
            elif b == 'shift':
                self.keyboard.release(Key.shift)
            else:
                self.keyboard.release(b if b not in self.MAPPING_SPECIAL_KEY else self.MAPPING_SPECIAL_KEY[b])

    def _set_jog_mode_for_key(self, key: SpeedEditorKey):
        if key not in self.JOG:
            return
        self.se.set_jog_leds(self.JOG[key][0])
        self.se.set_jog_mode(self.JOG[key][1])

    def __init__(self, se, bindings):
        self.se = se
        self.bindings = bindings
        self.keyboard = Controller()
        self.keys = []
        self.leds = 0
        self.se.set_leds(self.leds)
        self._set_jog_mode_for_key(SpeedEditorKey.SHTL)

        self.relative_count = 0
        self.relative_dead_speed = 320
        self.relative_speed = 1024
        self.relative_max_speed = 10

        self.absolute_min = 0
        self.absolute_max = 255

    def select_back(self, character_count):
        for _ in range(character_count):
            self.emulate('shift+arrowleft')

    def handle_absolute_jog(self, value):
        nbr_values = self.absolute_max - self.absolute_min
        type_value = str(int((value + 4096) * nbr_values / 8192))
        val_length = len(type_value)
        self.keyboard.type(type_value)
        self.select_back(val_length)

    def handle_relative_jog(self, value):
        if abs(value) < self.relative_dead_speed:
            return
        self.relative_count += value
        print(self.relative_count)
        if abs(self.relative_count) < self.relative_speed:
            return
        is_right = self.relative_count > 0
        action_count = abs(self.relative_count) // self.relative_speed
        action_count = action_count if action_count < self.relative_max_speed else self.relative_max_speed
        self.relative_count = self.relative_count % self.relative_speed
        key = SpeedEditorKey.WHEEL_RIGHT.real if is_right else SpeedEditorKey.WHEEL_LEFT.real
        binding = self.bindings.get(str(key), None)
        if binding:
            for _ in range(action_count):
                self.emulate(binding)

    def jog(self, mode: SpeedEditorJogMode, value):
        if mode == SpeedEditorJogMode.RELATIVE_0 or mode == SpeedEditorJogMode.RELATIVE_2:
            self.handle_relative_jog(value)
        else:
            self.handle_absolute_jog(value)

    def key(self, keys: List[SpeedEditorKey]):
        for k in keys:
            if k not in self.keys:
                binding = self.bindings.get(str(k.real), None)
                if binding:
                    self.emulate(binding)

        # Find keys being released and toggle led if there is one
        for k in self.keys:
            if k not in keys:
                # Select jog mode
                self._set_jog_mode_for_key(k)

                # Toggle leds
                self.leds ^= getattr(SpeedEditorLed, k.name, 0)
                self.se.set_leds(self.leds)

        self.keys = keys

    def battery(self, charging: bool, level: int):
        """
        charging [False/True] Is currently charging
        level    [0-100]      Current charge lvel
        """
        print(f"Battery {level:d} %{' and charging' if charging else '':s}")
