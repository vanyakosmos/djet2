from django.conf import settings

# Theme
JET_DEFAULT_THEME = getattr(settings, 'JET_DEFAULT_THEME', 'default')
JET_THEMES = getattr(settings, 'JET_THEMES', [])

# Side menu
JET_SIDE_MENU_CLS = getattr(settings, 'JET_SIDE_MENU_CLS', 'jet.sidebar.Sidebar')
JET_SIDE_MENU_COMPACT = getattr(settings, 'JET_SIDE_MENU_COMPACT', False)
JET_SIDE_MENU_ITEMS = getattr(settings, 'JET_SIDE_MENU_ITEMS', None)

# Improved usability
JET_CHANGE_FORM_SIBLING_LINKS = getattr(settings, 'JET_CHANGE_FORM_SIBLING_LINKS', True)
