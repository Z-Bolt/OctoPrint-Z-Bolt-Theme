# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask
import socket



class zboltthemePlugin(octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.SimpleApiPlugin,
                    octoprint.plugin.StartupPlugin):

    def __init__(self):
        hostname = socket.gethostname() + ".local"
        self.printer_name = [hostname]

    def get_settings_defaults(self):
        return dict(
            webcam=dict(
                enabled=False
                )
        )

    def get_assets(self):
        return dict(
            less=['less/theme.less'],
            js=['js/zbolttheme.js'],
            css=['css/main.css', 'css/theme.css']
        )

    def get_api_commands(self):
        return dict(
            update_printer_name=[]
        )

    def on_api_command(self, command, data):
        if command == "update_printer_name":
            self.printer_name = data.get("printer_name")
            self._plugin_manager.send_plugin_message(
                self._identifier, dict(printer_name=self.printer_name))

    def on_api_get(self, request):
        return flask.jsonify(printer_name=self.printer_name)

    def get_template_configs(self):
        return [
            dict(type="settings", name="Z-Bolt",
                 data_bind="visible: loginState.isAdmin()"),
        ]

    ##~~ Softwareupdate hook
    def get_update_information(self):
        return dict(
        zbolttheme=dict(
            displayName = "Z-Bolt Theme",
            displayVersion = self._plugin_version,

            type="github_release",
            user="Z-Bolt",
            repo="OctoPrint-zbolttheme",
            current=self._plugin_version,

            pip="https://github.com/Z-Bolt/OctoPrint-Z-Bolt-Theme/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Z-Bolt Theme"

def __plugin_load__():
    global __plugin_implementation__    
    __plugin_implementation__ = zboltthemePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config":__plugin_implementation__.get_update_information
    }
