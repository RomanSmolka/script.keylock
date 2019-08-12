import xbmc
import xbmcgui
import xbmcaddon
import shutil
import urlparse
import sys

# create a class for your addon, we need this to get info about your addon
ADDON = xbmcaddon.Addon()
PATH = ADDON.getAddonInfo('path').decode('utf-8')

keymaps_dir = xbmc.translatePath("special://userdata/keymaps")

def numbInput():
	try:
		shutil.move(keymaps_dir+'/gen.xml', keymaps_dir+'/gen.xml.disabled')
		shutil.move(keymaps_dir+'/numb.xml.disabled', keymaps_dir+'/numb.xml')
		xbmc.sleep(100)
		xbmc.executebuiltin('Action(reloadkeymaps)')
	except:
		pass

def restoreInput():
	try:
		shutil.move(keymaps_dir+'/gen.xml.disabled', keymaps_dir+'/gen.xml')
		shutil.move(keymaps_dir+'/numb.xml', keymaps_dir+'/numb.xml.disabled')
		xbmc.sleep(100)
		xbmc.executebuiltin('Action(reloadkeymaps)')
	except:
		pass

class GUI(xbmcgui.WindowXMLDialog):

	def onInit(self):
		xbmc.executebuiltin('Container.SetViewMode(50)')
		self.clearList()

		numbInput()
		xbmc.sleep(100)
		self.setFocusId(1)

	def onAction(self, action):
		# xbmc.executebuiltin('Notification(Action ID, %s, 1000)'%(action.getId()))
		if action.getId() == 10:
			self.close()
		if action.getId() == 2:
			self.setFocusId(2)
			self.triggered = True
			xbmc.sleep(3200)
			self.setFocusId(1)
			self.triggered = False
		if action.getId() == 122:
			if self.triggered: 
				restoreInput()
				self.close()

action = None
if len(sys.argv) > 1: 
	args = urlparse.parse_qs(sys.argv[2][1:])
	action = args.get('action', None)

if action == 'restore':
	xbmc.log('Restoring keymap configuration gen.xml')
	restoreInput()
else:	
	ui = GUI('main.xml', PATH, 'default', '720p')
	ui.doModal()

	restoreInput()

	del ui
