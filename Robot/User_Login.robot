*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${Browser}  Chrome                                                        # $ for Scalar Variable
${URL}  http://newtours.demoaut.com/                                       # $ for Scalar Variable
@{List}  admin  admin                                                      # @ for list variables
&{Credentials}  k1=admin  k2=admin                                         # & for dictionary variables


*** Test Cases ***
TC001_UserLogin
  Open Browser  ${URL}  ${Browser}
  Maximize Browser Window
  Input Text  name:userName  &{Credentials}[k1]       # Input Text is keyword, name:username is element identification and then textbox value from variable
  Input Text  name:password  &{Credentials}[k2]
  Click Element  name:login
  Close Browser
  Log  This program is running on %{username} on %{os}
