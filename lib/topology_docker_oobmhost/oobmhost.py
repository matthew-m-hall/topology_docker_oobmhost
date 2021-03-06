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

from topology_docker.node import DockerNode
from topology_docker.shell import DockerBashShell


class OobmHostNode(DockerNode):
    """
    Modified host node for the Topology Docker platform engine.

    This custom node loads a host image and has the eth0 interface

    See :class:`topology_docker.node.DockerNode`.
    """

    def __init__(self, identifier, image='ubuntu:14.04', **kwargs):

        super(OobmHostNode, self).__init__(
            identifier, image=image, network_mode='bridge', **kwargs
        )
        self._interface_counter = 0

    def notify_add_biport(self, node, biport):
        """
        Get notified that a new biport was added to this engine node.

        :param node: The specification node that spawn this engine node.
        :type node: pynml.nml.Node
        :param biport: The specification bidirectional port added.
        :type biport: pynml.nml.BidirectionalPort
        :rtype: str
        :return: The assigned interface name of the port.
        """
        if self._interface_counter == 0:
            self._interface_counter += 1
            return 'eth0'
        else:
            raise Exception(
                'Multiple interfaces not supported on host type oobmhost'
                )
        return biport.metadata.get('label', biport.identifier)

    def _register_shells(self, connectionobj):
        """
        See :meth:`CommonNode._register_shells` for more information.
        """
        connectionobj._register_shell('bash', DockerBashShell())


__all__ = ['OobmHostNode']
