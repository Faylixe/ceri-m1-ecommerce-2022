FROM node:slim AS build

WORKDIR /app
COPY package*.json /app/
RUN yarn install
COPY ./ /app/
RUN yarn run build

FROM nginx:stable

COPY --from=build /app/build/ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf