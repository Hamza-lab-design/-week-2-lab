"""
RECORD CHECK  -  my version
===========================

Name  :hamza
Lane  :  AI     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_count = 0 

while True: 

    label = input("Dataset name (type quit to stop): ")
    if label == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float (input("Rows expected: "))

    difference = limit - value
    percent = value / limit * 100

    if percent >=100:
        status = "OVER LIMIT"
        over_count += 1
    elif percent >= 90:
        status = "WARNING" 
    else:
        status = "OK"


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = 0.0   # replace with your calculation
percent = 0.0       # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

status = ""   # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
