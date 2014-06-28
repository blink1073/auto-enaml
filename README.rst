Welcome to Auto-Enaml
=====================

Auto-Enaml provides utilities for the auto generation of Enaml widgets based on Atom classes.

Simple Example::

    class Demo(Atom):
        boolean_value = Bool(True)
        str_value = Str("Hello")
        dict_value = Dict(default=dict(a=1, b=2))
        tuple_value = Tuple(default=(1, 2, 3))

    demo = Demo()
    app = QtApplication()
    view = auto_view(demo,
                     'boolean_value',
                     'str_value',
                     auto_item('tuple_value', background='green',
                               label_tool_tip='My Label'),)
    view.show()

See `the docs <http://blink1073.github.io/auto-enaml/docs>`_ for more information.

For version information, see `the Revision History <https://github.com/blink1073/auto-enaml/blob/master/releasenotes.rst>`_.
