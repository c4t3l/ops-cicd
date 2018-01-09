# Tests for minion formula

'''
##################################################################################
# This file is responsible for testing the outcomes of your states and formulas. #
# Please see https://testinfra.readthedocs.io/en/latest/ for more information    #
# on how to use testinfra.                                                       #
##################################################################################
'''

import pytest
import os

SERVICE_NAME = 'cicd'
BASE_CONFIG = ''
YUMDIR = ''

'''
# The following are just examples
# Be sure to test according to what your state is doing

# Test for existence of config file
def test_base_config_exists(host):
    config = BASE_CONFIG
    assert host.file(config).exists

# Test if item is a directory
def test_repos_d(host):
    config = YUMDIR
    assert host.file(config).is_directory

# Test if value is in file
def test_value_in_file(host):
    assert host.file(BASE_CONFIG).contains(VALUE)

# Parameterized test
@pytest.mark.parametrize('name', [
    'eog-base.repo',
    'eog-updates.repo',
    'eog-local.repo',
    'eog-epel.repo',
    'eog-updates.repo',
    'eog-mysql-community.repo',
    'eog-saltstack.repo',
    ])

def test_check_repo_files(host, name):
    config = YUMDIR + '/' + name
    assert host.file(config).exists
    
# Count the number of files in the repo
# This will fail if another repo is added without incrementing 
# the assertion value of repo_count
def test_count_repo_files(host):
    fmt_cmd = 'ls -l ' + YUMDIR + '| wc -l'
    cmd = host.run(fmt_cmd)
    repo_count = int(cmd.stdout.strip('\n')) - 1
    assert repo_count == 6

# Test if package is installed
def test_package_installed(host):
    assert host.package(PACKAGE_NAME).is_installed

# Test if service is running
def test_service_is_running(host):
    assert host.service(SERVICE_NAME).is_running
'''
