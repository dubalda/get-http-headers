docker build -f Dockerfile.python -t http-headers-python . && docker run --rm -p 5002:5002 --name http-headers-python http-headers-python

docker run -it --rm --name http-headers-python -v "$PWD/python":/usr/src/myapp -w /usr/src/myapp -p 5002:5002 python:3 python webserver.py


sudo firewall-cmd --add-port 5002/tcp
sudo firewall-cmd --list-all | less
