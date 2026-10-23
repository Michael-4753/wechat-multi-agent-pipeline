"""
Crew 编排 - 把Agent和任务组装成完整流水线
"""
from crewai import Crew, Process

from agents import (
    CollectorAgent,
    AnalyzerAgent,
    ReporterAgent,
    NotifierAgent
)
from tasks import (
    collect_data_task,
    analyze_data_task,
    generate_report_task,
    push_notification_task
)


def create_weekly_report_crew():
    """创建公众号周报生成Crew"""

    # 1. 初始化所有Agent
    collector = CollectorAgent()
    analyzer = AnalyzerAgent()
    reporter = ReporterAgent()
    notifier = NotifierAgent()

    # 2. 把Agent绑定到任务
    collect_data_task.agent = collector
    analyze_data_task.agent = analyzer
    generate_report_task.agent = reporter
    push_notification_task.agent = notifier

    # 3. 创建Crew（团队）
    crew = Crew(
        agents=[collector, analyzer, reporter, notifier],
        tasks=[
            collect_data_task,
            analyze_data_task,
            generate_report_task,
            push_notification_task
        ],
        process=Process.sequential,  # 串行执行，一个任务做完再做下一个
        verbose=True
    )

    return crew
