Terminal version of a Passwortmanager.
Struct listed below:

Main
  |
  V
Register
  |
  V
Login
  |
  V
AccountManager
--------------------------------

Register(PWInput):
  run():
    # get input from baseclass 
    # check for restrictions
    # hash
    # save in file
  verify_password()

Login(PWInput):
  run():
    # get input from baseclass 
    # check for restrictions
    # hash input
    # load hashed password
    # compare both hashes
    
AccountManager
  run()
    # get input
    # actions based on input
  add()
  delete()
  print_account()
  print_all()
  edit()

PWInput:
  run()
    # get input for username and password
    # check input based on Restictions
  
