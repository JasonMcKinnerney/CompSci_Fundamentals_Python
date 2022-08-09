
def main():
    #open the input in.dat file for reading
    # open the output out.dat file for writing
    begin_file = open('in.dat', 'r')
    final_file = open('out.dat', 'w')
    # initialize an accumulator to 0
    total = 0
    for line in begin_file:
        line = line.rstrip('\n')
        if len(line) > 0:
            li = line.split(',')
            total += int(li[1])
            combined = [li[1], li[0], str(total)]
            complete = ', '.join(combined)
            final_file.write(complete + '\n')
    begin_file.close()
    print(final_file)
    final_file.close()

    # start a loop that loops through the input file line by line
        # trim the last character off the line because it's a "\n"
        # if the line length is greater than zero
            # split the line into a list
            # add the numeric part of the line (the second element) to the accumulator (convert to int first)
            # write out the data to the output file as shown in the readme.txt
    # close the input file
    # close the output file

main()

