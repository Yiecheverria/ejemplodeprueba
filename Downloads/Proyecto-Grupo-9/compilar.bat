git clone https://github.com/PabloCaiza/library_microservices_v3.git && cd ./Proyecto-Grupo-9 && cd ./app-books && gradlew libertyPackage && docker build -t jaimesalvador/app-books:1.0.0 . && cd .. && cd ./app-authors && docker build -t jaimesalvador/app-authors:1.0.0 . && cd .. && docker push jaimesalvador/app-books:1.0.0 && docker push jaimesalvador/app-authors:1.0.0 && docker compose up

