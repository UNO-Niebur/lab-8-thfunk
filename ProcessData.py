#ProcessData.py
#Name: Taran Funk
#Date: 3/29/2026
#Assignment: Lab 8

def makeUserID(firstName, lastName, nuID):
  if(len(lastName)<5):
    lastName = lastName + "x"*(5-len(lastName))
  else:    
    lastName = lastName[0:5]
  userID = firstName[0].lower() + lastName.lower() + nuID[-3:]
  return userID

def makeMajorYear(major, year):
  if(year == "Freshman"):
    yearShort = "FR"
  elif(year == "Sophomore"):
    yearShort = "SO"
  elif(year == "Junior"):
    yearShort = "JR"
  elif(year == "Senior"):
    yearShort = "SR"
  majorShort = major[0:3].upper()  
  majorYear = majorShort + "-" + yearShort
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  outFile.write("Last Name,First Name,UserID,Major-Year\n")

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    #Split the line into its components and assign to variables for easier use
    data = line.strip().split()
    firstName = data[0]
    lastName = data[1]
    email = data[2]
    nuID = data[3]
    DOB = data[4]
    year = data[5]
    major = data[6]

    #Create the userID and major-year values using the functions we defined
    userID = makeUserID(firstName, lastName, nuID)
    majorYear = makeMajorYear(major, year)

    #Write the student information to the output file in CSV format
    outFile.write(f"{lastName},{firstName},{userID},{majorYear}\n")

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
