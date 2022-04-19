from genericpath import exists
import os


class Soldier:
    
    def __init__(self,directory,file_type,img_type):
        self.directory = directory
        self.file_type = file_type
        self.img_type = img_type
    
    @property
    def changing_directory(self):
        # os.chdir("C:\\Users\\Saket\OneDrive\Desktop\\1_Coding Theory\Code with Harry\\2\\3_Python\Projects\Oh Soldier Prettify My Folder")
        os.chdir(self.directory)
    
    @property
    def capitalizing_file_type(self):
        c = (os.listdir())
        d = []
        for name in c:
            if self.file_type in name:
                d.append(name)
                f = name.capitalize()
                os.rename(name,f)

    @property
    def numbering_images(self):
        c = os.listdir()
        i = []
        count = 0
        for img in c:
            if self.img_type in img:
                i.append(img)
                m = 0
                for n in i:
                    m+=1
                print(m)
                while(count < len(i)):
                    if os.path.exists(f"{m-1}_{i[m-1]}") == True:
                        break
                    else:
                        os.rename(img,f"{count}_{i[count]}")
                    count += 1
                print(os.path.exists(f"{m-1}_{i[m-1]}"))



dire = input("Enter the name of the directory : ")
file = input("Enter the file type ('.txt', etc;) : ")
img = input("Enter the image type : ")
beautify = Soldier(dire,file,img)


 
beautify.changing_directory
beautify.capitalizing_file_type
beautify.numbering_images