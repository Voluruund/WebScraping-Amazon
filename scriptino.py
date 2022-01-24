from logging import PlaceHolder
from sqlite3 import Row
from textwrap import fill
from tkinter import CENTER, font
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import * 
from tkinter import ttk

#window style
window =Tk()
window.geometry("700x700")
window.title("Analizza cronologia")
window.resizable(False, False)
window.configure(background="#f0f0f0")

#main function, gets a string in input 
def cercaProdotti():
    global ricerca 
    ricerca = entry1.get()
    window.quit()
    return ricerca

#spacer element placed at the very top
sp = ttk.Label(window)
sp.pack(ipadx=10, fill='both', ipady=90)

#title spacer
spacer = ttk.Label(window, text="Inserisci il prodotto da ricercare", font=("Arial", 18), justify=CENTER)
spacer.pack(ipady=30, fill='y', expand=False)

# This is used to take input from user
# and show it in Entry Widget.
# Whatever data that we get from keyboard
# will be treated as string.
entry1 = ttk.Entry(window, justify=CENTER, foreground='black', font = ('Arial', 12))
entry1.focus_force()
entry1.pack(ipadx = 30, ipady = 5, expand=False)

#middle spacer
sp2 = ttk.Label(window)
sp2.pack(ipadx=0, fill='both', ipady=30)

# This is used to run the main function
search = ttk.Button(window, text="Cerca", command=cercaProdotti)
search.pack( ipadx = 70, ipady = 10, expand=False)


window.mainloop()

#browser opening
browser = webdriver.Chrome(ChromeDriverManager().install())
#replace all spaces with %20 so it can fit the url
keyword = ricerca.replace(' ', '%20')

#generalized link
browser.get(f'https://www.amazon.it/s?k={keyword}&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2O993R8FKRR89&sprefix={keyword}%2Caps%2C83&ref=nb_sb_noss_1')

links = []
#only works with the 4 products layout
divs = browser.find_elements(By.CLASS_NAME, 'sg-col-4-of-12')

#gets all the link
for div in divs:
    try:
        links.append(div.find_element(By.TAG_NAME, 'a').get_attribute('href'))
    except Exception as e:
        print(e)

#opens every link in a new tab
for link in links:
    browser.execute_script(f'''window.open("{link}" , "_blank")''')
    #delay between openings
    time.sleep(20)