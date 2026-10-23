"""
所有任务定义 - CrewAI版
每个任务对应一个Agent的具体工作内容
"""
from crewai import Task


# 任务1：数据采集
collect_data_task = Task(
    description="""
    从公众号后台采集以下数据：
    1. 用户分析：累计粉丝、近30天新增、近30天取关、粉丝来源分布
    2. 内容分析：近30天总阅读、发布文章数、TOP5文章阅读量
    3. 流量分析：推荐、搜一搜、朋友圈、公众号主页各渠道占比
    
    输出结构化的JSON数据，确保每个数字都准确，不要编造。
    """,
    expected_output="结构化的原始数据JSON，包含user_data、content_data、traffic_data三个部分",
    agent=None  # 后面在crew里绑定
)

# 任务2：数据分析
analyze_data_task = Task(
    description="""
    基于采集到的原始数据，完成以下分析：
    1. 计算7个核心指标：粉丝总量、近30天净增、总阅读、爆款文章、推荐流量占比、文章页涨粉占比、爆款贡献占比
    2. 识别异常：有没有哪个指标突然大幅波动？哪个流量渠道占比过高有风险？
    3. 提炼3条关键洞察：从数据里能看出什么反常识的结论？对下周内容创作有什么指导？
    
    要求：洞察必须是可执行的，不要说正确的废话。
    """,
    expected_output="核心指标清单 + 异常提示 + 3条关键洞察（每条包含标题和详细说明）",
    agent=None
)

# 任务3：报告生成
generate_report_task = Task(
    description="""
    基于分析结果，生成手机版HTML周报：
    1. 标题：公众号周报 + 日期
    2. 核心指标卡片：7个核心指标用卡片形式展示，大数字+小标签
    3. 关键洞察：3条洞察用高亮框展示
    4. 风格：简洁现代，适合手机阅读，主色调用#667eea
    
    同时生成一段简短的飞书消息摘要（200字以内），包含5个核心数字。
    """,
    expected_output="完整的手机版HTML代码 + 飞书消息摘要文本",
    agent=None
)

# 任务4：推送通知
push_notification_task = Task(
    description="""
    完成以下推送动作：
    1. 把生成的HTML报告保存到outputs目录
    2. 模拟上传到飞书云空间，生成分享链接
    3. 发送飞书私信，内容是：周报摘要 + 报告链接
    
    最后返回推送是否成功。
    """,
    expected_output="推送结果，包含报告链接和发送状态",
    agent=None
)
