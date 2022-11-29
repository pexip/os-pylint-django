# pylint: disable=missing-docstring, wildcard-import, unused-wildcard-import
# flake8: noqa=F401, F403

from django.contrib.auth.models import *  # [imported-auth-user]
from django.contrib.auth.models import User  # [imported-auth-user]
from django.db import models


class PullRequest(models.Model):
    author = models.ForeignKey("auth.User", models.CASCADE)  # [hard-coded-auth-user]
