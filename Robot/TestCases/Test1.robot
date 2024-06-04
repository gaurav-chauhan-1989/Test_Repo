*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Browser.robot

*** Test Cases ***
Browser open and maximize
Input Text  name:firstname  Gaurav

