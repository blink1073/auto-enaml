
import enaml
from utils import MInfo, Partial

with enaml.imports():
    from auto_editors import AutoItem, PyAutoView, PyAutoWindow


def auto_item(info,  **kwargs):
    """Generate a Label-Editor combo tied to a particular `Atom` member.

    Parameters
    ----------
    info : tuple of (atom_instance, string) or a string
        If used within an auto_view, a string can be used for the member
        name.  Otherwise, a tuple with the atom_instance and the name
        must be used.
    kwargs : dictionary
        Keyword arguments to pass to the widgets.  Label-specific
        properties can be set by using a prefix (e.g. label_tooltip).
        The same is true for the editor.

    Returns
    -------
    item : AutoItem enaml instance
    """
    if isinstance(info, str):
        return Partial(info, **kwargs)
    elif isinstance(info, tuple) and len(info) == 2:
        info = MInfo(*info)
    else:
        raise TypeError('"info" must be a str, a 2-tuple of (model, name)')
    label_kwargs = {}
    editor_kwargs = {}
    for kwarg in kwargs.keys():
        if kwarg.startswith('label_'):
            label_kwargs[kwarg.replace('label_', '')] = kwargs.pop(kwarg)
        elif kwarg.startswith('editor_'):
            editor_kwargs[kwarg.replace('editor_', '')] = kwargs.pop(kwarg)
    item = AutoItem(minfo=info, **kwargs)
    for (key, value) in label_kwargs.items():
        setattr(item.label, key, value)
    for (key, value) in editor_kwargs.items():
        setattr(item.editor, key, value)
    return item


def auto_view(model, *objects, **kwargs):
    """ Generate a view directly from an `Atom` instance.

    Parameters
    ----------
    model : Instance of Atom-based class.
    objects : str or auto_items
        Arguments used to build the auto_item editors.  Can be a name
        of a member (string), or an auto_item.
    kwargs : dictionary
        Keyword arguments to pass to the view.

    Returns
    -------
    item : AutoView enaml instance
    """
    objects = list(objects)
    for (ind, obj) in enumerate(objects):
        if isinstance(obj, str):
            objects[ind] = auto_item((model, obj))
        elif isinstance(obj, Partial):
            objects[ind] = auto_item((model, obj.name), **obj.kwargs)
    return PyAutoView(objects=objects, **kwargs)


def auto_window(model, *objects, **kwargs):
    """ Generate a window directly from an `Atom` instance.

    Parameters
    ----------
    model : Instance of Atom-based class or an auto_view
    objects : str or auto_items
        Arguments used to build the auto_item editors.  Can be a name
        of a member (string), or an auto_item.
    kwargs : dictionary
        Keyword arguments to pass to the window.

    Returns
    -------
    item : AutoWindow enaml instance
    """
    if isinstance(model, PyAutoView):
        return PyAutoWindow(view=model, **kwargs)
    if not objects:
        objects = (sorted(k for k in model.members().keys()
                   if not k.startswith('_')))
    return PyAutoWindow(view=auto_view(model, *objects), **kwargs)
