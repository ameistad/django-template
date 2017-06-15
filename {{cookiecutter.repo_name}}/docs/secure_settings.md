# Notes on secure settings used

- Security middleware is removed and all necessary headers are set by Caddy which the official Django documentation recommends. See: https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.security

- No X-Frame-Option headers are set in Caddy and X-Frame-Options middleware is removed from settings. This is taken care of the content security policy frame-ancestors 'none' set in the Caddyfile. See: https://www.w3.org/TR/CSP2/#frame-ancestors-and-frame-options
