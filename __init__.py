from flask import Blueprint

from CTFd.models import (
    Challenges,
    Flags
)
from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.flags import FlagException, get_flag_class
from CTFd.utils.uploads import delete_file
from CTFd.utils.user import get_ip
from CTFd.plugins.challenges import CHALLENGE_CLASSES
from . import monitor


class CustomChallengeClass(CHALLENGE_CLASSES["standard"]):
    @classmethod
    def attempt(cls, challenge, request):
        data = request.form or request.get_json()
        submission = data["submission"].strip()
        flags = Flags.query.filter_by(challenge_id=challenge.id).all()
        for flag in flags:
            try:
                if get_flag_class(flag.type).compare(flag, submission):
                    monitor.Monitor(challenge.id)
                    return True, "Correct"
            except FlagException as e:
                return False, str(e)
        return False, "Incorrecttttt"


def load(app):
    CHALLENGE_CLASSES["standard"] = CustomChallengeClass
    register_plugin_assets_directory(app, base_path="")
