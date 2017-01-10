import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from wilt import Wilt


class Interface(Gtk.Window):

    def __init__(self, title):
        Gtk.Window.__init__(self, title=title)

        self.auth_box = Gtk.Box(spacing=6)
        self.auth_box.set_spacing(16)
        self.add(self.auth_box)

        self._user = Gtk.Entry()
        self._user.set_text('Username')
        self.auth_box.pack_start(self._user, True, True, 0)

        self._pass = Gtk.Entry()
        self._pass.set_text('Password')
        self.auth_box.pack_start(self._pass, True, True, 0)

        self._login = Gtk.Button(label='Login')
        self._login.connect('clicked', self.on_login_click)
        self.auth_box.pack_start(self._login, True, True, 0)

        self._reg = Gtk.Button(label='Register')
        self._reg.connect('clicked', self.on_reg_click)
        self.auth_box.pack_start(self._reg, True, True, 0)

        self.set_title(title)
        self.connect('delete-event', Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def on_login_click(self, widget):
        self.wilt = Wilt(self._user.get_text(), self._pass.get_text())

        if self.wilt.login():
            print('Weew!')
        else:
            print('Not logged in')

    def on_reg_click(self, widget):
        pass

I = Interface('What I Listen To')
