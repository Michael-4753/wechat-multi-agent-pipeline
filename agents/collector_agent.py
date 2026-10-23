"""
数据采集Agent - CrewAI版
负责从公众号后台采集用户数据、内容数据、流量来源数据
"""
from crewai import Agent


class CollectorAgent(Agent):
    def __init__(self):
        super().__init__(
            role="公众号数据采集专家",
            goal="从公众号后台准确、完整地采集用户数据、内容数据和流量来源数据",
            backstory="""
                你是一个经验丰富的公众号数据采集工程师，擅长使用浏览器自动化工具
                从微信公众号后台提取数据。你知道公众号后台的每个数据入口在哪里，
                知道怎么爬取用户分析、内容分析、菜单分析等各个模块的数据，
                并且能把原始数据整理成结构化的JSON格式。
            """,
            verbose=True,
            allow_delegation=False
        )
