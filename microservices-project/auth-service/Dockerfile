FROM openjdk:11-jdk-slim
WORKDIR /app
COPY target/auth-service.jar .
EXPOSE 8081
CMD ["java", "-jar", "auth-service.jar"]
