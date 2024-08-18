from crewai_tools import YoutubeChannelSearchTool

yt_tool= YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06',config=dict(
        llm=dict(
            provider="ollama"
        )
    ))