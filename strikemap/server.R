library(shiny)
library(googledrive)
library(leaflet)
library(dplyr)
library(leaflet.extras)

function(input, output) {
  map_data <- read.csv(file = paste0(as.character(drive_get(as_id(as.character(drive_find(type = "spreadsheet")[1,2])))[1]), ".csv"), stringsAsFactors = F)
  map_data$Latitude <- as.numeric(map_data$Latitude)
  map_data$Longitude <- as.numeric(map_data$Longitude)
  
  #create the map
  output$mymap <- renderLeaflet({
    leaflet(map_data) %>% 
      setView(lng = -3.4, lat = 55.4, zoom = 5)  %>% #setting the view over ~ center of North America
      addTiles() %>%
      addCircles(data = map_data, lat = ~ Latitude, lng = ~ Longitude, weight = 1, radius = 10000, popup = ~ Title, label = ~ Title, fillOpacity = 0.5)
  })
}
