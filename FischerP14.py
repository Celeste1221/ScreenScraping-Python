# Programmer: Mary Fischer
# Purpose: Create a screen scraping app that lets the user enter the url and the content they want to scrape

import wx

# define functions 
def Submit(event):
    # this screen scraping code is modified from a course - I added the try except and adapted it for a GUI and to write to a file
    from bs4 import BeautifulSoup  
    import urllib.request
    try:
        website = urllib.request.urlopen(url.GetValue())
    except:
        msg.SetValue('Invalid URL')
    html_doc = website.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    anchortags = soup.find_all('a')

    # check if file exists, if not, create and open it; write to it: tag['href'], save and close file
    # reference: https://www.w3schools.com/python/python_file_remove.asp
    import os
    if os.path.exists(filename.GetValue()):
        msg.SetValue('That file already exists. Please choose another file name.')
    else:
        try:
            f = open(filename.GetValue(), "w")
            for tag in anchortags:
                f.write(tag['href'] + '\n')
            msg.SetValue('Your data has been saved to a file. Click OPEN to view.')
            f.close()
        except IOError:
            msg.SetValue('Unable to open file.')

# display the screen scraping results in the GUI window
def Open(event):
    f = open(filename.GetValue(), "r")
    msg.SetValue(f.read())
    f.close()

# clear all the boxes and resets the msg box
def Clear(event):
    filename.SetValue('')
    msg.SetValue('Enter a web site URL above, exactly as it is shown in the address bar.\
                  \nThen enter a filename where you want to save your data.')
    url.SetValue('')


# Create GUI
# references: 
# https://letscodepython.com/blog/2017/12/27/building-guis-wxpython/
# https://wxpython.org/Phoenix/docs/html/wx.TextCtrl.html?highlight=textctrl#phoenix-title-textctrl-styles
app = wx.App()
win = wx.Frame(None, title = "Welcome to the Screen Scraper App", size = (590,530)) 
bkg = wx.Panel(win) #the panel object in the background to deal with resizing

# add controls (5)
urlLabel = wx.StaticText(bkg, label = 'Enter URL')
url = wx.TextCtrl(bkg)
submit = wx.Button(bkg, label = 'SUBMIT')
opn = wx.Button(bkg, label = 'OPEN')                                            
msg = wx.TextCtrl(bkg, style = wx.TE_READONLY | wx.TE_MULTILINE | wx.HSCROLL | wx.TE_AUTO_URL,
                  value = 'Enter a web site URL above, exactly as it is shown in the address bar.\
                  \nThen enter a filename where you want to save your data.')
filenameLabel = wx.StaticText(bkg, label = 'Enter Filename:')
filename = wx.TextCtrl(bkg)
clear = wx.Button(bkg, label = 'CLEAR')

# sizer for the horizontal box
hbox = wx.BoxSizer(wx.HORIZONTAL)
hbox.Add(urlLabel, proportion = 0, flag = wx.ALIGN_CENTER | wx.TOP, border = 5)
hbox.Add(url, proportion = 1, flag = wx.LEFT |wx.TOP | wx.RIGHT, border = 5)
hbox.Add(submit, proportion=0, flag = wx.RIGHT | wx.TOP, border = 5)
hbox.Add(opn, proportion = 0, flag = wx.RIGHT | wx.TOP, border = 5)

# sizer for the vertical box
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND |wx.LEFT | wx.RIGHT, border = 5)
vbox.Add(filenameLabel, proportion = 0, flag = wx.EXPAND | wx.LEFT, border = 5)
vbox.Add(filename, proportion = 0, flag = wx.EXPAND | wx.RIGHT | wx.LEFT, border = 5)
vbox.Add(msg, proportion = 1,
         flag = wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM | wx.RIGHT, border = 5)
vbox.Add(clear, flag = wx.ALIGN_RIGHT |wx.RIGHT | wx.BOTTOM, border = 5)
bkg.SetSizer(vbox)

# bind the submit button 
submit.Bind(wx.EVT_BUTTON, Submit)

# bind the open button
opn.Bind(wx.EVT_BUTTON, Open)

# bind the clear button
clear.Bind(wx.EVT_BUTTON, Clear)

win.Show()
app.MainLoop
                    
