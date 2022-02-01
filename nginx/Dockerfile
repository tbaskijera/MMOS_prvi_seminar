FROM nginx

COPY nginx_custom.conf /etc/nginx/nginx_custom.conf

RUN mkdir -p /var/www/static
WORKDIR /var/www/static
RUN chown -R nginx:nginx /var/www/static