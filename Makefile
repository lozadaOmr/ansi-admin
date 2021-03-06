migrate-reset:
	mysql -u root -h 127.0.0.1 -ppassword -P 3306 -e "use ansible_dev;drop database ansible_dev;create database ansible_dev;"

migrate:
	docker exec -it ansibleadmin_app_1 python manage.py migrate

seed:
	 docker exec -it ansibleadmin_app_1 python manage.py loaddata users.json

migrations:
	docker exec -it ansibleadmin_app_1 python manage.py makemigrations
	- make migrate

collectstatic:
	docker exec -it ansibleadmin_app_1 python manage.py collectstatic

refresh:
	- make migrate-reset
	- make migrate
	- make seed
