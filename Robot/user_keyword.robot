*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  http://newtours.demoaut.com/
@{Credentials}  admin  admin


*** Test Cases ***
TC_001
  Open Browser  ${URL}  ${Browser}
  Maximize Browser Window
  Login_Module  @{Credentials}[0]  @{Credentials}[1]                  # Add values to arguments.1st value for 1st arument and 2nd for 2nd argument
  Close Browser
  Log  This program is run %{username} on %{os}



*** Keywords ***
Login_Module
  [Arguments]  ${Username}  ${Password}                               # Define Arguments double space separated
  Input Text  name:userName  ${Username}                              # Assign argument to element locator
  Input Text  name:password  ${Password}                              # Assign argument to element locator
  Click Element  name:login
