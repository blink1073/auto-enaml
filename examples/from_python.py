#----------------------------------------------------------------------------
#
#  Copyright (c) 2013-14, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in /LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#
#----------------------------------------------------------------------------
from enaml.qt.qt_application import QtApplication
from atom.api import (Atom, Bool, Enum, Float, Int, Str, Long, Coerced,
                      Range, Unicode, FloatRange, observe, List, Dict, Tuple)
from auto_enaml import auto_window, auto_view, auto_item


class AllTypes(Atom):
    """ A simple class with all kinds of traits

    """
    boolean_value = Bool(True)
    int_value = Int(42)
    float_value = Float(3.141592)
    enum_value = Enum("foo", "bar", "baz", "qux")
    int_range_value = Range(0, 10)
    long_value = Long(10)
    float_range_value = FloatRange(0.0, 1.0)
    uni_value = Unicode("Word")
    str_value = Str("Hello")
    coerced_value = Coerced(int)
    list_value = List(default=[1, 3, 4])
    dict_value = Dict(default=dict(a=1, b=2))
    tuple_value = Tuple(default=(1, 2, 3))

    _my_float = Float()

    @observe('boolean_value', 'int_value', 'float_value', 'enum_value')
    def something_changed(self, change):
        print change
        self.float_range_value *= 0.9


if __name__ == '__main__':
    all = AllTypes()
    app = QtApplication()
    view = auto_view(all, 
                     'boolean_value',
                     auto_item('uni_value', tool_tip='Hey There'))
    win = auto_window(view)
    win.show()

    # what we need now is View and Item replacements

    app.start()
