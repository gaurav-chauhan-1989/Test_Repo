*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  http://www.facebook.com

**** Test Cases ***
TC_001
  Open Browser  ${URL}  ${Browser}
  Maximize Browser Window
  Select Radio Button  sex  1                           # To click on a radio button we need locator as well as its value. As it contains more than one value
  Click Link  id:terms-link
