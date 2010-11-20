# -*- coding: UTF-8 -*-
# Copyright (C) 2007 Henry Obein <henry@itaapy.com>
# Copyright (C) 2007-2008 Juan David Ibáñez Palomar <jdavid@itaapy.com>
# Copyright (C) 2007-2008 Nicolas Deram <nicolas@itaapy.com>
# Copyright (C) 2008 Hervé Cauwelier <herve@itaapy.com>
# Copyright (C) 2008 Sylvain Taverne <sylvain@itaapy.com>
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
from itools.xml import XMLParser
from itools.gettext import MSG
from itools.core import get_abspath
from itools.datatypes import String
from itools.web import get_context
from itools.stl import stl

# Import from ikaaro
from ikaaro.autoform import Widget, stl_namespaces


############################################################
# Forms Widget
############################################################

class EAWidget(Widget):
    """It's an EditArea Widget, for file code edit, used for edit the CSS here,
    see: <http://www.cdolivet.com>"""

    template = '/ui/editarea/ea.xml'
    scripts = ['/ui/editarea/edit_area_full.js']

    # Configuration
    width = 610
    height = 340
    readonly = False

    def ea_language(self):
        path = get_abspath('ui/editarea/langs')
        languages = [ x[:-3] for x in lfs.get_names(path) ]
        return get_context().accept_language.select_language(languages)

    def get_prefix(self):
        context = get_context()
        here = context.resource.get_abspath()
        prefix = here.get_pathto(self.template)
        return prefix

    def render(self):
         prefix = self.get_prefix()
         template = self.get_template()
         return stl(events=template, namespace=self, prefix=prefix)


###########################################################################
# Widget to reuse
###########################################################################

ea_widget = EAWidget('data', title=MSG(u'Body'))
