import sublime, sublime_plugin
import os

MELD_BIN_PATH = '/usr/bin/meld'

class MeldDiffCommand(sublime_plugin.WindowCommand):
    def run(self, files):
        if len(files) != 2:
            return
        os.system('%s "%s" "%s" &' %(MELD_BIN_PATH, files[0], files[1]))