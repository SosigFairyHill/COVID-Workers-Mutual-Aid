library(googledrive)
library(leaflet)
library(dplyr)
library(leaflet.extras)

ui <- fluidPage(
  mainPanel( 
    #this will create a space for us to display our map
    leafletOutput(outputId = "mymap")))

#create the map
output$mymap <- renderLeaflet({
  leaflet(map_data) %>% 
    setView(lng = -99, lat = 45, zoom = 2)  %>% #setting the view over ~ center of North America
    addTiles() %>% 
    addCircles(data = data, lat = ~ Latitude, lng = ~ Longitude, weight = 1, radius = 1, popup = ~ Title, label = ~ Title, fillOpacity = 0.5)
})

server <- function(input, output, session) {
  
  options(httr_oob_default=TRUE)
  
  drive_auth()
  
  drive_download(as_id(as.character(drive_find(type = "spreadsheet")[1,2])),type = "csv")
  
  map_data <- read.csv(file = paste0(as.character(drive_get(as_id(as.character(drive_find(type = "spreadsheet")[1,2])))[1]), ".csv"))
  
  #create the map
  output$mymap <- renderLeaflet({
    leaflet(map_data) %>% 
      setView(lng = -99, lat = 45, zoom = 2)  %>% #setting the view over ~ center of North America
      addTiles() %>% 
      addCircles(data = data, lat = ~ Latitude, lng = ~ Longitude, weight = 1, radius = 1, popup = ~ Title, label = ~ Title, fillOpacity = 0.5)
  })
  
}