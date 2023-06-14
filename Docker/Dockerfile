# Use the official Nginx image as the base image
FROM nginx:latest

# Install the curl package
RUN apt-get update && apt-get install -y curl

# Copy the custom Nginx configuration file to the container
#COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for incoming traffic
EXPOSE 80