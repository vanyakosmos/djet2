from django.utils.translation import gettext_lazy as _

from jet.utils import get_app_list
from .base import DashboardModule


class AppList(DashboardModule):
    """
    Shows applications and containing models links. For each model "created" and "change" links are displayed.

    Usage example:

    .. code-block:: python

        from django.utils.translation import gettext_lazy as _
        from jet.dashboard import modules
        from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


        class CustomIndexDashboard(Dashboard):
            columns = 3

            def init_with_context(self, context):
                self.children.append(modules.AppList(
                    _('Applications'),
                    exclude=('auth.*',),
                    column=0,
                    order=0
                ))

    """

    title = _('Applications')
    template = 'jet.dashboard/modules/app_list.html'

    #: Specify models which should be displayed. ``models`` is an array of string formatted as ``app_label.model``.
    #: Also its possible to specify all application models with * sign (e.g. ``auth.*``).
    models = None

    #: Specify models which should NOT be displayed. ``exclude`` is an array of string formatted as ``app_label.model``.
    #: Also its possible to specify all application models with * sign (e.g. ``auth.*``).
    exclude = None
    hide_empty = True

    def settings_dict(self):
        return {
            'models': self.models,
            'exclude': self.exclude
        }

    def load_settings(self, settings):
        self.models = settings.get('models')
        self.exclude = settings.get('exclude')

    def init_with_context(self, context):
        app_list = get_app_list(context)
        app_to_remove = []

        for app in app_list:
            app_name = app.get('app_label', app.get('name', ''))
            app['models'] = filter(
                lambda model: self.models is None or ('%s.%s' % (app_name, model['object_name'])) in self.models or (
                        '%s.*' % app_name) in self.models,
                app['models']
            )
            app['models'] = filter(
                lambda model: self.exclude is None or (
                        ('%s.%s' % (app_name, model['object_name'])) not in self.exclude and (
                            '%s.*' % app_name) not in self.exclude),
                app['models']
            )
            app['models'] = list(app['models'])

            if self.hide_empty and len(list(app['models'])) == 0:
                app_to_remove.append(app)

        for app in app_to_remove:
            app_list.remove(app)

        self.children = app_list
