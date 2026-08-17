import time


class CorrectEmailUser():
    firstname = "Alex" + str(time.time())
    lastname = "Guest"
    email = str(time.time()) + "@fakemail.org"
    password = "Rojer101"
    birthday = "7"
    birthmonth = "July"
    birthyear = "1989"
    company = "apple"
    address = "main street 1"
    country = "Singapore"
    state = "Singapore"
    city = "Samara"
    zipcode = "123456"
    mobile_number = "+9 999 999 99 99"

class NotCorrectEmailUser():
    firstname = "Alex" + str(time.time())