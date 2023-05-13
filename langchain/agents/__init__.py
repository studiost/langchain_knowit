"""Interface for agents."""

"""
定义了一系列的Agent和工具函数，包括：
- Agent: Agent的基类
- AgentExecutor: 执行Agent的类
- AgentOutputParser: 解析Agent输出的类
- BaseMultiActionAgent: 处理多个action的Agent的基类
- BaseSingleActionAgent: 处理单个action的Agent的基类
- LLMSingleActionAgent: 处理单个action的LLM（Language Model Masked）Agent的基类
- create_csv_agent: 创建输出为csv文件的Agent的函数
- create_json_agent: 创建输出为json文件的Agent的函数
- create_openapi_agent: 创建输出为OpenAPI文档的Agent的函数
- create_pandas_dataframe_agent: 创建输出为pandas DataFrame的Agent的函数
- create_pbi_agent: 创建输出为Power BI数据模型的Agent的函数
- create_pbi_chat_agent: 创建输出为Power BI聊天的Agent的函数
- create_spark_dataframe_agent: 创建输出为Spark DataFrame的Agent的函数
- create_sql_agent: 创建输出为SQL语句的Agent的函数
- create_vectorstore_agent: 创建输出为vector store的Agent的函数
- create_vectorstore_router_agent: 创建输出为vector store router的Agent的函数
- AgentType: Agent的类型
- ConversationalAgent: 处理对话的Agent的基类
- ConversationalChatAgent: 处理聊天对话的Agent的基类
- initialize_agent: 初始化Agent的函数
- get_all_tool_names: 获取所有可用的工具函数名的函数
- load_agent: 加载Agent的函数
- load_huggingface_tool: 加载huggingface工具的函数
- load_tools: 加载工具的函数
- MRKLChain: 处理MRKL的Agent的基类
- ReActChain: 处理ReAct的Agent的基类
- ReActTextWorldAgent: 处理ReAct TextWorld的Agent的基类
- SelfAskWithSearchChain: 处理自我提问并搜索的Agent的基类
- StructuredChatAgent: 处理结构化对话的Agent的基类
- Tool: 工具函数的基类
- ZeroShotAgent: 处理ZeroShot的Agent的基类
"""

from langchain.agents.agent import (
    Agent,
    AgentExecutor,
    AgentOutputParser,
    BaseMultiActionAgent,
    BaseSingleActionAgent,
    LLMSingleActionAgent,
)
from langchain.agents.agent_toolkits import (
    create_csv_agent,
    create_json_agent,
    create_openapi_agent,
    create_pandas_dataframe_agent,
    create_pbi_agent,
    create_pbi_chat_agent,
    create_spark_dataframe_agent,
    create_sql_agent,
    create_vectorstore_agent,
    create_vectorstore_router_agent,
)
from langchain.agents.agent_types import AgentType
from langchain.agents.conversational.base import ConversationalAgent
from langchain.agents.conversational_chat.base import ConversationalChatAgent
from langchain.agents.initialize import initialize_agent
from langchain.agents.load_tools import (
    get_all_tool_names,
    load_huggingface_tool,
    load_tools,
)
from langchain.agents.loading import load_agent
from langchain.agents.mrkl.base import MRKLChain, ZeroShotAgent
from langchain.agents.react.base import ReActChain, ReActTextWorldAgent
from langchain.agents.self_ask_with_search.base import SelfAskWithSearchChain
from langchain.agents.structured_chat.base import StructuredChatAgent
from langchain.agents.tools import Tool, tool

__all__ = [
    "Agent",
    "AgentExecutor",
    "AgentOutputParser",
    "AgentType",
    "BaseMultiActionAgent",
    "BaseSingleActionAgent",
    "ConversationalAgent",
    "ConversationalChatAgent",
    "LLMSingleActionAgent",
    "MRKLChain",
    "ReActChain",
    "ReActTextWorldAgent",
    "SelfAskWithSearchChain",
    "StructuredChatAgent",
    "Tool",
    "ZeroShotAgent",
    "create_csv_agent",
    "create_json_agent",
    "create_openapi_agent",
    "create_pandas_dataframe_agent",
    "create_pbi_agent",
    "create_pbi_chat_agent",
    "create_spark_dataframe_agent",
    "create_sql_agent",
    "create_vectorstore_agent",
    "create_vectorstore_router_agent",
    "get_all_tool_names",
    "initialize_agent",
    "load_agent",
    "load_huggingface_tool",
    "load_tools",
    "tool",
]
