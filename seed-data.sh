#!/usr/bin/env bash
# ensure mongo container is running
docker exec -it demo-mongo mongosh -u admin -p password --authenticationDatabase admin --eval 'db = db.getSiblingDB("mydb"); db.items.insertMany([{id:1,name:"John",designation:"Account manager",city:"Bangalore"},{id:2,name:"Sam",designation:"Product manager",city:"Pune"}]);'