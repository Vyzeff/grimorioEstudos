from fileinput import filename
import requests
import re
#kinda works, didn't get around to finalize it
def downloadSequence(url, output):

    sequence = True
    while sequence:
        downloadCount = 0
        
        if downloadCount == 0:    
            r = requests.get(url)
            fileName = url.rsplit("/", 1)[1]
            downloadCount += 1  
            
        '''             
        elif downloadCount < 10:
            oldName = url.rsplit("/", 1)[1]
            fileExtension = url.rsplit(".", 1)[1]
            fileName = re.sub(oldName, f"image00downloadCount}.fileExtension}", oldName)
            downloadCount += 1 
             
        else:
            oldName = url.rsplit("/", 1)[1]
            fileExtension = url.rsplit(".", 1)[1]
            fileName = re.sub(oldName, f"image0downloadCount}.fileExtension}", oldName)
            downloadCount += 1  
            r = requests.get() 
        '''   
                
        with open(f"{output}/{fileName}", "wb") as f:
            f.write(r.content)
        break
    print("Your files were dowloaded successfully.")

if __name__ == "__main__":
    downloadSequence("http://699340.youcanlearnit.net/image001.jpg", "./my_stuff")