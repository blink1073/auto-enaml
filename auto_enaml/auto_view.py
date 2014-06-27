#
# (C) Copyright 2013 Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is open source software distributed according to the terms in
# LICENSE.txt
#
import enaml

with enaml.imports():
    from auto_editors import AutoItem, _AutoView, _AutoWindow


class _Partial(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs


def auto_item(model, name=None, **kwargs):
    if not name:
        return _Partial(model, **kwargs)
    return AutoItem(model_name=(model, name), **kwargs)


def auto_view(model, *objects, **kwargs):
    """ Generate a view directly from an `Atom` instance.
    """
    objects = list(objects)
    for (ind, obj) in enumerate(objects):
        if isinstance(obj, str):
            objects[ind] = auto_item(model, obj)
        if isinstance(obj, _Partial):
            objects[ind] = auto_item(model, obj.name, **obj.kwargs)
    return _AutoView(objects=objects, **kwargs)


def auto_window(model, *objects, **kwargs):
    """ Generate a window directly from an `Atom` instance.
    """
    if isinstance(model, _AutoView):
        return _AutoWindow(view=model, **kwargs)
    if not objects:
        objects = (sorted(k for k in model.members().keys()
                   if not k.startswith('_')))
    return _AutoWindow(view=auto_view(model, *objects), **kwargs)
