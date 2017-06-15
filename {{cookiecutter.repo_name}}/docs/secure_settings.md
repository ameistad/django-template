# Notes on secure settings used

- Security middleware is removed and all necessary headers are set by Caddy which the official Django documentation recommends. See: https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.security

- X-Frame-Options middleware is removed from settings. This is taken care by Caddy with the X-Frame-Options set to DENY header and the content security policy frame-ancestors set to none. We need to set both because old browsers does not support frame-ancestors. This means that the default settings does not allow frames to be used by default.
See: https://www.w3.org/TR/CSP2/#frame-ancestors-and-frame-options  | https://docs.djangoproject.com/en/stable/ref/clickjacking/
