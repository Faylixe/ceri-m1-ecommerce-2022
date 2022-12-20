FROM node:18.12.0 AS node
WORKDIR /appli_ecommerce
COPY package.json .
COPY . .
RUN npm install -g npm@9.2.0
FROM nginx:alpine
COPY --from=node /appli_ecommerce/dist/appli_ecommerce /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]