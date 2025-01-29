import os
import sys

import requests


def yank_release(package_name, version, api_token):
    """
    Yank a specific version of a package on PyPI.

    :param package_name: Name of the package on PyPI
    :param version: Version number to yank
    :param api_token: PyPI API token with necessary permissions
    """
    url = f"https://pypi.org/pypi/{package_name}/{version}/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    data = {
        "yanked": True,
        "message": "Release yanked due to tag deletion."
    }

    response = requests.patch(url, json=data, headers=headers, auth=(api_token, ''))

    if response.status_code == 200:
        print(f"Successfully yanked {package_name}=={version} on PyPI.")
    else:
        print(f"Failed to yank {package_name}=={version} on PyPI.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        sys.exit(1)


def main():
    package_name = os.getenv("PACKAGE_NAME")
    version = os.getenv("VERSION")
    api_token = os.getenv("PYPI_API_TOKEN")

    if not all([package_name, version, api_token]):
        print("Error: PACKAGE_NAME, VERSION, and PYPI_API_TOKEN must be set.")
        sys.exit(1)

    yank_release(package_name, version, api_token)


if __name__ == "__main__":
    main()
