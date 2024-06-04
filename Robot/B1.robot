*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  http://www.facebook.com

*** Keywords ***
Browser open and maximize
  Open Browser  ${URL}  ${Browser}
  Maximize Browser Window