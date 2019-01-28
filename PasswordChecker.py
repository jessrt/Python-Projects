passwordCount = 0;
i = 0
oneChar = 'a'
checkRule = [0, 0, 0, 0]
firstPassword = ""
confirmPassword = ""
match = False
valid = False
span = False

def ruleDisplay():
    print(" The set of password rules is given below:")
    print(" 1.) Password length must by 8 to 32 characters")
    print(" 2.) It must contain at least one numerical.")
    print(" 3.) It must contain one upper-case letter")
    print(" 4.) It must contain one lower-case letter")
    print(" 5.) It must contain at least one special character \n"
          "     set: { # $ * ( ) % & ^  )")

def askForPassword():
    txt = input("Please enter your password: ")
    return txt

def displaySuccess():
    print("Matching passwords. Your password will be updated.")

def displayFail():
    print("Password passed length check; however, it "
          "failed to meet one of the other password rules.")

def displayMatchFail():
    print("Match fail.")

def passwordLength(pLen):
    if pLen > 32 or pLen < 8:
        print("Password must be between 8 & 32 characters.")
        return False
    else:
        return True

def checkPasswordCharacters(oneChar):
    converted = ord(oneChar)

    # check if number is present
    if converted >= 48 and converted <=57:
        checkRule[0] += 1

    # check if lower-case letter is present
    elif converted >=97 and converted <=122:
        checkRule[1] += 1

    # check if upper-case letter is present
    elif converted > 65 and converted <=90:
        checkRule[2] += 1

    # check if special character is present
    elif((converted >= 35 and converted <=38) or ((converted >=40)
          and (converted <=42)) or converted == 94 ):
        checkRule[3] += 1

def checkRules():
    if ((checkRule[0] > 0) and (checkRule[1] > 0) and
            (checkRule[2] > 0) and (checkRule[3] > 0)):
        return True

def matching(first, confirm):
    if first == confirm:
        return True
    else:
        return False

# while the passwords do not match
while match is False:

    # While the inputted password is invalid
    while valid is False:
        # display the rules
        ruleDisplay()

        # Ask the user for length
        while span is False:
            firstPassword = askForPassword()
            passwordCount = len(firstPassword)
            span = passwordLength(passwordCount)

        # Checks each of the characters to see if password
        # meets standards

        while i < passwordCount:
            checkPasswordCharacters(firstPassword[i])
            i += 1

        # If the password does not meet standards, ask the user to
        # create another.

        valid = checkRules()
        if valid is False:
            displayFail()
            checkRule = [0, 0, 0, 0]

    # Asks the user to re-enter the password. If they do not,
    # exit the program.
    confirmPassword = input("Please re-type your password: ")
    match = matching(firstPassword, confirmPassword)
    if match is False:
        displayMatchFail()
        checkRule = [0, 0, 0, 0]
        valid = False
        break

# Only if the two inputs match, display success message & exit the program
if match is True:
    displaySuccess()
exit(1)
