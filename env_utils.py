from pprint import pformat
from textwrap import dedent
from typing import Any, Dict, Optional

import environs
from colorama import Fore, Style

env = environs.Env()
env.read_env()


class EnvVar:
    def __init__(
        self,
        name: str,
        default: Optional[Any] = None,
        secret: bool = False,
        desc: Optional[str] = None,
        environs_env: environs.Env = env,
    ):
        """A construct for an environment variable.

        - name: Name of the environment variable
        - default: Default value
        - secret: If True, when this env var is displayed / printed, it will
                  only show a small proportion (first 3 characters)
          default to str
        - desc: Description.
        - environs_env: An instantiated environs.Env object from which the
                        env var value is retrieved
        """

        self.name = name
        self.default = default
        self.secret = secret
        self.desc = desc
        if self.desc is not None:
            self.desc = dedent(self.desc).strip()
        self.env = environs_env

        # Process values
        self.use_default: bool = True
        self.value = self.default
        if type(default) == bool:
            value_init = self.env.bool(self.name, self.default)
        elif type(default) == int:
            value_init = self.env.int(self.name, self.default)
        else:
            value_init = self.env(self.name, self.default)
        if value_init is not None:
            self.use_default = False
            self.value = value_init
        self.value_display = str(self.value)
        if self.secret and value_init is not None:
            self.value_display = str(self.value)[:3] + "******"

    def __repr__(self):
        if self.desc is not None:
            desc = Style.DIM + Fore.YELLOW + self.desc + Style.RESET_ALL
        else:
            desc = ""
        header_section = "variable: {name}\n{desc}\n".format(
            name=Style.BRIGHT + Fore.BLUE + self.name + Style.RESET_ALL,
            desc=desc,
        )
        if self.use_default:
            value_display = (
                Style.BRIGHT
                + Fore.WHITE
                + self.value_display
                + Style.RESET_ALL
            )
        else:
            value_display = (
                Style.BRIGHT
                + Fore.YELLOW
                + self.value_display
                + Style.RESET_ALL
            )
        value_section = "value: {value}\tdefault: {default}\n".format(
            value=value_display, default=self.default
        )
        rest_section = "{secret}".format(
            secret=Style.DIM + Fore.WHITE + "Secrect" + Style.RESET_ALL
            if self.secret
            else ""
        )
        if rest_section != "":
            rest_section += "\n"
        message = f"{header_section}{value_section}{rest_section}---\n"
        return message

    def configs_to_dict(self) -> Dict:
        res = {
            "name": self.name,
            "value": self.value,
            "value_display": self.value_display,
            "default": self.default,
            "desc": self.desc,
            "secret": self.secret,
        }
        return res


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

    def items(self):
        keys = list(vars(self).keys())
        res_dict = {key: getattr(self, key).configs_to_dict() for key in keys}
        return res_dict.items()
