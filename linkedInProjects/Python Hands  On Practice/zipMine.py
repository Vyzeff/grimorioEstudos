from zipfile import ZipFile
import os

def zipAll(directory, fileTypes, output):
    filePaths = []
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            fileRedundant, fileExtension = os.path.splitext(filename)
            #print(fileExtension)
            if fileExtension in fileTypes:
                filePath = os.path.join(root, filename)
                filePaths.append(filePath)
                
    print("The following files will be zipped.")
    for filename in filePaths:
        print(filename)
        
    with ZipFile(output, "w") as zip:
        for file in filePaths:
            zip.write(file)
    print("Files compressed.")
    
if __name__ == "__main__":
    zipAll(directory="./my_stuff", fileTypes=[".jpg", ".txt"],output="ziptest.zip")