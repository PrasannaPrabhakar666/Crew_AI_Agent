#!/bin/zsh

model_name = "mistral:7b"
custom_model_name = "crewai-mistral"

ollama pull $model_name

ollama create $custom_model_name -f ./Mistral7bModelFile
