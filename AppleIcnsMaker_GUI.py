__author__ = 'lane'

# !/usr/bin/env python
# -*-python-*-
# ========================
# Copyright 2013-2015 to Lane128 on github
# Version v1.0
# ========================

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import askopenfilename
import os, sys



def openFile():
    filePath = askopenfilename()
    entryText.set(filePath)


def ImageProcess():
    tagImage=entryText.get()
    #if type(tagImage) != 'str':
    #    tagImage = str(tagImage[0])
    if not os.path.isfile(tagImage):
        print '>>>Error path, please choose the png image path.'
        sys.exit()
    filePath = os.path.realpath(tagImage)
    dirPath = os.path.dirname(filePath)
    fileInfo = os.path.basename(filePath)
    fileEx = fileInfo.split('.')[-1]
    if fileEx == 'png':
        fileName = fileInfo[:-4]
        createDirName = fileName + '.iconset'
        createDir = dirPath + '/' + createDirName
        if os.path.exists(createDir):
            print '>>>The old dir exists,ready to delete.'
            os.system('rm -rf ' + createDir)
            print '>>>delete!'
        print '>>>Ready to create the iconset dir.'
        os.mkdir(createDir)
        print '>>>Creation finished!'
        sizeList = [16, 32, 128, 256, 512]
        for size in sizeList:
            finalName = 'icon_' + str(size) + 'x' + str(size) + '.' + fileEx
            xfinalName = 'icon_' + str(size) + 'x' + str(size) + '@2x.' + fileEx
            os.system(
                'sips -Z ' + str(size) + ' ' + filePath + ' --out ' + dirPath + '/' + createDirName + '/' + finalName)
            print '>>> ' + finalName + '  Done!'
            os.system('sips -Z ' + str(
                size * 2) + ' ' + filePath + ' --out ' + dirPath + '/' + createDirName + '/' + xfinalName)
            print '>>> ' + xfinalName + ' Done!'
        print '>>>Copy and make pngs finished!'
        icnsName = fileName + '.icns'
        os.system('iconutil -c icns ' + dirPath + '/' + createDirName + ' -o ' + dirPath + '/' + icnsName)
        print '>>> ' + icnsName + ' finished~'
    else:
        print '>>>Not a png image.'


if __name__ == '__main__':
    root = Tk()
    entryText=StringVar()
    root.title('AppleIcnsMaker')
    root.geometry('500x300+300+300')
    l1 = Label(root,text='File Path:')
    l1.pack(fill=X)
    e1 = Entry(root, width=270,textvariable=entryText)
    e1.pack(fill=X)
    entryText.set('Input Path')
    Button(text='Open file', command=openFile).pack(fill=None)
    Button(text='Generate',command=ImageProcess).pack(fill=None)
    mainloop()
