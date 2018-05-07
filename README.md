content
* [Add django reversion](#-add-django-reversion)
* [Add django reversion compare](#-add-django-reversion-compare)
* [References](#references)

## Add django reversion

1. Install with pip: pip install django-reversion.
2. Add 'reversion' to INSTALLED_APPS.
3. Run *`python manage.py migrate`*
4. Register your models with a subclass of `reversion.admin.VersionAdmin`

```python
from django.contrib import admin
from reversion.admin import VersionAdmin

@admin.register(YourModel)
class YourModelAdmin(VersionAdmin):
    pass
```
5. Run `python manage.py createinitialrevisions`

    [Defail createinitialrevisions](https://django-reversion.readthedocs.io/en/stable/commands.html#createinitialrevisions)

## Add django reversion compare

1. `pip install django-reversion-compare`
2. `pip install diff-match-patch`
3. Change `settings.py`:

Add reversion_compare to INSTALLED_APPS in your settings.py, e.g.:

```python
INSTALLED_APPS = (
    'django...',
    ...
    'reversion', # https://github.com/etianen/django-reversion
    'reversion_compare', # https://github.com/jedie/django-reversion-compare
    ...
)
```
If you want to show reversion to admin:

```python
# Add reversion models to admin interface:
ADD_REVERSION_ADMIN=True
```

4. Change `admin.py`, Inherit from `CompareVersionAdmin` instead of `VersionAdmin` to get the comparison feature.

```python
from django.contrib import admin
from reversion_compare.admin import CompareVersionAdmin

@admin.register(YourModel)
class YourModelAdmin(CompareVersionAdmin):
    pass
```

## References
https://django-reversion.readthedocs.io/en/stable/
https://github.com/etianen/django-reversion
https://github.com/jedie/django-reversion-compare
