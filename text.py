# -*- coding: UTF-8 -*-
# Copyright (C) 2010 Hervé Cauwelier <herve@itaapy.com>
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

from ikaaro.registry import register_resource_class
from ikaaro.text import CSS as BaseCSS

from edit_area import ea_widget



############################################################
# EditArea edit view (mix CSS_Edit and HTMLEditView)
############################################################

class CSS_Edit(Text_Edit):
    """Code editor view using the EditArea instead of a basic textarea or
    the WYSIWYG tinyMCE (that cannot edit source directly as far as I known
    [Armel])."""

    schema = merge_dicts(File_Edit.schema, data=String)

    widgets = [
        timestamp_widget,
        ea_widget]

    title = "Edit CSS file"



class CSS(BaseCSS):
    edit = CSS_Edit()



# Overwrite class for 'text/css'
# Maybe automatic
register_resource_class(CSS)

