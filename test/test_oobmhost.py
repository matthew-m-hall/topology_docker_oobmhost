# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Tests for hosts.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division


TOPOLOGY = """
[image="ubuntu:12.04" type=oobmhost name="Host 1"] hs1
[type=oobmhost name="Host 2"] hs2
"""


def test_image(topology, step):
    """
    Test that image selection features works as expected.
    """
    hs1 = topology.get('hs1')
    hs2 = topology.get('hs2')

    issue = hs1('cat /etc/issue', shell='bash')
    assert '12.04' in issue

    issue = hs2('cat /etc/issue', shell='bash')
    assert '14.04' in issue
