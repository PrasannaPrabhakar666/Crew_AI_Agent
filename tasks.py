from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task=Task(
    description=("Identify the video {topic}."
    "Get detailed information about the video from the channel video."),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    agent=blog_researcher,
    tools=[yt_tool]
)

write_task= Task(
    description=( "get the info from the youtube channel on the topic {topic}."),
    output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
    agent=blog_writer,
    tools=[yt_tool],
    async_execution=False,
    output_file='output.md'
)