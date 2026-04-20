FROM node:18-alpine

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

EXPOSE 3000

ENV FRONTEND_PORT=3000

CMD ["node", "./bin/www"]
