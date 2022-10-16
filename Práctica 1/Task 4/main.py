# FUNCTION TO ENCODE WITH RUN-LENGTH
def run_length(inp):
    output = ""
    # We go over the input sequence
    i = 0
    while i <= len(inp) - 1:
        # We use a counter called k to check how many characters there are from a type
        k = 1
        # We take the current character and store it in c
        c = inp[i]
        j = i
        while j < len(inp) - 1:
            # If the current input is equal to the next one, we add 1 to the k counter and keep searching in the next
            # character, else we stop
            if inp[j] == inp[j + 1]:
                k += 1
                j += 1
            else:
                break
        # We add to the output code the number of equal characters we have counted and the character itself
        output += str(k) + c
        i = j + 1
    # Once all the code has been checked, we return de coded sequence
    return output


# Checking the function works with an example
if __name__ == "__main__":
    code = "BBBBBBBBBBBBNBBBBBBBBBBBBNNNBBBBBBBBBBBBBBBBBBBBBBBBNBBBBBBBBBBBBBB"
    print(run_length(code))
