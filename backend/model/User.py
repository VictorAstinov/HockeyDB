from errors import BadRequest, UserAlreadyExistsError, UserNotFoundError


class User:
    def __init__(
        self,
        account_id: int = None,
        username: str = None,
        email: str = None,
        password: str = None,
        fullname: str = None,
        profile_pic: str = None,
    ):
        self.account_id = account_id
        self.username = username
        self.email = email
        self.password = password
        self.fullname = fullname
        self.profile_pic = profile_pic

        if profile_pic is None:
            self.profile_pic = "/static/default_profile_pic.png"

    def to_dict(self) -> dict:
        return {
            'account_id': self.account_id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'profile_pic': self.profile_pic,
        }

    def check_account_id(self) -> None:
        if self.account_id is None:
            raise BadRequest("Please specify the account to retrieve")
        if self.account_id is not int:
            raise BadRequest("account_id is required to be an integer")

    def get(self) -> None:
        self.check_account_id()

        # perform SQL query to fill in the rest of the user details
        # if the user does not exist then raise UserNotFoundError
        pass

    def create(self) -> None:
        if self.username is None:
            raise BadRequest("Username is a required field")
        if self.email is None:
            raise BadRequest("Email is a required field")
        if self.password is None:
            raise BadRequest("Password is a required field")
        if self.fullname is None:
            raise BadRequest("Full name is a required field")

        # perform SQL query that may raise a UserAlreadyExistsError
        # after SQL user creation get the account_id and set self.account_id
        pass

    def update(self) -> None:
        self.check_account_id()

        # perform SQL query to update user
        # if the user does not exist then raise UserNotFoundError
        # permission checking will be handled by caller
        pass

    def delete(self) -> None:
        self.check_account_id()

        # perform SQL query to delete user
        # if the user does not exist then raise UserNotFoundError
        # permission checking will be handled by caller
        pass


def search_users(username: str, fuzzy=True) -> list[User]:
    # perform a SQL fuzzy search for a certain username
    pass
