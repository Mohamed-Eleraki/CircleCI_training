FROM node:latest

# Create app directory
WORKDIR /usr/src/app

# Copy the node files from the node-package directory
#COPY ../node-package/* ./
COPY /node-package/* ./

# Install app dependencies
RUN npm install

# start app
RUN npm stars

# Bundle app source
COPY . .

# Expose the port that the app will run on
EXPOSE 3000

# Start the app
CMD [ "npm", "start" ]