try:
   fh = open("testfile", "w")
   print("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()