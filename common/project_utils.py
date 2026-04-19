from __future__ import annotations

import os
from dotenv import load_dotenv


if not load_dotenv():
    raise FileNotFoundError("Error: .env file was not found in the project root.")


class ProjectUtils:
    @staticmethod
    def get_user_name() -> str:
        user_name = os.getenv("JENKINS_USERNAME")
        if not user_name:
            raise RuntimeError("Set JENKINS_USERNAME")

        return user_name

    @staticmethod
    def get_password() -> str:
        password = os.getenv("JENKINS_PASSWORD")
        if not password:
            raise RuntimeError("Set JENKINS_PASSWORD")

        return password

    @staticmethod
    def get_url() -> str:
        base_url = os.getenv("JENKINS_URL")
        if base_url:
            return base_url if base_url.endswith("/") else f"{base_url}/"

        host = os.getenv("JENKINS_HOST")
        port = os.getenv("JENKINS_PORT")
        if not host or not port:
            raise RuntimeError("Set JENKINS_URL or both JENKINS_HOST and JENKINS_PORT")

        return f"http://{host}:{port}/"

    @staticmethod
    def get_options() -> list[str]:
        options = os.getenv("BROWSER_OPTIONS_CHROME")
        if not options:
            raise RuntimeError("Set BROWSER_OPTIONS_CHROME")

        return [option.strip() for option in options.split(";") if option.strip()]

    @staticmethod
    def get_browser() -> str:
        browser_name = os.getenv("BROWSER_NAME")
        if browser_name != "chrome":
            raise ValueError(f"Unsupported browser '{browser_name}'. Only 'chrome' is supported.")

        return browser_name