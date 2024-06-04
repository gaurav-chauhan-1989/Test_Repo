*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  https://www.google.com

*** Test Cases ***
TC_001_Login
  Open Browser  ${URL}  ${Browser}
