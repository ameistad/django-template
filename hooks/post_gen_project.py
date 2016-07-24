#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hook to rename .env.keep to .env
after generating the project.
"""

import os


repo_dir = './config/settings'
old_env_file = os.path.join(repo_dir, '.env.keep')
new_env_file = os.path.join(repo_dir, '.env')

os.rename(old_env_file, new_env_file)

print("Django project was generated in {{ cookiecutter.repo_name }}.")
