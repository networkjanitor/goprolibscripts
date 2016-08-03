import goprolib.HERO4.status as gp_stats

import goprolib.HERO4.HERO4 as HERO4
import goprolib.HERO4.settings as gp_settings

import time

def single_night_photo():
    h4.set_mode(gp_stats.App.mode.PHOTO, gp_stats.App.sub_mode.NIGHT_PHOTO)
    h4.set_setting(gp_settings.Setup.lcd.OFF)
    h4.set_setting(gp_settings.Photo.resolution.WIDE_12MP)
    h4.set_setting(gp_settings.Photo.exposure_time.AUTO)
    h4.set_setting(gp_settings.Photo.protune.ON)
    h4.set_setting(gp_settings.Photo.protune_sharpness.HIGH)
    h4.set_setting(gp_settings.Photo.protune_ev.ZERO)
    h4.set_setting(gp_settings.Photo.protune_iso.ISO_800)
    h4.set_setting(gp_settings.Photo.protune_color.GOPRO_COLOR)
    h4.set_setting(gp_settings.Photo.protune_white_balance.NATIVE)
    h4.shutter(True)
    
    
def single_night_multishot():
    h4.set_mode(gp_stats.App.mode.MULTISHOT, gp_stats.App.sub_mode.NIGHTLAPSE)
    h4.set_setting(gp_settings.Setup.lcd.OFF)
    h4.set_setting(gp_settings.MultiShot.nightlapse_rate.CONTINUOUS)
    h4.set_setting(gp_settings.MultiShot.resolution.WIDE_12MP)
    h4.set_setting(gp_settings.MultiShot.exposure_time.AUTO)
    h4.set_setting(gp_settings.MultiShot.protune.ON)
    h4.set_setting(gp_settings.MultiShot.protune_sharpness.HIGH)
    h4.set_setting(gp_settings.MultiShot.protune_ev.ZERO)
    h4.set_setting(gp_settings.MultiShot.protune_iso.ISO_200)
    h4.set_setting(gp_settings.MultiShot.protune_color.FLAT)
    h4.set_setting(gp_settings.MultiShot.protune_white_balance.NATIVE)
    h4.shutter(True)
    time.sleep(10)
    h4.shutter(True)
    #h4.shutter(False)


if __name__ == '__main__':
    h4 = HERO4.HERO4()
    h4.autoconfigure()
    single_night_multishot()
    
    