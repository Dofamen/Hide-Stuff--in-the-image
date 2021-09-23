"""
Every jpeg image start with FF D8 FF
and end with FF D9 (Hex)
so every program that read the image stop at the flag of FF D9 
so everything after it will be ignored by any programs that open images

"""

import PIL.Image
import io


class hideTextInsideImage():
    def __init__(self, imagePath):
        assert imagePath.endswith(".jpeg")
        self.__imagePath=imagePath
    
    def write(self, message):
        # opening the image as binary adn as append mode to write stuff on it
        with open(self.__imagePath, "ab") as f:
            # the 'b' before the string used to convert the string to binary
            message = bytes(message, encoding="ascii")
            f.write(message')
        
        print("DONE")
    
    def read(self):
        # Reading From the Image
        with open(self.__imagePath, "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            # re-positioning the file cursor to after the FFD0 the +2 mean move the cursor 2bytes after the F
            f.seek(offset+2)
            return f.read() # printing the hiding message
            
    


class hideImageInsideImage():
    def __init__(self, imagePath):
        assert imagePath.endswith(".jpeg")
        self.__imagePath=imagePath
    
    def write(self, imageTobeHide, isGenerated=False):
        format='PNG'
        if isGenerated is False:
            img = Image.open(imageTobeHide)
            format=imageTobeHide[imageTobeHide.index('.')+1:]

        byteArr = io.BytesIO()
        img.save(byteArr, Format=format)

        with open(self.__imagePath, "ab") as f:
            f.write(byteArr.getvalue())
        print("DONE")
    
    def getHidedImage(self, FileName):
       
        with open(self.__imagePath, "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
        
            f.seek(offset+2)
            newImage = Image.open(io.BytesIO(f.read()))

            newImage.save(FileName)

            
    
class hideExeInsideImage():
    def __init__(self, imagePath):
        assert imagePath.endswith(".jpeg")
        self.__imagePath=imagePath
    
    def write(self, exeFile):
        with open(self.__imagePath, "ab") as f, open(self.exeFile, "rb") as p :
            f.write(p.read)
        
        print("DONE")
    
    def read(self, outputFileName):

        with open(self.__imagePath, "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))
            f.seek(offset+2)
            with open(outputFileName, "wb") as e:
                e.write(f.read())
        
        print("DONE")

               