import pytest
import click

from one_click import utils


def test_dict_to_tfvars():
    sample = {
        "project_link_or_path": "~/MyName/projects/project",
        "use_github": "1",
        "use_local": "0",
    }
    utils.dict_to_tfvars(sample)


def test_py_version_to_image():
    with pytest.raises(click.BadParameter):
        utils.py_version_to_image("3.8")
        utils.py_version_to_image("3.6.3")
        utils.py_version_to_image("best_version")

    assert (
        utils.py_version_to_image("3.7")
        == "tiangolo/uwsgi-nginx-flask:python3.7"
    )
