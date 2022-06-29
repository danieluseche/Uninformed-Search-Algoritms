#!/usr/bin/bash

# Clearing the previous file
$(> output.time)

# Looping among the travel salesman instances
for FILE in TSP_instances/*
do
  $(echo $FILE >> output.time)
  $(time (python3 uniformCostSearch.py $FILE) &>> output.time)
  $(echo $'*****************************************************\n'>> output.time)
done

#Ploting the complexity graph
$(python3 graph.py)

