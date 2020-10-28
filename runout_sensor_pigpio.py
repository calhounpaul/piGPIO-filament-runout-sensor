from __future__ import absolute_import, unicode_literals
import pigpio
import octoprint.plugin

class runout_sensor_pigpio(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("runout sensor check check")
        piboard = pigpio.pi()
        def runout_sensor_pigpio_cbf(GPIO, level, tick):
            self._printer.pause_print()
            self._logger.info("level change detected on 17")  
        cb = piboard.callback(17, pigpio.EITHER_EDGE, runout_sensor_pigpio_cbf)	
        piboard.set_glitch_filter(17, 500)

__plugin_name__ = "piGPIO-filament-runout-sensor"
__plugin_version__ = "0.1.0"
__plugin_description__ = "Pauses print when switch level changes"
__plugin_pythoncompat__ = ">=2.7,<4"#!/usr/bin/env python2.7
__plugin_implementation__ = runout_sensor_pigpio()
