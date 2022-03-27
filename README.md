The main.py is afterwards containerized using Docker.

To run the code, you must have Docker installed on your machine.

Download all the files, navigate into your download folder using the terminal and run the next docker commands:

    1) docker build -t python-imdb . (builds the Docker Image using the Dockerfile)
    2) docker run -t -i python-imdb (runs the Docker Container)
