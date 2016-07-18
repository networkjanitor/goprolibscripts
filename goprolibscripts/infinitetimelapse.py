import datetime
import time
import sys

import goprolib.HERO4.status as gp_stats
import goprolib.HERO4.HERO4 as HERO4
import goprolib.HERO4.settings as gp_settings
import goprolibscripts.remove_fisheye as gp_lc


def nightlapse_flat_iso200(h4):
    h4.set_mode(gp_stats.App.mode.MULTISHOT, gp_stats.App.sub_mode.NIGHTLAPSE)
    h4.set_setting(gp_settings.Setup.lcd.OFF)
    h4.set_setting(gp_settings.MultiShot.resolution.WIDE_12MP)
    h4.set_setting(gp_settings.MultiShot.nightlapse_rate.SEC_15)
    h4.set_setting(gp_settings.MultiShot.exposure_time.AUTO)
    h4.set_setting(gp_settings.MultiShot.protune.ON)
    h4.set_setting(gp_settings.MultiShot.protune_sharpness.HIGH)
    h4.set_setting(gp_settings.MultiShot.protune_ev.ZERO)
    h4.set_setting(gp_settings.MultiShot.protune_iso.ISO_200)
    h4.set_setting(gp_settings.MultiShot.protune_color.FLAT)
    h4.set_setting(gp_settings.MultiShot.protune_white_balance.NATIVE)

# pretty good for night
# dont use ndf on camera
def nightlapse_gpc_iso400_ndf(h4):
    h4.set_mode(gp_stats.App.mode.MULTISHOT, gp_stats.App.sub_mode.NIGHTLAPSE)
    h4.set_setting(gp_settings.Setup.lcd.OFF)
    h4.set_setting(gp_settings.MultiShot.resolution.WIDE_12MP)
    h4.set_setting(gp_settings.MultiShot.exposure_time.SEC_5)
    h4.set_setting(gp_settings.MultiShot.nightlapse_rate.SEC_10)
    h4.set_setting(gp_settings.MultiShot.protune.ON)
    h4.set_setting(gp_settings.MultiShot.protune_sharpness.HIGH)
    h4.set_setting(gp_settings.MultiShot.protune_ev.PLUS_1)
    h4.set_setting(gp_settings.MultiShot.protune_iso.ISO_400)
    h4.set_setting(gp_settings.MultiShot.protune_color.GOPRO_COLOR)
    h4.set_setting(gp_settings.MultiShot.protune_white_balance.NATIVE)

if __name__ == '__main__':
    h4 = HERO4.HERO4()
    h4.autoconfigure()
    nightlapse_gpc_iso400_ndf(h4)
    h4.shutter(True)
    print('shutter=true')
    while True:
        try:
            h4.download_all(delete_after_download=True, path='/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto')
            #gp_lc.remove_fisheye_from_folder('/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/102GOPRO/', '/media/xyoz/XYOZ-INT1000E/Pictures/2016_07_15 GoPro NDF Auto/lenscorrected/', [0.06335, -0.18432, -0.13009])
            time.sleep(30)
        except KeyboardInterrupt:
            h4.shutter(False)
            print('shutter=false')
            sys.exit(1)
        except Exception as e:
            print(e)
            print(datetime.datetime.now())

