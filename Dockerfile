# FROM node:16.14.2-alpine3.14
# WORKDIR /
# COPY . .
# RUN npm install --production
# CMD ["npm", "start"]
# EXPOSE 3000

# Build step #1: build the React front end
FROM node:16.14.2-alpine3.15
WORKDIR /
ENV PATH /node_modules/.bin:$PATH
COPY package.json package-lock.json ./
COPY ./src ./src
# COPY ./public ./public
RUN npm install
RUN npm build
CMD ["npm", "start"]
EXPOSE 3000

# Build step #2: build the API with the client as static files
FROM python:3.10.5
WORKDIR /app
# COPY --from=build-step /app/build ./build

# RUN mkdir ./api
# COPY api/requirements.txt api/api.py api/.flaskenv ./api
RUN pip install -r /requirements.txt
ENV FLASK_ENV production

EXPOSE 5000
# WORKDIR /app/api
CMD ["gunicorn", "-b", ":5000", "app:create_app()"]