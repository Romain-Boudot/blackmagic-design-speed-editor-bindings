#!/usr/bin/env python3
# Copyright (C) 2021 Sylvain Munaut <tnt@246tNt.com>
# SPDX-License-Identifier: Apache-2.0
# Edited

from bmd import SpeedEditor
from handler import SpeedEditorHandler

if __name__ == '__main__':
    se = SpeedEditor()
    se.authenticate()
    se.set_handler(SpeedEditorHandler(se))

    while True:
        se.poll()
