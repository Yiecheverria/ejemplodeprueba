#FROM arm64v8/eclipse-temurin:17
#FROM eclipse-temurin:17.0.5_8-jre-alpine
FROM openjdk:17
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    libssl-dev \
#    && rm -rf /var/lib/apt/lists/*
RUN mkdir /app
WORKDIR /app
COPY build/libs/app-books.jar ./app.jar
CMD ["java","-jar","app.jar"]