# easy hai lekin lengthy tha idk this "|" method...

user=input("file name with extension: ")

if ".gif" in user:
    print("image/gif")
elif ".jpg" in user:
    print("image/jpg")
elif ".jpeg" in user:
    print("image/jpeg")
elif ".png" in user:
    print("image/png")
elif ".pdf" in user:
    print("document/pdf")
elif ".txt" in user:
    print("document/txt")
elif ".zip" in user:
    print("file/zip")
else:
    print("application/octet-stream")