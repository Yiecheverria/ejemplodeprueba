#!/bin/bash
git clone https://github.com/PabloCaiza/library_microservices_v3.git
cd library_microservices_v3
#book microservice
cd app-books
./gradlew libertyPackage
docker build -t yiecheverria/app-books:1.0.0
cd ..
#author microservice 
cd app-authors
docker build -t yiecheverria/app-authors:1.0.0
cd ..
#push docker hub
docker push yiecheverria/app-books:1.0.0
docker push yiecheverria/app-authors:1.0.0
#run docker compose 
docker compose up




