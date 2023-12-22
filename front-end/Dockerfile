# BUILD STAGE
FROM node:lts-alpine as build-stage

# make the 'node-docker' folder the current working directory
WORKDIR /node-docker

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# get API var arguments from building process and put them in an env file
ARG VITE_API_HOST
ARG VITE_API_PORT

RUN echo "VITE_API_HOST=${VITE_API_HOST}" >> .env.production
RUN echo "VITE_API_PORT=${VITE_API_PORT}" >> .env.production

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'node-docker' folder)
COPY . .

# build app for production stage
RUN npm run build


# PRODUCTION STAGE
FROM nginx:alpine

# remove default static files
RUN rm -rf /usr/share/nginx/html/*

# copy built app from build stage
COPY --from=build-stage /node-docker/dist /usr/share/nginx/html/

# expose HTTP port (unsecure)
EXPOSE 80

# set entrypoint for nginx image
ENTRYPOINT ["nginx", "-g", "daemon off;"]
