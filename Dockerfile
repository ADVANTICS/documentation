FROM node:latest

RUN npm install -g docsify-cli

WORKDIR /app
EXPOSE 3000

ENTRYPOINT [ "docsify" ]
CMD ["serve", "--port", "3000", "."]
