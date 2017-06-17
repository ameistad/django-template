# Folder structure

__apps__
Put django-admin startapp content here.

```sh
$ django-admin startapp my_app apps
```

__config__
The approach in this template is to divide settings in different files and put them in the settings folder.

- `base.py` - common settings for all environments. Every file below imports from this with `from .base import *`.
- `development.py` - settings only used when developing.
- `production.py` - settings only used when the app is deployed.
- `testing.py` - testing specific settings.

You can control what settings file is loaded with the environment variable `DJANGO_SETTINGS_MODULE`.

__docker__
Files and folders for Docker.

__requirements__
Holds requirements files for the various environments.

__media__
Uploaded content from the site goes here.

__templates__
Templates that are not related to an app goes here.

__tests__
Test files that are not related to an app goes here.
