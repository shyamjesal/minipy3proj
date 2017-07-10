# > Import Required Modules
import csv

# In the branch dictionary, 1 is A1, 2 is A2 and so on. And the values corresponding to each branch is the number of seats(not actual, don't worry. They are scaled down according to the number of responses filled in the csv.)
branch = {'1':7,'2':8,'3':13,'4':10,'7':22,'8':5,'A':13,'B':5}
# I've set the initial cutoffs to 10. Change it or don't use this dictionary, it is your choice.
cutoff = {'1':10,'2':10,'3':10,'4':10,'7':10,'8':10,'A':10,'B':10}

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # > Open File
    rawfile = open('file.csv')
    # > Start reading the file
    filereader = csv.reader(rawfile)
    csv_data = list(filereader)
    parsed_data = []
    
    # > Don't forget to skip the header row in the csv

    fields = csv_data.pop(0)
    #csv_data = sorted(filelist, key=lambda x:x[1],reverse=True)

    # > Figure out the variables and what they are doing.
    # The following loop adds the data from csv to parsed_data
    for row in csv_data:
        # Figure out what dict() and zip() do. Read the documentation. Links are in the post.
        parsed_data.append(dict(zip(fields, row)))

    # > Close the file
    rawfile.close()
    # > Return parsed_data
    return parsed_data

def allot(new_data):
    """Function to allot branch based on preferences you get from the parsed_data"""
    for i in range(len(new_data)):
        # In the following two lines, uncomment the one you think would work in this case.
        # prefcount = 1
        prefcount='1'
        # The following line will throw an error because x doesn't exist. Find the right value to replace x.
        for j in range(1,10):
            x=new_data[i][prefcount]

            if(x==""):
                new_data[i]['alloted'] = x
                break

            a,b=x

            if(branch[b]>0):
                # You know what to do here. I recommend using the interactive mode to find out how data is displayed.
                branch[b]-=1
                new_data[i]['alloted'] = x
                cutoff[b] = new_data[i]["CG Year 1"]
                break
            else:
                # I filled this part in because it might confuse a few of you but try to figure what this does.
                prefcount=ord(prefcount)-48
                prefcount+=49
                prefcount=chr(prefcount)


def addnew(new_data):
    """Writes back alloted stuff into csv file"""
    outputFile = open('output.csv', 'w')
    outputWriter = csv.writer(outputFile)
    # > Write the edited parsed_data, i.e. new_data to a new csv file.
    outputWriter.writerow(['ID', 'CG Year 1', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'alloted'])
    for row in new_data:
        outputWriter.writerow([row['ID'], row['CG Year 1'], row['1'], row['2'], row['3'], row['4'], row['5'], row['6'], row['7'], row['8'], row['9'], row['alloted']])
    outputFile.close()
def main():
    # The right way to work through this would be to work on one function at a time. Parse the data first. Check what format you are getting the data in, and then allot it.
    # And do the reverse of what you did in parsing, write the data back to the file.
    new_data = parse('file.csv', ",")
    allot(new_data)
    print(cutoff)
    addnew(new_data)

if __name__ == "__main__":
    main()
