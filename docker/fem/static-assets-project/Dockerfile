# run
# docker build -t static-app .
# docker run -p 8080:80 static-app
# 80 is nginx default

# build stage, or node:latest, builder is variable name
FROM node:alpine AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build

# run stage
# you could use nginx:latest
FROM nginx:1.17
COPY --from=builder /app/build /usr/share/nginx/html
# or COPY --from=0