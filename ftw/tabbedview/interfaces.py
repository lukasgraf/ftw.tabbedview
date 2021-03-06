# pylint: disable=E0211, E0213
# E0211: Method has no argument
# E0213: Method should have "self" as first argument

from zope import schema
from zope.interface import Interface

try:
    from collective.quickupload.browser.interfaces import IQuickUploadCapable
except ImportError:
    QUICKUPLOAD_INSTALLED = False
else:
    QUICKUPLOAD_INSTALLED = True


class ITabbedView(Interface):
    """A type for collaborative spaces."""

    batch_size = schema.Int(title=u"Batch Size", min=1, default=50)

    timeout = schema.Int(title=u"Timeout for ajax Requests in ms",
                         min=500, default=5000)

    extjs_enabled = schema.Bool(title=u'Extjs is enabled',
                                default=False)

    dynamic_batchsize_enabled = schema.Bool(
        title=u'Display the Batch size input field.',
        default=False)

    max_dynamic_batchsize = schema.Int(
        title=u'Dynamic batchsize maximum',
        default=500,)

    quickupload_addable_types = schema.List(
        title=u'',
        description=u'Types which are addable with quickupload',
        default=["File", ],
        )


class IListingView(Interface):
    """Marker interface for listing tabs.
    """


class IGridStateStorageKeyGenerator(Interface):
    """Adapter interface for a multi adapter which provides a key for storing
    the grid state in dictstorage with. Dependending on the key the same state
    is stored for more or less tabs (shared).
    """

    def __init__(context, tabview, request):
        """The multi-adapter adapts (context, tabview, request).
        """

    def get_key():
        """Returns a string which is used for storing the state in the
        dictstorage.
        """


class IDefaultDictStorageConfig(Interface):
    """The default dict storage configuration configures `ftw.dictstorage`
    to store its data as annotations on the plone site root.
    """

    def get_annotated_object():
        """Returns the annotated object (the plone site by default).
        """

if QUICKUPLOAD_INSTALLED:
    class ITabbedviewUploadable(Interface, IQuickUploadCapable):
        """Marker interfaces"""
