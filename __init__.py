# -*- coding: UTF-8 -*-
# Copyright (C) 2007-2008 Juan David IBÁÑEZ PALOMAR <jdavid@itaapy.com>
# Copyright (C) 2008 Nicolas DERAM <nicolas@itaapy.com>
# Copyright (C) 2010 Armel FORTUN <armel@tchack.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import from itools
from itools.core import get_abspath
from itools.core import get_version

# Import from ikaaro
from ikaaro.skins import register_skin

# Import from editarea
from text import CSS

# The version
__version__ = get_version()

# Register skin
register_skin('editarea', get_abspath('ui'))
