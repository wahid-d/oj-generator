import os
import shutil
import random

def WriteToFiles(folderName, inputs, outputs):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    for input in inputs:
        fileName = folderName + "/%d.in" % (inputs.index(input) + 1)
        file = open(fileName, "w")
        file.write(input)
        file.close()
    for output in outputs:
        fileName = folderName + "/%d.out" % (outputs.index(output) + 1)
        file = open(fileName, "w")
        file.write(output)
        file.close()

    # uncomment the code below if zip is needed

    # zipFilename = folderName + "/data"
    # shutil.make_archive(zipFilename, 'zip', folderName)
    # shutil.make_archive("data", 'zip', os.getcwd())
    # shutil.move("data.zip", zipFilename + ".zip")

# Below is the singularity problem demo

# folderName = "oj-dataset"

# inputs = []
# outputs = []

# for i in range(10):
#     intMax = 2 ** 32 - 1
#     a = random.randint(0, intMax)
#     input = "%d\n" % (a)
    
#     sum = 0
#     while(a > 0 or sum > 9):
     
#         if(a == 0):
#             a = sum
#             sum = 0
         
#         sum += a % 10
#         a //= 10
        
#     output = "%d\n" % (sum)

#     inputs.append(input)
#     outputs.append(output)

# WriteToFiles(folderName, inputs, outputs)