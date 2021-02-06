startNum = 5
endNum = 10
someName = 1
counter = 0

print("Our starting number is:",startNum)
print("Our ending number is:",endNum)

for someName in range(startNum):
    print("inside the loop", counter, someName)
    if someName == 2:
        print ("I'm out!!")
        break
    counter += 1
    

