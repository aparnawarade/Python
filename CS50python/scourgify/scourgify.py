import csv
import sys
def main():
    length=len(sys.argv)
    if length<3:
        sys.exit("Too few command-line arguments")
    elif length>3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1]=="before.csv":
        open_and_processfile(sys.argv[1],sys.argv[2])
    else:
        sys.exit("Could not read ",sys.argv[1])

def  open_and_processfile(inputfile,outputfile):
    mylist=[]
    try:
        with open(inputfile) as file:
            reader=csv.DictReader(file)
            for row in reader:
                mylist.append({"name":row['name'],"house":row['house']})

        with open(outputfile,"w", newline="\n") as file:
            fieldname=["first","last","house"]
            writer=csv.DictWriter(file,fieldnames=fieldname)
            writer.writeheader()
            for line in mylist:
                first,last=line["name"].split(",")
                writer.writerow({"first":first.strip(),"last":last.strip(),"house":line["house"]})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

main()
