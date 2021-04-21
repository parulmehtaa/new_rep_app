from os import write
import sys
# Read the file

file=open("dummydata.csv","r") #open in read mode
file_contents=file.read() #read the contents of file
lines=file_contents.split("\n") #split on next row

print(len(lines))

header=lines[0].split(";") #extracting the header
print("first print")
print(header[0:5])
lines=lines[1:]

# creating multidimensional array for lines
records=[]
for line in lines[:5]:
    cell=line.split(";")
    cell=cell[:5]
    records.append(cell)

# printing records

print("second print")
for record in records:
    
    print(record)

# calculating country with the maximum area

max=-sys.maxsize
i=0
for record in records:
    print(record)
    print(i)
    if int(record[1])>int(max):
        
        max=record[1]
    i+=1
print(f"max value of {header[1]} is {max}")

# Filtering out the row with max area
new_record=[]
for record in records:
        new_record.append(record)


new_record_lines=[]
for record in new_record:
    new_record_lines.append(";".join(record))

print("--------------------------------------------")
print(new_record_lines)

new_record_content= "\n".join(new_record_lines)
print(new_record_content)

f=open("new_record.csv","w")
f.write(new_record_content)