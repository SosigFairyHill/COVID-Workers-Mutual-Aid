library(shiny)
library(googledrive)
library(leaflet)
library(dplyr)
library(leaflet.extras)

options(httr_oob_default=TRUE)

drive_auth()

drive_download(as_id(as.character(drive_find(type = "spreadsheet")[1,2])),type = "csv", overwrite = T)