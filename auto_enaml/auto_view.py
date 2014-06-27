#
# (C) Copyright 2013 Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is open source software distributed according to the terms in
# LICENSE.txt
#
import enaml
from utils import MInfo, _Partial

with enaml.imports():
    from auto_editors import AutoItem, _AutoView, _AutoWindow


def auto_item(info,  **kwargs):
    if isinstance(info, str):
        return _Partial(info, **kwargs)
    if not isinstance(info, MInfo):
        raise TypeError('"info" must be a str or an MInfo object')
    return AutoItem(minfo=info, **kwargs)


def auto_view(model, *objects, **kwargs):
    """ Generate a view directly from an `Atom` instance.
    """
    objects = list(objects)
    for (ind, obj) in enumerate(objects):
        if isinstance(obj, str):
            objects[ind] = auto_item(MInfo(model, obj))
        elif isinstance(obj, _Partial):
            minfo = MInfo(model, obj.name)
            objects[ind] = auto_item(minfo, **obj.kwargs)
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
