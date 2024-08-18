from crewai import Agent
from tools import yt_tools
from langchain_openai import ChatOpenAI
from langchain_community.llms import ollama

model = ollama(model="mistral:7b")

import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model = "crewai-mistral7b",
    base_url = "http://localhost:11434/v1")

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    backstory=("Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion"),
    memory=True,
    allow_delegation=True,
    tools=[yt_tools],
    llm=llm
)

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    tools=[yt_tools],
    backstory=( "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."),
    allow_delegation=False,
    llm=llm
)