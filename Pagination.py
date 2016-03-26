'''
Created on 14 Aug 2013

@author: RAJESH
Question:
Pagination is the process of dividing content into discrete pages. Pagination is common in Web-based applications, and is used for limiting the result set and displaying a limited number of records on the web page.
E.g.:
Consider the Department-Employee scenario. If the search operation is performed on the basis of Department Id, and there are 100,000 employees per department, then it does not make sense to display the details of 100,000 employees in single page. So, pagination allows to display limited results e.g. 20 records per page. "Previous" and "Next" links or the Page numbers are usually provided on the user interface so that users can navigate to other pages.
Q. Write a program for selecting the records that need to be displayed on user interface. Records should be filtered as per the input parameters, and should be sorted by Employee Name. Requirement is to ensure faster initial page load.
Your program should extract the records from this file on the basis of input parameters. For example, if the input is (Department ID-10, Page Size-20, and Page Number -1), then the program should retrieve first set of 20 records for Department ID-10 sorted by employee name. If the input is (Department ID-10, Page Size-20, and Page Number -2), then the program should retrieve second set of 20 records. As the data for a given department will be sorted by employee name, there will be no overlapping between first page and second page.
Asumptions:
->Input file data may or may not be sorted by Department and Employee ID
->Expected Volumes: Department Data File may have approx. 100,000 records per department ID. Page Size is expected to be less than 100 records.

'''

from operator import itemgetter
#Read File
filePath = raw_input()
inputParams = raw_input().strip().split(',')
if(len(inputParams) != 3):
    print "Invalid Input"
    exit()
    
with open(filePath, 'r') as f:
    records = f.readlines()

recordDict = {}
for rec in records:
    recArray = rec.strip().split(',')
#    recArray[2] = recArray[2].split()
    if recordDict.has_key(recArray[0]):
        recordDict[recArray[0]].append(recArray)
    else:
        recordDict[recArray[0]] = [recArray]

if recordDict.has_key(inputParams[0]):
    filteredItems = recordDict[inputParams[0]]
else:
    print "Data Unavailable"
    exit()

sortedfilteredItems = sorted(filteredItems, key=itemgetter(2))
pageCount = len(sortedfilteredItems)/int(inputParams[1])
if int(inputParams[2])  > pageCount :
    print "Data Unavailable"
    exit()

limitedSortedfilteredItems = sortedfilteredItems[(int(inputParams[2]) - 1) * int(inputParams[1]): (int(inputParams[2]) - 1) * int(inputParams[1]) + int(inputParams[1])]

for i in limitedSortedfilteredItems:
    print ",".join(i)
