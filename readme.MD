## Install Dependencies

docker-compose up

## Download a model

###Examples:

To download a specific model run the following command after substituting the model you want (e.g.mistral-nemo, etc). Run this command in a separate console after docker-compose up is already running

docker exec -it ollama-docker ollama run [some model name]

Llama 3.1:

docker exec -it ollama-docker ollama run llama3.1


