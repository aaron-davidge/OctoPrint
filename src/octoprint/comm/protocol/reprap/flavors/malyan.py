# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2018 The OctoPrint Project - Released under terms of the AGPLv3 License"

from octoprint.comm.protocol.reprap.flavors.generic import GenericFlavor

class MalyanFlavor(GenericFlavor):

	key = "malyan"
	name = "Malyan"

	always_send_checksum = False
	block_while_dwelling = True
	sd_always_available = True

	@classmethod
	def identifier(cls, firmware_name, firmware_info):
		return "malyan" in firmware_name.lower()
