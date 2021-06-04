# PasswordChecker

Python App to Check a user's password's vulnerabillity

## How Checker works?

This code takes the password that you want to check calling the 'modules' script to load two counters arrays and a couple of lists from ascii table to compare it.

Next it calls 'additions' script to calculate a qualification with every condition checked.

In second place it calls 'deductions' script to calculate another qualification to substract to addition's number to apply penalties.

### Scripts calling

- main
  - modules
  - additions
    - modules
  - deductions
    - modules
