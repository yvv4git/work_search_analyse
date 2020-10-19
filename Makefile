# Этого делать не надо, ибо у меня только один контейнер.
# docker_volume:
#	docker volume create --driver local --opt type=none --opt device=/home/yvv/data/prog/prjs/work_search_analyse/dump/ --opt o=bind hh_dump

# Create only image.
docker_build:
	docker-compose build

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