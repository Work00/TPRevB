import os
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from filebrowser import FileBrowser
from generalElements.buttons.MenuButton import MenuButton
from generalElements.dropDowns.NormalDropDown import NormalDropDown
from generalElements.popups.NormalPopup import NormalPopup
from generalElements.popups.ConfirmPopup import ConfirmPopup
from screenTheme.ColorElement import ColorElement
from generalconstants import *

from kivy.lang.builder import Builder
Builder.load_string("""
<FakeButton@Label>:
    canvas.before:
        Color:
            rgba: self.background_color
        BorderImage:
            pos: self.pos
            size: self.size
            source: 'data/button.png'
    background_color: 1, 1, 1, 1
    mipmap: True
    font_size: app.text_scale
    size_hint_y: None
    height: app.button_scale

<FakeInfoLabel@Label>:
    canvas.before:
        Color:
            rgba: app.theme.info_background
        Rectangle:
            pos: self.pos
            size: self.size
    mipmap: True
    shorten: True
    shorten_from: 'right'
    font_size: app.text_scale
    size_hint_x: 1
    size_hint_max_x: self.texture_size[0] + 20
    color: app.theme.info_text


<ScreenTheme>:
    canvas.before:
        Color:
            rgba: app.theme.background
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        MainHeader:
            NormalButton:
                text: 'Back To Library'
                on_release: app.show_database()
            HeaderLabel:
                text: 'Theme Settings'
            InfoLabel:
            SettingsButton:
        BoxLayout:
            orientation: 'horizontal'
            SplitterPanelLeft:
                id: leftpanel
                #width: app.leftpanel_width
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_x: .25
                    #WideButton:
                    #    text: 'Undo Changes'
                    #    on_release: root.theme_default()
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: app.button_scale
                        WideButton:
                            text: 'Export Theme'
                            on_release: root.save_theme()
                        WideButton:
                            text: 'Import Theme'
                            on_release: root.load_theme()
                    MenuStarterButtonWide:
                        id: loadPreset
                        text: 'Load Theme Preset'
                        on_release: root.preset_drop.open(self)
                    WideButton:
                        text: 'Save Current Theme'
                        on_release: app.save_current_theme()
                    Scroller:
                        GridLayout:
                            id: colorElementHolder
                            padding: app.padding, app.padding, app.padding * 2, app.padding
                            cols: 1
                            size_hint: 1, None
                            height: self.minimum_height

                            NormalLabel:
                                text: 'Headers'
                            ColorElement:
                                color_property: 'header_main_background'
                                text: 'Main Background'
                            ColorElement:
                                color_property: 'header_text'
                                text: 'Main Text'
                            ColorElement:
                                color_property: 'info_text'
                                text: 'Info Text'
                            ColorElement:
                                color_property: 'info_background'
                                text: 'Info Background'
                            ColorElement:
                                color_property: 'header_background'
                                text: 'Sub Background'

                            MediumBufferY:
                            NormalLabel:
                                text: 'Misc'
                            ColorElement:
                                color_property: 'background'
                                text: 'Window Background'
                            ColorElement:
                                color_property: 'main_background'
                                text: 'Main Area'
                            ColorElement:
                                color_property: 'text'
                                text: 'Normal Text'
                            ColorElement:
                                color_property: 'selected'
                                text: 'Selected'
                            ColorElement:
                                color_property: 'missing'
                                text: 'Missing'
                            ColorElement:
                                color_property: 'favorite'
                                text: 'Favorite Icon'

                            MediumBufferY:
                            NormalLabel:
                                text: 'Sidebar'
                            ColorElement:
                                color_property: 'sidebar_background'
                                text: 'Background'
                            ColorElement:
                                color_property: 'sidebar_resizer'
                                text: 'Resizer'
                            ColorElement:
                                color_property: 'area_background'
                                text: 'Sub-Area'
                            ColorElement:
                                color_property: 'scroller'
                                text: 'Scrollbar Unselected'
                            ColorElement:
                                color_property: 'scroller_selected'
                                text: 'Scrollbar Selected'

                            MediumBufferY:
                            NormalLabel:
                                text: 'Buttons'
                            ColorElement:
                                color_property: 'button_down'
                                text: 'Normal Down'
                            ColorElement:
                                color_property: 'button_up'
                                text: 'Normal Up'
                            ColorElement:
                                color_property: 'button_text'
                                text: 'Button Text'
                            ColorElement:
                                color_property: 'button_warn_down'
                                text: 'Warn Down'
                            ColorElement:
                                color_property: 'button_warn_up'
                                text: 'Warn Up'
                            ColorElement:
                                color_property: 'button_toggle_true'
                                text: 'Toggle True'
                            ColorElement:
                                color_property: 'button_toggle_false'
                                text: 'Toggle False'
                            ColorElement:
                                color_property: 'button_disabled'
                                text: 'Disabled'
                            ColorElement:
                                color_property: 'button_disabled_text'
                                text: 'Disabled Text'

                            MediumBufferY:
                            NormalLabel:
                                text: 'Other Inputs'
                            ColorElement:
                                color_property: 'input_background'
                                text: 'Input Area'
                            ColorElement:
                                color_property: 'disabled_text'
                                text: 'Input Hint Text'
                            ColorElement:
                                color_property: 'slider_background'
                                text: 'Slider Background'
                            ColorElement:
                                color_property: 'slider_grabber'
                                text: 'Slider Grabber'

                            MediumBufferY:
                            NormalLabel:
                                text: 'Menus'
                            ColorElement:
                                color_property: 'button_menu_up'
                                text: 'Menu Button Up'
                            ColorElement:
                                color_property: 'button_menu_down'
                                text: 'Menu Button Down'
                            ColorElement:
                                color_property: 'menu_background'
                                text: 'Menu Background'

            BoxLayout:
                orientation: 'horizontal'
                LargeBufferX:
                BoxLayout:
                    size_hint_x: 0.5
                    orientation: 'vertical'
                    LargeBufferY:
                    BoxLayout:
                        size_hint_x: 1
                        orientation: 'vertical'
                        MainHeader:
                            HeaderLabel:
                                text: "Main Header"
                            FakeInfoLabel:
                                text: 'Info Text'
                        Header:
                            size_hint_y: None
                            height: app.button_scale
                            NormalLabel:
                                text: 'Sub-Header'
                        MainArea:
                            orientation: 'vertical'
                            SmallBufferY:
                            NormalLabel:
                                text: 'Main Area'
                            SmallBufferY:
                            BoxLayout:
                                orientation: 'horizontal'
                                LargeBufferX:
                                NormalLabel:
                                    canvas.before:
                                        Color:
                                            rgba: app.theme.selected
                                        Rectangle:
                                            pos: self.pos
                                            size: self.size
                                    size_hint: 1, 1
                                    text: 'Selected Photo'
                                LargeBufferX:
                                NormalLabel:
                                    canvas.before:
                                        Color:
                                            rgba: app.theme.missing
                                        Rectangle:
                                            pos: self.pos
                                            size: self.size
                                    size_hint: 1, 1
                                    text: 'Missing Photo'
                                LargeBufferX:
                            LargeBufferY:
                            BoxLayout:
                                orientation: 'horizontal'
                                LargeBufferX:
                                GridLayout:
                                    cols: 2
                                    NormalLabel:
                                        text: 'Favorite Icon'
                                    Widget:
                                        size_hint: None, None
                                        width: app.button_scale
                                        height: app.button_scale
                                        canvas.before:
                                            Color:
                                                rgba: app.theme.favorite
                                            Rectangle:
                                                pos: self.pos
                                                size: self.size
                                                source: 'data/star.png'
                                LargeBufferX:
                                Widget:
                                LargeBufferX:
                    LargeBufferY:
                LargeBufferX:
                BoxLayout:
                    size_hint_x: 0.5
                    orientation: 'vertical'
                    LargeBufferY:
                    SplitterPanel:
                        sizable_from: 'left'
                        min_size: self.parent.width
                        max_size: self.parent.width
                        size_hint_x: 1
                        Scroller:
                            GridLayout:
                                cols: 1
                                padding: app.button_scale / 2, app.button_scale / 2, app.button_scale / 2, app.button_scale / 2
                                size_hint_y: None
                                height: self.minimum_height
                                NormalLabel:
                                    text: "Sidebar"
                                MediumBufferY:
                                NormalLabel:
                                    canvas.before:
                                        Color:
                                            rgba: app.theme.area_background
                                        BorderImage:
                                            pos: self.pos
                                            size: self.size
                                            source: 'data/buttonflat.png'
                                    text: 'Sidebar Sub-area'
                                MediumBufferY:
                                GridLayout:
                                    size_hint_y: None
                                    cols: 2
                                    spacing: app.button_scale/2, app.button_scale/2
                                    FakeButton:
                                        color: app.theme.button_text
                                        background_color: app.theme.button_up
                                        text: 'Normal Button Up'
                                    FakeButton:
                                        color: app.theme.button_text
                                        background_color: app.theme.button_down
                                        text: 'Normal Button Down'
                                    FakeButton:
                                        color: app.theme.button_text
                                        background_color: app.theme.button_warn_up
                                        text: 'Warn Button Up'
                                    FakeButton:
                                        color: app.theme.button_text
                                        background_color: app.theme.button_warn_down
                                        text: 'Warn Button Down'
                                    FakeButton:
                                        color: app.theme.button_text
                                        background_color: app.theme.button_toggle_true
                                        text: 'Toggle Button On'
                                    FakeButton:
                                        color: app.theme.button_text
                                        background_color: app.theme.button_toggle_false
                                        text: 'Toggle Button Off'
                                    GridLayout:
                                        cols: 1
                                        size_hint_y: None
                                        height: self.minimum_height
                                        spacing: 0, app.button_scale / 2
                                        FakeButton:
                                            color: app.theme.button_disabled_text
                                            background_color: app.theme.button_disabled
                                            text: 'Disabled Button'
                                        NormalInput:
                                            hint_text: 'Input Area'
                                            cursor_color: 0, 0, 0, 0
                                            readonly: True
                                        BoxLayout:
                                            orientation: 'horizontal'
                                            size_hint_y: None
                                            height: app.button_scale
                                            ShortLabel:
                                                text: 'Slider'
                                            NormalSlider:
                                                disabled: True
                                    BoxLayout:
                                        orientation: 'vertical'
                                        size_hint_y: None
                                        height: app.button_scale * 4
                                        FakeButton:
                                            color: app.theme.button_text
                                            background_color: app.theme.button_menu_down
                                            canvas.after:
                                                Color:
                                                    rgba: 1, 1, 1, .5
                                                Rectangle:
                                                    pos: (self.pos[0]+self.width-(self.height/1.5)), self.pos[1]
                                                    size: self.height/2, self.height
                                                    source: 'data/menuarrows.png'
                                            text: 'Menu Button Down'
                                        BoxLayout:
                                            size_hint_y: None
                                            height: app.button_scale * 2
                                            orientation: 'vertical'
                                            canvas.before:
                                                Color:
                                                    rgba: app.theme.menu_background
                                                Rectangle:
                                                    size: self.size
                                                    pos: self.pos
                                                    source: 'data/buttonflat.png'
                                            NormalLabel:
                                                text: 'Menu Dropdown'
                                            FakeButton:
                                                color: app.theme.button_text
                                                background_color: app.theme.button_menu_up
                                                text: 'Menu Button Up'
                                        LargeBufferY:
                    LargeBufferY:
""")


