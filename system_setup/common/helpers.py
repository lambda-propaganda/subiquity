#!/usr/bin/env python3
# Copyright 2015-2021 Canonical, Ltd.
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

import os


def is_reconfigure(is_dryrun):
    is_dryrun_reconfigure = is_dryrun and \
        os.getenv("DRYRUN_RECONFIG") == "true"
    count = 0
    with open('/etc/passwd', 'r') as f:
        for line in f:
            # check every normal user except nobody (65534)
            if int(line.split(':')[2]) >= 1000 and \
               int(line.split(':')[2]) != 65534:
                count += 1
    is_none_dryrun_normaluser = not is_dryrun and count != 0
    return is_dryrun_reconfigure or is_none_dryrun_normaluser
