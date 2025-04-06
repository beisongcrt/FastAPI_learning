myapp/
├── main.py                👉 启动文件，注册所有路由
├── api/                   👉 所有接口按功能模块拆分
│   ├── __init__.py
│   ├── chat.py            👉 聊天接口
│   └── calc.py            👉 计算接口
├── models/
│   ├── __init__.py
│   └── schemas.py         👉 所有数据模型
└── requirements.txt       👉 项目依赖（可选）
