file = input("Please enter the name of a file: ")
filename = file.lower().strip()

if filename.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
            print("application/zip")
    elif filename.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")

else:
    print("application/octet-stream")
