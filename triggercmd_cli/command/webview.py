import gi
import sys
import os
from typing import Tuple

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2

gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator


class PythonWebView:
    def __init__(self, url, background: bool = False, methods: dict = None, methods_args: Tuple[tuple] = None):
        self.url = url
        self.window = None
        self.background = background
        if not methods:
            self.methods = dict()
        else:
            self.methods = methods
        if not methods_args:
            self.methods_args = tuple()
        else:
            self.methods_args = methods_args

        for method in self.methods.get("create"):
            method()
        if not self.background:
            self.init_window()
            self.background = False

    def init_window(self, *args, **kwargs):
        if not self.window:
            self.window = Gtk.Window()
            self.wview = WebKit2.WebView()
            self.wview.load_uri(self.url)
            self.window.resize(411, 731)
            self.window.add(self.wview)
            self.window.show_all()
            self.window.connect('delete-event',self.quit_gui)

    def output(self, *args):
        print(args)

    def quit_gui(self, *args):
        self.window = None

    def quit_menu(self, *args):
        for method in self.methods.get("quit"):
            method()
        sys.exit()
        
    def show_window(self, *args, **kwargs):
        if self.window:
            self.window.show_all()

    def tray_indicator(self, *args, **kwargs):
        indicator = appindicator.Indicator.new("TriggerCMD Agent", "/home/gustavo/Imagens/icontriggercmd.png", appindicator.IndicatorCategory.APPLICATION_STATUS)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        indicator.set_menu(self.create_menu())
        Gtk.main()

    def create_menu(self, *args, **kwargs):
        self.menu = Gtk.Menu()

        command_one = Gtk.MenuItem('TRIGGERcmd')
        command_one.connect('activate', self.init_window)
        self.menu.append(command_one)

        exittray = Gtk.MenuItem('Exit')
        exittray.connect('activate', self.quit_menu)
        self.menu.append(exittray)

        self.menu.show_all()
        return self.menu

    def run(self):
        self.tray_indicator()
        Gtk.main()
