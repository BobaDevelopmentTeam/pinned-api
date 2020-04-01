
def insertUser(name: str, password: str) -> int:
    ## insertUser function takes in the name of the user
    ## and the password, which will be encrypted
    ## and the current date and inserts this into the Users Table
    ## Ideally this would be used to create a User object later on.
    pass
def deleteUser(uid: int) -> bool:
    ## deleteUser should delete a user given a unique ID pertaining
    ## to the user's ID, and should return True or False
    ## to indicate whether or not the query was successful.
    pass


def userPin(uid: int, pintype: int, img=None, *args) -> int:
    ## userPin takes in a user id and a pintype as well as an image
    pass