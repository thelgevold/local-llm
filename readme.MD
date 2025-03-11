## Install Dependencies

docker-compose up

## Download a model

###Examples:

To download a specific model run the following command in a separate console after running docker-compose up

docker exec -it ollama-docker ollama run llama3.1

docker exec -it ollama-docker ollama run mistral-nemo

## Create a new local model from a fine tunes GGUF
docker exec -it ollama-docker ollama create custom_llama8B -f /root/.ollama/custom/Modelfile