
from enaml.qt.qt_application import QtApplication
from atom.api import (Atom, Bool, Enum, Float, Int, Str, Long, Coerced,
                      Range, Unicode, FloatRange, observe, List, Dict, Tuple,
                      Typed)
from matplotlib.figure import Figure 
from auto_enaml.api import auto_window, auto_view, auto_item


class AllTypes(Atom):
    """ A simple class with all kinds of traits

    """
    boolean_value = Bool(True)
    int_value = Int(42)
    float_value = Float(3.141592)
    enum_value = Enum("foo", "bar", "baz", "qux")
    int_range_value = Range(0, 10)
    long_value = Long(10)
    float_range_value = FloatRange(0.0, 1.0, value=.5)
    uni_value = Unicode("Word")
    str_value = Str("Hello")
    coerced_value = Coerced(int)
    list_value = List(default=[1, 3, 4])
    dict_value = Dict(default=dict(a=1, b=2))
    tuple_value = Tuple(default=(1, 2, 3))
    figure = Typed(Figure)

    _my_float = Float()

    @observe('boolean_value', 'int_value', 'float_value', 'enum_value')
    def something_changed(self, change):
        if change['type'] == 'create':
            return
        print change
        self.float_range_value *= 0.9

    def _default_figure(self):
        fig = Figure()
        ax = fig.subplot(111)
        ax.plot([1,2,3])
        fig.tight_layout()


if __name__ == '__main__':
    all_types = AllTypes()
    app = QtApplication()
    view = auto_view(all_types,
                     'boolean_value',
                     'str_value',
                     auto_item('uni_value', tool_tip='Hey There'),
                     auto_item('tuple_value', background='green',
                               label_tool_tip='My Label'),)
    win = auto_window(view, title='Auto Enaml Demo')
    win.show()

    app.start()
