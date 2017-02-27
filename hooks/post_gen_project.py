#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple script to rename .env.keep to .env after generating the project.
"""

import os

os.rename('.env.keep', '.env')

print('Django project was generated in {{ cookiecutter.repo_name }}.')
