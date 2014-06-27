#
# (C) Copyright 2013 Enthought, Inc., Austin, TX
# All right reserved.
#
# This file is open source software distributed according to the terms in
# LICENSE.txt
#
import enaml
from utils import _MInfo, _Partial

with enaml.imports():
    from auto_editors import AutoItem, _AutoView, _AutoWindow


def auto_item(info,  **kwargs):
    if isinstance(info, str):
        return _Partial(info, **kwargs)
    if isinstance(info, tuple) and len(info) == 2:
        info = _MInfo(*info)
    if not isinstance(info, _MInfo):
        raise TypeError('"info" must be a str, a 2-tuple of (model, name) or '
                        'an MInfo object')
    return AutoItem(minfo=info, **kwargs)


def auto_view(model, *objects, **kwargs):
    """ Generate a view directly from an `Atom` instance.
    """
    objects = list(objects)
    for (ind, obj) in enumerate(objects):
        if isinstance(obj, str):
            objects[ind] = auto_item((model, obj))
        elif isinstance(obj, _Partial):
            objects[ind] = auto_item((model, obj.name), **obj.kwargs)
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
