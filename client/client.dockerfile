FROM node:16-alpine3.15

WORKDIR /client

COPY package*.json /client

RUN yarn install

COPY . .

CMD [ "yarn", "dev" ]