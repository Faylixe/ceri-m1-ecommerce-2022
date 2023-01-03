FROM node:18.12.0 AS node
WORKDIR /appli_ecommerce
COPY package.json .
COPY . .
RUN npm install -g npm@9.2.0
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/configfile.template
COPY --from=node /appli_ecommerce/dist/appli_ecommerce /usr/share/nginx/html
ENV PORT 8080
ENV HOST 0.0.0.0
EXPOSE 8080
CMD sh -c "envsubst '\$PORT' < /etc/nginx/conf.d/configfile.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
