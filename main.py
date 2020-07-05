# python dem for showing online Text change with pysimplegui
# this works but i feel it is not as awsome as possible.
# may this is smarter to do.
#
__author__ = "Volker Heggemann"
__copyright__ = "Copyright 2020, Volker Heggemann"
__credits__ = ["The PySimpleGui Project"]
__license__ = "CC BY-NC-SA"
__version__ = "3.0 DE"
__maintainer__ = "vohe"
__email__ = "vohegg@gmail.com"
__status__ = "rolling Release"

# gettext is the gnu translation wrapper
# look: https://docs.python.org/3/library/gettext.html
# there ara many samples, like https://phrase.com/blog/posts/translate-python-gnu-gettext/
import gettext

# The GUI Modul of your choice
import PySimpleGUI as sg

# possible languages as many as you create with pygettext
# for each of this a folder have to be under
# locales/xx/LC_MESSAGES/
lang = ('de', 'en', 'nd')

# Start with one out of the list
lang_akt = lang[2]

# every language gets a gettext object which is callable.
# i store this in a dict like {lang[0..x]:Object,...}
almanach = {}

# this dict stores the actual translation strings.
# it is also a key:value dict
textdict = {}

# first we fill the dict with data
try:
    for language in lang:
        almanach[language] = gettext.translation('demo', localedir='locale', languages=[language])
except:
    # gettext gives us a _() function. but if it fails we need a fallback
    # this is not smart, but if someone find a better way, feel free
    _ = lambda s: s


# this is the trick for PySimpleGui
# ever String that should be translatet goes into the Translation dict
# everytime we change the language (almanach[language].install()) we need to do this
def get_locale_text():
    tdict = {}
    tdict['hello'] = _('Hello! What is your name?')
    tdict['another'] = _('Another string')
    return tdict


# just a print out to console
# to test if any string is there

for anylang in lang:
    # install and activate a new language
    almanach[anylang].install()
    # set all the strings to the new language
    textdict = get_locale_text()
    print(textdict['hello'])
    print(textdict['another'])

# here starts the PySimpleGui sample file
#
# create a layout, but every string that should be translate wrapp
# into a _() function in the get_locale_text() section and here
# after that use the variable.
# look at the key it is the key for the dict and the key for the Element

layout = [[sg.Text(textdict['hello'], key='hello')], [sg.Button(textdict['another'], key='another')]]

# Create the window
window = sg.Window("Demo", layout)

looptime = 500
# rotating counter
i = 0
# Create an event loop
while True:
    event, values = window.read(looptime)
    # End program if user closes window or
    # presses the ... button
    if event == "another" or event == sg.WIN_CLOSED:
        break

    if event:  # only as a sample - normaly this is called if the language should change
        almanach[lang[i]].install()  # lang 1,2 or 2 what ever.
        textdict = get_locale_text()  # update all text strings
        for key in textdict:  # call in a loop all elements which has text strings.
            # this raises errors if the elements got no key's
            # like radio buttons, checkboxes, system notifications....
            window[key].update(textdict[key])
    i += 1
    if i > 2:
        i = 0
window.close()
