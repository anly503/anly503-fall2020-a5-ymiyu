library(plotly)
library(tidyverse)

setwd("~/Desktop/eco/04_sm_csv/04")
file_list <- list.files(path="~/Desktop/eco/04_sm_csv/04")

data_list <- list()
for(i in 1:length(file_list)){
  data_list[[i]] <- fread(file_list[i],select=c(1), header = F)
  print(file_list[i])
}

daily_mean = unlist(lapply(data_list, function(x){mean(x[,1])}))
daily_mean_df <- data.frame(cbind(gsub(".csv", "", file_list), daily_mean))
names(daily_mean_df) <- c("date", "daily_mean")
daily_mean_df <- daily_mean_df %>%
  mutate(date = as.Date(date),
         daily_mean = as.numeric(daily_mean)) 


fig <- plot_ly(daily_mean_df, x = ~date, y = ~daily_mean,
               type='scatter', mode='lines') %>% 
  plotly::layout(xaxis=list(title='Date'),
                 yaxis=list(title='Real Power'),
                 title = "Average Daily Real Power from Jul 2012 to Jan 2013",
                 showlegend=FALSE)
fig
