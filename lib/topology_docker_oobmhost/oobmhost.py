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
Custom Topology Docker Node for OpenSwitch.

    http://openswitch.net/
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from json import loads

from topology_docker.node import DockerNode
from topology_docker.utils import ensure_dir
from topology_docker.shell import DockerShell, DockerBashShell


class OobmHostNode(DockerNode):
    """
    Modified host node for the Topology Docker platform engine.

    This custom node loads a host image and has the eth0 interface

    See :class:`topology_docker.node.DockerNode`.
    """

    def __init__(self, identifier, image='ubuntu:latest', **kwargs):

        super(OobmHostNode, self).__init__(
            identifier, image=image, network_mode='bridge', **kwargs
        )
        self._shells['bash'] = DockerBashShell(
            self.container_id, 'bash'
        )


__all__ = ['OobmHostNode']
