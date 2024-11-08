FROM openjdk:11-jdk-slim
WORKDIR /app
COPY target/product-service.jar .
EXPOSE 8082
CMD ["java", "-jar", "product-service.jar"]
