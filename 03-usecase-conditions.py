username = "ec2-user"
password = "Devops123"

in_username = input("Please enter username:")
in_password = input("Please enter password:")

if username == in_username:
    if password == in_password:
        print("login successfull")
    else:
        print("Please enter correct password")
else:
    print("Please check user name")

    #or

if (username == in_username) and (password == in_password):
    print("Login successfull")
else:
    print("Please check uname and passwd")
