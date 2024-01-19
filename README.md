# Terminal Password Manager

This project is a terminal-based Password Manager with the following structure:

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

csharp
Copy code

## Register (PWInput):
```python
run():
  # get input from base class 
  # check for restrictions
  # hash
  # save in file
verify_password()
Login (PWInput):
python
Copy code
run():
  # get input from base class 
  # check for restrictions
  # hash input
  # load hashed password
  # compare both hashes
AccountManager:
python
Copy code
run():
  # get input
  # actions based on input
add()
delete()
print_account()
print_all()
edit()
PWInput:
python
Copy code
run():
  # get input for username and password
  # check input based on restrictions
Feel free to adjust the formatting according to your preferences.





