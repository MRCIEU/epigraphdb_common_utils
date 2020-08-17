from pprint import pformat
from textwrap import dedent
from typing import Any, Optional

import environs

env = environs.Env()
env.read_env()


class EnvVar:
    def __init__(
        self,
        name: str,
        default: Optional[Any] = None,
        secret: bool = False,
        type=str,
        desc: Optional[str] = None,
        environs_env: environs.Env = env,
    ):
        """A construct for an environment variable.

        - name: Name of the environment variable
        - default: Default value
        - secret: If True, when this env var is displayed / printed, it will
                  only show a small proportion (first 3 characters)
        - type: Object type of the env var to be coerced into,
          default to str
        - desc: Description.
        - environs_env: An instantiated environs.Env object from which the
                        env var value is retrieved
        """

        self.name = name
        self.default = default
        self.secret = secret
        self.desc = desc
        self.env = environs_env

        # Process values
        self.use_default: bool = True
        self.value = self.default
        value_init = self.env(self.name, self.default)
        if value_init is not None:
            self.value = value_init
            self.use_default = False
        self.value_display = self.value
        if self.secret:
            self.value_display = str(self.value)[:3] + "******"

    def __repr__(self):
        header_section = "variable: {name}\n{desc}\n".format(
            name=self.name,
            desc=dedent(self.desc).strip() if self.desc is not None else "",
        )
        value_section = "value: {value}\tdefault: {default}\n".format(
            value=self.value_display, default=self.default
        )
        rest_section = "{secret}".format(
            secret="Secrect" if self.secret else ""
        )
        if rest_section != "":
            rest_section += "\n"
        message = f"{header_section}{value_section}{rest_section}---\n"
        return message


class EnvConfigs:
    """A construct to store environment variables used by an instance
    (e.g. api, docker container), and its keyword args should be
    EnvVar objects.

    When printed, it will mask secret variables. Use `[]` to get the
    actual value.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, key: str):
        return getattr(self, key).value

    def __repr__(self):
        return pformat(vars(self))
