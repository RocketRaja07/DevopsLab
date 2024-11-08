FROM openjdk:11-jdk-slim
WORKDIR /app
COPY target/order-service.jar .
EXPOSE 8083
CMD ["java", "-jar", "order-service.jar"]