class ScreenTheme(Screen):
    """Screen layout of the album viewer."""
    popup = None  #Holder for the screen's popup dialog
    theme_backup = {}
    filename = ''
    preset_drop = ObjectProperty()

    def drop_widget(self, fullpath, position, dropped_type='file', aspect=1):
        """Dummy function.  Here because the app can possibly call this function for any screen."""
        pass

    def text_input_active(self):
        """Detects if any text input fields are currently active (being typed in).
        Returns: True or False
        """

        input_active = False
        for widget in self.walk(restrict=True):
            if widget.__class__.__name__ == 'NormalInput' or widget.__class__.__name__ == 'FloatInput' or widget.__class__.__name__ == 'IntegerInput':
                if widget.focus:
                    input_active = True
                    break
        return input_active

    def has_popup(self):
        """Detects if the current screen has a popup active.
        Returns: True or False
        """

        if self.popup:
            if self.popup.open:
                return True
        return False

    def dismiss_popup(self, *_):
        """Close a currently open popup for this screen."""

        if self.popup:
            self.popup.dismiss()
            self.popup = None

    def dismiss_extra(self):
        """Close any running processes."""

        return False

    def key(self, key):
        """Handles keyboard shortcuts, performs the actions needed.
        Argument:
            key: The name of the key command to perform.
        """

        if self.text_input_active():
            pass
        else:
            if not self.popup or (not self.popup.open):
                pass
            elif self.popup and self.popup.open:
                if key == 'enter':
                    self.popup.content.dispatch('on_answer', 'yes')

    def on_leave(self):
        """Called when the screen is left.  Clean up some things."""

        app = App.get_running_app()

    def on_enter(self):
        """Called when the screen is entered.  Set up variables and widgets."""

        app = App.get_running_app()
        self.ids['leftpanel'].width = app.left_panel_width()

        #back up theme
        self.theme_backup = app.theme.theme_to_data(app.theme)

        #Set up preset menu
        self.preset_drop = NormalDropDown()
        for preset in themes:
            menu_button = MenuButton(text=preset['name'])
            menu_button.bind(on_release=self.set_preset)
            self.preset_drop.add_widget(menu_button)

    def set_preset(self, instance):
        """Sets the current dialog preset settings to one of the presets stored in the app.
        Argument:
            index: Integer, the index of the preset to set.
        """

        self.preset_drop.dismiss()
        app = App.get_running_app()
        for preset in themes:
            if preset['name'] == instance.text:
                app.theme.data_to_theme(preset)
                self.reload_colors()
                app.message('Reset Theme To: '+instance.text)
                break

    def load_theme(self):
        content = FileBrowser(ok_text='Load', directory_select=False, file_editable=True, export_mode=False, file='theme.txt')
        content.bind(on_cancel=self.dismiss_popup)
        content.bind(on_ok=self.load_theme_finish)
        self.popup = NormalPopup(title="Select Theme To Load", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def load_theme_finish(self, *_):
        path = self.popup.content.path
        file = self.popup.content.file
        self.dismiss_popup()
        self.filename = os.path.join(path, file)
        app = App.get_running_app()
        theme_file = self.filename
        loaded, data = app.load_theme_data(theme_file)
        if not loaded:
            app.message('Could Not Load Theme: '+str(data))
            return
        else:
            app.message('Loaded Theme: '+theme_file)
        self.theme_backup = data
        app.theme.data_to_theme(data)
        self.reload_colors()

    def save_theme(self):
        content = FileBrowser(ok_text='Save', directory_select=False, file_editable=True, export_mode=True, file='theme.txt')
        content.bind(on_cancel=self.dismiss_popup)
        content.bind(on_ok=self.save_theme_check)
        self.popup = NormalPopup(title="Select File To Save Theme To", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def save_theme_check(self, *_):
        path = self.popup.content.path
        file = self.popup.content.file
        self.dismiss_popup()
        self.filename = os.path.join(path, file)
        if os.path.isfile(self.filename):
            app = App.get_running_app()
            content = ConfirmPopup(text='Overwrite the file "'+self.filename+'"?', yes_text='Overwrite', no_text="Cancel", warn_yes=True)
            content.bind(on_answer=self.save_theme_finish)
            self.popup = NormalPopup(title='Confirm Overwrite', content=content, size_hint=(None, None), size=(app.popup_x, app.button_scale * 4), auto_dismiss=False)
            self.popup.open()
        else:
            self.save_theme_finish()

    def save_theme_finish(self, instance=None, answer='yes'):
        self.dismiss_popup()
        if answer != 'yes':
            return

        app = App.get_running_app()
        theme_file = self.filename
        data = app.theme_to_data(app.theme)
        saved = app.save_theme_data(theme_file, data)
        if saved is True:
            app.message('Saved Theme')
        else:
            app.message('Could Not Save Theme: '+str(saved))

    def reset_theme(self):
        app = App.get_running_app()
        app.theme.data_to_theme(self.theme_backup)
        self.reload_colors()

    def reload_colors(self):
        color_element_holder = self.ids['colorElementHolder']
        for widget in color_element_holder.children:
            try:
                widget.on_color_property()
                if widget.expanded:
                    widget.toggle_expanded()
            except:
                pass

    def theme_default(self, *_):
        app = App.get_running_app()
        app.theme_default()
        self.reload_colors()
