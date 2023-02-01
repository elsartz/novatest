# Build step #2: build the API with the client as static files
FROM python:3.10.5
WORKDIR /app
# COPY --from=build-step /app/build ./build

# RUN mkdir ./api
# COPY api/requirements.txt api/api.py api/.flaskenv ./api
# COPY ./requirements.txt ./
RUN pip freeze > requirements.txt
RUN pip install -r ./requirements.txt
ENV FLASK_ENV production
COPY . .
EXPOSE 5000
# WORKDIR /app/api
CMD ["gunicorn", "-b", ":5000", "app:create_app()"]

# Build step #1: build the React front end
FROM node:16.14.2-alpine3.15
WORKDIR /
ENV PATH /node_modules/.bin:$PATH
COPY package.json package-lock.json ./
COPY ./src ./src
# COPY ./public ./public
RUN npm install
COPY . .

# run the build command
RUN npm run dev

# set the command to start the application
CMD ["npm", "dev"]