docker pull amazonlinux
docker run -dit --name amazonlinux1 amazonlinux
docker cp ./lib 6fa099639e79:/copied

docker attach #<container_id>
yum list installed
yum install python3
