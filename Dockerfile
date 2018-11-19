FROM ubuntu:16.04

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y curl
RUN apt-get install -y python3 python3-pip
RUN pip3 install Flask flask_json pyyaml numpy requests prettytable flask_cors tqdm matplotlib pillow gunicorn psutil -U flask-cors

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g @vue/cli

RUN apt-get install -y nginx

WORKDIR /simulation

COPY goodbackend goodbackend
COPY goodbackend/saveddata goodbackend/saveddata
COPY vuefront vuefront

COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh entrypoint.sh

RUN cd vuefront/ && npm install && npm i vue-resource && npm i bootstrap-vue && npm run build && cd ../
RUN chmod +x entrypoint.sh

ENTRYPOINT ./entrypoint.sh


# docker load -i dockedSimulation.docker
# docker save -o dockedSimulation.docker simulation
# docker run --rm -ti -v C:/Users/Zeus/Desktop/saveddata:/simulation/backend/saveddata --name simulation -p 80:80 simulation
# docker run --rm -ti -v /opt/saveddata:/simulation/backend/saveddata --name simulation -p 80:80 simulation
# docker build -t simulation -f Dockerfile .
# docker build -t test -f Dockerfile .
# docker run --rm -ti -v /Users/jobraf/Desktop/saveddata:/simulation/backend/saveddata --name simulation -p 80:80 test
# docker run --rm -ti -v /opt/saveddata:/simulation/backend/saveddata --name simulation -p 80:80 test

# docker run --rm -d -v /opt/saveddata:/simulation/backend/saveddata --name simulation1 -p 80:80 simulation1
#  docker logs -f simulation1
# docker exec -ti simulation1 /bin/bash



# docker run --rm -ti -v /Users/jobraf/Desktop/saveddata:/simulation/backend/saveddata --name simulation -p 80:80 simulation
# docker run --rm -d -v /Users/jobraf/Desktop/saveddata:/simulation/backend/saveddata --name simulation -p 80:80 simulation