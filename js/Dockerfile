ARG NODE_VERSION=22.12.0

FROM node:${NODE_VERSION} AS base

WORKDIR /js
COPY package.json package-lock.json ./
RUN npm install

COPY . . 

CMD [ "npm", "run", "serve" ]
