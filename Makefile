# Start http proxy for python pip install
docker_proxy:
	docker run -it --rm -p 8118:8118 -d dperson/torproxy

# Create only image.
docker_build:
	#docker-compose build --force-rm --no-cache
	docker build --no-cache --rm -m 2G --network=host --add-host=privoxy:192.168.1.12 -t yvv4docker/work_sa -f Dockerfile.work_sa .

# Push image to docker hub
docker_push:
	docker push yvv4docker/work_sa

# Remove nono images
docker_rmi_none:
	docker images -a |grep none |awk '{print $3}' | xargs docker rmi

# Run container and create it if necessary.
docker_run:
	docker-compose up

# Stop container.
docker_stop:
	docker-compose stop

# Delete image.
docker_rm:
	docker rm work_sa
	docker rmi work_search_analyse_work_sa