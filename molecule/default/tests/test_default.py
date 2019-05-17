import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/var/lib/jenkins"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/var/lib/jenkins/config.xml"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("jenkins").exists
    assert host.user("jenkins").exists


def test_service(host):
    s = host.service("jenkins")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):

    s = host.socket("tcp://0.0.0.0:8080")
    assert s.is_listening
