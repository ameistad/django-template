#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hook to rename development.keep to development.env
after generating the project.
"""

import os


repo_dir = './config/settings'
old_env_file = os.path.join(repo_dir, 'development.keep')
new_env_file = os.path.join(repo_dir, 'development.env')

os.rename(old_env_file, new_env_file)

print("Django project was generated in {{ cookiecutter.repo_name }}.")
