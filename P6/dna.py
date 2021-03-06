import csv
import sys

# DNA profiling program

# Terminates program if there are more/less than 2 command-line arguments, or if file extensions are incorrectly entered
if len(sys.argv) != 3 or sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".txt") == False:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)


# Opens and reads csv file, stores strs from column headers (from row 1) in 'strs'
# Note: File not closed as it is needed for matching later
csvfile = open(sys.argv[1], "r")
reader = csv.DictReader(csvfile)
strs = reader.fieldnames

# Opens and reads txt file, stores dna sequence in 'dna', and closes file
with open(sys.argv[2], "r") as txtfile:
    dna = txtfile.read()


# Defines lists 'count' and 'maxcount' with x number of elements initialied to 0, where x is the number of strs in the csv
# 'Count' temporarily stores the number of times an str appears consecutively, beginning from the nucleotide (char) being checked
# 'Maxcount' stores the highest value that count reaches after checking all the nucleotides (chars) in 'dna'
count = [0] * (len(strs) - 1)
maxcount = [0] * (len(strs) - 1)


# Checks 'dna' for each of the strs in the csv
i = 0
while i < (len(strs) - 1):

    # Checks every nucleotide (char) in 'dna' for the current str
    j = 0
    while j < len(dna):

        # Adds 1 to count if str is present
        if dna[j:(j + len(strs[i + 1]))] == strs[i + 1]:
            count[i] += 1

            # Checks for consecutive repeats and adds 1 to count for each consecutive repeat
            k = 0
            while k < (len(dna) - j):
                if dna[j + k + len(strs[i + 1]):(j + k + (2 * len(strs[i + 1])))] == strs[i + 1]:
                    count[i] += 1
                else:
                    break
                k += len(strs[i + 1])

            # Stores count in maxcount if the current value of count is larger than maxcount
            if count[i] > maxcount[i]:
                maxcount[i] = count[i]

        count[i] = 0
        j += 1

    i += 1


# 'Match' and 'name' store the results of the profiling
match = False
name = list()


# Generates profiling results
for row in reader:

    # Temporarily stores str values from csv (as int) for each individual
    combi = [0] * (len(strs) - 1)
    i = 0
    while i < (len(strs) - 1):
        combi[i] = int(row[strs[i + 1]])
        i += 1

    # Checks if 'maxcount' matches 'combi'
    if maxcount == combi:
        match = True
        name.append(row[strs[0]])
        # Include break to check for single names/matches only
        # break

csvfile.close()


# Prints profiling results
if match == True:
    i = 0
    while i < len(name):
        print(name[i])
        i += 1

else:
    print("No match")