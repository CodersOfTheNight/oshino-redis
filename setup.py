#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

from oshino_redis.version import get_version


setup(name="oshino_redis",
      version=get_version(),
      description="...",
      author="zaibacu",
      packages=["oshino_redis"],
      install_requires=["oshino", "aioredis"],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=["pytest-runner"]
      )
