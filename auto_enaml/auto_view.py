
import enaml
from utils import _MInfo, _Partial

with enaml.imports():
    from auto_editors import AutoItem, _AutoView, _AutoWindow


def auto_item(info,  **kwargs):
    if isinstance(info, str):
        return _Partial(info, **kwargs)
    elif isinstance(info, tuple) and len(info) == 2:
        info = _MInfo(*info)
    else:
        raise TypeError('"info" must be a str, a 2-tuple of (model, name)')
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
