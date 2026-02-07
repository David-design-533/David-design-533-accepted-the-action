# David-design-533-accepted-the-action

## 项目内容 / Project Contents

本仓库包含以下项目：

### 1. 肺部变化可视化模型 / Lung Visualization Model

一个用于展示抽烟对肺部影响的交互式3D可视化教育工具。

**特性：**
- 3D肺部结构模型
- 分阶段吸烟影响模拟（1年、5年、10年、20年、30年）
- 实时健康指标监测
- 交互式时间轴控制

📁 **项目目录**: `lung_visualization/`
📖 **文档**: [lung_visualization/README.md](lung_visualization/README.md)

**快速开始：**
```bash
cd lung_visualization
python3 serve.py
# 打开浏览器访问: http://localhost:8000/index.html
```

### 2. 图书馆管理系统流程图 / Library Management System Flowchart

flowchart TD
    %% 定义子图（泳道）
    subgraph Library_System [图书馆管理系统 (LMS)]
        direction TB
        
        subgraph Manage_Dept [采编与管理部门]
            direction TB
            Procurement[图书采购管理] --> Financial[财务预算管理]
            Financial --> Cataloging[图书编目与分类]
            Cataloging --> AssetMgmt[典藏/资产管理]
            AssetMgmt --> Quality[入馆质量检查]
        end

        subgraph Circulation_Dept [流通与书库部门]
            direction TB
            Shelving[图书上架] --> Inventory[库存跟踪]
            Inventory --> LocationMgmt[架位/层架移动]
            
            BorrowingReq[借阅申请] --> CheckOut[借出扫描处理]
            CheckOut --> DueDate[生成应还日期]
            
            ReturnReq[归还申请] --> CheckIn[归还扫描处理]
            CheckIn --> ConditionCheck[书况核验]
            ConditionCheck --> Reshelving[回库/重新上架]
        end

        subgraph Reader_Service [读者服务终端]
            direction TB
            Search[图书检索/OPAC] --> Reservation[预约/预留]
            Reservation --> BorrowingReq
            
            BorrowingHistory[借阅历史记录]
            FineMgmt[逾期罚款管理]
        end
    end

    %% 跨部门流程关系
    Procurement -->|新书入库| Shelving
    Cataloging -->|元数据同步| Search
    
    LocationMgmt -.->|更新位置| Search
    
    CheckOut -->|状态更新:已借出| Inventory
    CheckOut -->|记录日志| BorrowingHistory
    
    CheckIn -->|状态更新:在馆| Inventory
    CheckIn -->|检查是否逾期| FineMgmt
    
    Reshelving --> Shelving

    %% 样式设置 (模仿原图色调)
    classDef blueFill fill:#e6f3ff,stroke:#333,stroke-width:1px;
    classDef darkBlue fill:#b3d9ff,stroke:#333,stroke-width:1px;
    
    class Procurement,Financial,Cataloging,AssetMgmt,Quality blueFill
    class Shelving,Inventory,LocationMgmt,CheckOut,CheckIn,Reshelving darkBlue
    class Search,Reservation,BorrowingReq,ReturnReq,FineMgmt,BorrowingHistory blueFill