with open("attendance.txt","w") as file:
 file.write("Haifa: Absent\n")
 file.write("Janna:Present\n")
 file.write("Sir.Bryne: Absent\n")
 file.write("Kiki: Present\n")
 file.write("Layla: Present\n")
 file.write("Coach Eyad: Absent\n")
 
 with open("Attendance.txt","a") as file:
  file.write("Daisy:Present\n")
  print("-----Fetching Data From Disk----")
  with open("attendance.txt","r") as file:
   for line in file:
    #.strip()removes the hidden '\n' at the end of the lines
    print(line.strip())