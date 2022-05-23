from sys import argv, exit
import csv


def main():
    if len(argv) != 3:
        print("Incorrect number of command-line arguments.")
        exit()

    STRs = []
    people = []

    # Read in sequenceData file - using `with` we dont have to close a file
    with open(argv[1], "r") as sequenceData:
        reader = csv.DictReader(sequenceData)
        # Fill list of Short Tandem Repeats (STRs)
        STRs = reader.fieldnames[1:]
        for row in reader:
            # Add person to people
            people.append(row)

    # Initialise dictionary
    stringCount = dict.fromkeys(STRs, 0)

    # Read in sequence file
    with open(argv[2], "r") as sequenceFile:
        # Grab the first line of txt
        sequence = sequenceFile.readline()
        # Loop over every STR from the sequenceData
        for STR in STRs:
            # Update the sequence STR dictionary with max amount of repeats
            stringCount[STR] = find_repeats(sequence, STR)

    # Check if any person has same amount of STR repeats as sequence
    for person in people:
        matches = 0

        for STR in STRs:
            if int(person[STR]) != stringCount[STR]:
                continue
            matches += 1

        if matches == len(STRs):
            print(person['name'])
            exit(0)

    print("No match")
    exit(1)


def find_repeats(sequence, STR):
    # número de bases
    length = len(STR)

    maxRepeats = 0
    for i in range(len(sequence)):
        # inicia e repete o repeat
        repeats = 0

        if sequence[i: i + length] == STR:
            # if first match
            repeats += 1
            # adiciona por repetidos matches
            while sequence[i: i + length] == sequence[i + length: i + (2 * length)]:
                repeats += 1
                i += length

        # muda maxRepeat se a atual for maior que a antiga
        if repeats > maxRepeats:
            maxRepeats = repeats

    return maxRepeats


if __name__ == "__main__":
    main()