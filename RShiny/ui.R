library(shiny)
library(googledrive)
library(leaflet)
library(dplyr)
library(leaflet.extras)

fluidPage(
  mainPanel( 
    #this will create a space for us to display our map
    leafletOutput(outputId = "mymap")))