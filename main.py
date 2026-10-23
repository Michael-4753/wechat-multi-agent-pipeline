"""
入口文件 - 运行完整的公众号周报生成流水线
"""
from crew import create_weekly_report_crew


def main():
    print("=" * 60)
    print("🚀 公众号周报多Agent流水线启动（CrewAI版）")
    print("=" * 60)

    # 创建Crew
    crew = create_weekly_report_crew()

    # 运行流水线
    result = crew.kickoff()

    print("\n" + "=" * 60)
    print("✅ 流水线执行完毕！")
    print("=" * 60)
    print(f"最终结果:\n{result}")


if __name__ == "__main__":
    main()
