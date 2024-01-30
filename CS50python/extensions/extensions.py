
def main():
    FileName=input("File Name : ")
    FileName=FileName.strip().lower().split(".")
    length=len(FileName)
    length=length-1
    if(len(FileName)<=1):
        print("application/octet-stream")
    elif(FileName[length] =="gif"):
        print("image/gif")
    elif(FileName[length] =="jpg" or FileName[length] =="jpeg" ):
        print("image/jpeg")
    elif(FileName[length] =="png" ):
        print("image/png")
    elif(FileName[length] =="png" ):
        print("image/png")
    elif(FileName[length] =="pdf" ):
        print("application/pdf")
    elif(FileName[length] =="txt" ):
        print("text/plain")
    elif(FileName[length] =="txt" ):
        print("text/plain")
    elif(FileName[length]=="zip"):
        print("application/zip")
    else:
     print("application/octet-stream")

main()
