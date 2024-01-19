# Terminal Password Manager

This project is a terminal-based Password Manager.
Register an account with username and masterpassword. The password will saved ecrypted and hashed in a file.
Log in and add accounts or get the password from a choosen account.

Structure
----
Main

↓

Register

↓

Login

↓

AccountManager


Detail
----
```python
Main()

  Register (PWInput):
    run():
      # get input from base class 
      # check for restrictions
      # hash
      # save in file
    verify_password()
      # verify password with a second input

  Login (PWInput):  
    run():
      # get input from base class 
      # check for restrictions
      # hash input
      # load hashed password
      # compare both hashes

  AccountManager:
    run():
      # get input
      # actions based on input
    add()
    delete()
    print_account()
    print_all()
    edit()
   
  PWInput:
    run():
      # get input for username and password
      # check input based on restrictions






