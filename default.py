# -*- coding: utf-8 -*-
#------------------------------------------------------------
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.astateoftranceradio'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# Entry point
def run():
# Get params
	params = plugintools.get_params()

	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("astateoftranceradio.main_list "+repr(params))

plugintools.add_item( 
    #action="", 
    title="A State of Trance",
    url="plugin://plugin.video.youtube/playlist/PL0cWlOyqP6_PKyS76fDsafkj_ho4KLmEA/",
    thumbnail="https://yt3.ggpht.com/-bp-G-1ubrMA/AAAAAAAAAAI/AAAAAAAAAAA/lysFIFc6AaQ/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",
    folder=True )

run()