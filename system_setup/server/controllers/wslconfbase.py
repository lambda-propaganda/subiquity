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

import attr

from subiquitycore.context import with_context

from subiquity.common.apidef import API
from subiquity.common.types import WSLConfigurationBase
from subiquity.server.controller import SubiquityController

log = logging.getLogger('subiquity.server.controllers.wsl_configuration_base')


class WSLConfigurationBaseController(SubiquityController):

    endpoint = API.wslconfbase

    autoinstall_key = model_name = "wslconfbase"
    autoinstall_schema = {
        'type': 'object',
        'properties': {
            'custom_path': {'type': 'string'},
            'custom_mount_opt': {'type': 'string'},
            'gen_host': {'type': 'boolean'},
            'gen_resolvconf': {'type': 'boolean'},
            },
        'required': [],
        'additionalProperties': False,
        }

    def load_autoinstall_data(self, data):
        if data is not None:
            identity_data = WSLConfigurationBase(
                custom_path=data['custom_path'],
                custom_mount_opt=data['custom_mount_opt'],
                gen_host=data['gen_host'],
                gen_resolvconf=data['gen_resolvconf'],
            )
            self.model.apply_settings(identity_data, self.opts.dry_run)

    @with_context()
    async def apply_autoinstall_config(self, context=None):
        pass

    def make_autoinstall(self):
        r = attr.asdict(self.model.wslconfbase)
        return r

    async def GET(self) -> WSLConfigurationBase:
        data = WSLConfigurationBase()
        if self.model.wslconfbase is not None:
            data.custom_path = self.model.wslconfbase.custom_path
            data.custom_mount_opt = self.model.wslconfbase.custom_mount_opt
            data.gen_host = self.model.wslconfbase.gen_host
            data.gen_resolvconf = self.model.wslconfbase.gen_resolvconf
        return data

    async def POST(self, data: WSLConfigurationBase):
        self.model.apply_settings(data, self.opts.dry_run)
        self.configured()
