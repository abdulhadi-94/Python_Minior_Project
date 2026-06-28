#creating function
def manage_marks():
  try:  
   marks1 =int(input("Enter the marks of 1st Subject: "))
   marks2 =int(input("Enter the marks of 2nd Subject: "))  
   marks3 =int(input("Enter the marks of 3rd Subject: "))
   marks4 =int(input("Enter the marks of 4th Subject: "))
   marks5 =int(input("Enter the marks of 5th Subject: "))
   
   # store the marks in the list
   total_marks =[marks1,marks2,marks3,marks4,marks5]
   # calculating average marks
   avreage=sum(total_marks)/5
   print("Average Marks: ",avreage)
   #claculating highest marks
   highest =max(total_marks)
   print("Highest Marks: ",highest)
   # calculating lowest marks
   lowest =min(total_marks)
   print("Lowest Marks: ",lowest)
   # printing all marks in descending order
   total_marks.sort(reverse=True)
   print("Sorted in descending order: ",total_marks)
  # handling ValueError if non-numeric input is given
  except ValueError:
    print("ERROR OCCURED-Enter only numeric value.")

# accessing function
manage_marks()

