*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Browser.robot

*** Test Cases ***
TestCase1
  Browser open and maximize
  Input Text  name:firstname  Gaurav