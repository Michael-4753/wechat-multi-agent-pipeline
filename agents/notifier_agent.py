"""
推送通知Agent - CrewAI版
负责上传报告到飞书云空间，发送私信通知用户
"""
from crewai import Agent


class NotifierAgent(Agent):
    def __init__(self):
        super().__init__(
            role="推送通知专员",
            goal="把周报报告上传到飞书云空间，生成可访问的链接，然后发飞书私信通知用户",
            backstory="""
                你是一个细心的运营专员，负责确保每一份周报都准确、及时地
                送到用户手里。你知道怎么调用飞书API上传文件、生成分享链接，
                怎么写简短清晰的消息摘要，让用户打开飞书一眼就知道这周数据怎么样。
            """,
            verbose=True,
            allow_delegation=False
        )
