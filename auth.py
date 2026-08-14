from database.database import (
    add_user,
    check_user
)


def register_user(
    name,
    email,
    password,
    role="Employee"
):

    return add_user(
        name,
        email,
        password,
        role
    )


def login_user(
    email,
    password
):

    return check_user(
        email,
        password
    )