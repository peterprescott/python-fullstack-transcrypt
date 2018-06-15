from Component_py.stubs import require  # __:skip
from actions.actions import (
    login_form_update, clear_login_form, login_user, register_user
)
from components.LoginForm import LoginForm
connect = require("react-redux").connect


def mapStateToProps(state):
    return {
        "login_form": state["login_form"]
    }


def mapDispatchToProps(dispatch):
    return {
        "login_form_update": lambda u, p: dispatch(login_form_update(u, p)),
        "clear_login_form": lambda: dispatch(clear_login_form()),
        "do_login": lambda u, p: dispatch(login_user(u, p)),
        "register_user": lambda u, p: dispatch(register_user(u, p))
    }


LoginFormContainer = connect(
    mapStateToProps,
    mapDispatchToProps
)(LoginForm)