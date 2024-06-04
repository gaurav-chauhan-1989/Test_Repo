*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  http://www.thetestingworld.com/testings/

*** Test Cases ***
TC_001
  Open Browser  ${URL}  ${Browser}
  Maximize Browser Window
  Select Checkbox  name:terms                        # Format to check checkbox
