def fsa_ends_with_ab(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    if state == 2:
        return True
    else:
        return False

s = input("Enter a string: ")

if fsa_ends_with_ab(s):
    print("Accepted (Ends with 'ab')")
else:
    print("Rejected")