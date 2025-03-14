# Copyright 2021 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import sys

from subiquity.client.client import SubiquityClient

log = logging.getLogger('system_setup.client.client')


class SystemSetupClient(SubiquityClient):

    from system_setup.client import controllers as controllers_mod

    snapd_socket_path = None

    variant = "wsl_setup"
    cmdline = sys.argv
    dryrun_cmdline_module = 'system_setup.cmd.tui'

    controllers = [
        "Welcome",
        "WSLIdentity",
        "WSLConfigurationBase",
        "Summary",
        ]

    def __init__(self, opts):
        # TODO WSL:
        # 1. remove reconfigure flag
        # 2. decide on which UI to show up based on existing user UID >=1000
        #    (or default user set in wsl.conf?)
        # 3. provide an API for this for the flutter UI to know about it
        # 4. Add Configuration Base page before Advanced
        # 5. Add language page
        # self.variant = "wsl_configuration"
        if opts.reconfigure:
            self.controllers = [
                "WSLConfigurationBase",
                "WSLConfigurationAdvanced",
                "Summary",
            ]
        super().__init__(opts)
