import httpx

from app.config import settings

DEFAULT_DATA = {
    "glossary": {
        "String": {
            "definition": "字符串（String）是一种数据类型，用于表示文本数据。它由一系列字符组成，包括字母、数字、符号和空格。",
            "characteristics": ["不可变性：在某些语言中，字符串一旦创建就不能被修改", "有序性：字符按特定顺序排列，可以通过索引访问"],
            "example": "Hello, World!",
            "related_concepts": ["Character", "Index"]
        },
        "Function": {
            "definition": "函数（Function）是一段可重复使用的代码块，它接受输入参数，执行特定任务，并可能返回结果。",
            "characteristics": ["封装性：将复杂逻辑封装在一个名称下", "可重用性：同一函数可以在不同位置多次调用"],
            "example": "def greet(name): return f\"Hello, {name}!\"",
            "related_concepts": ["Parameter", "Return Value", "Method"]
        },
        "Variable": {
            "definition": "变量（Variable）是用于存储数据值的命名内存位置。变量的值可以在程序执行过程中改变。",
            "characteristics": ["命名规则：必须遵循语言的标识符命名规范", "数据类型：每个变量都有特定的数据类型"],
            "example": "age = 25",
            "related_concepts": ["Data Type", "Assignment"]
        },
        "Parameter": {
            "definition": "参数（Parameter）是函数定义中声明的变量，用于接收调用者传递的值。",
            "characteristics": ["形式参数：函数定义中的变量名", "实际参数：调用函数时传递的实际值"],
            "example": "def add(a, b): return a + b",
            "related_concepts": ["Function", "Argument"]
        },
        "Return Value": {
            "definition": "返回值（Return Value）是函数执行完毕后返回给调用者的值。",
            "characteristics": ["类型一致性：返回值类型必须与函数声明一致", "可选性：函数可以没有返回值"],
            "example": "return result",
            "related_concepts": ["Function", "Parameter"]
        },
        "Array": {
            "definition": "数组（Array）是一种数据结构，用于存储相同类型的多个元素。数组中的元素通过索引来访问。",
            "characteristics": ["固定大小：数组创建后大小不能改变", "同质性：所有元素必须是相同类型"],
            "example": "int numbers[] = {1, 2, 3, 4, 5}",
            "related_concepts": ["Index", "List"]
        },
        "Index": {
            "definition": "索引（Index）是用于标识数组、字符串或其他有序数据结构中元素位置的整数值。在大多数编程语言中，索引通常从0开始计数。",
            "characteristics": ["从零开始：大多数语言索引从0开始", "非负整数：索引必须是非负整数"],
            "example": "text[0] // 访问第一个字符",
            "related_concepts": ["Array", "String"]
        },
        "Loop": {
            "definition": "循环（Loop）是一种控制结构，用于重复执行一段代码直到满足特定条件。",
            "characteristics": ["循环条件：决定循环是否继续执行", "循环体：需要重复执行的代码块"],
            "example": "for (int i = 0; i < 10; i++) { }",
            "related_concepts": ["Condition", "Iteration"]
        },
        "Class": {
            "definition": "类（Class）是面向对象编程的基本构件，用于创建对象的蓝图或模板。类定义了对象的属性和方法。",
            "characteristics": ["封装性：将数据和操作数据的方法绑定在一起", "继承性：子类可以继承父类的属性和方法"],
            "example": "class Person { String name; void greet() { } }",
            "related_concepts": ["Object", "Method", "Attribute"]
        },
        "Method": {
            "definition": "方法（Method）是与类或对象关联的函数。方法定义了类或对象可以执行的操作。",
            "characteristics": ["绑定性：方法与特定类或对象绑定", "访问控制：可以设置不同的访问权限"],
            "example": "public void sayHello() { System.out.println(\"Hello!\"); }",
            "related_concepts": ["Class", "Object", "Function"]
        },
        "Operator": {
            "definition": "运算符（Operator）是用于执行特定运算的符号。运算符可以操作一个或多个操作数并产生结果。",
            "characteristics": ["优先级：不同运算符有不同的执行优先级", "结合性：相同优先级运算符的执行顺序"],
            "example": "a + b, x > y, !condition",
            "related_concepts": ["Operand", "Expression"]
        },
        "List": {
            "definition": "列表（List）是一种动态数据结构，可以存储任意类型的元素，大小可以动态增长。",
            "characteristics": ["动态大小：可以根据需要添加或删除元素", "异质性：可以存储不同类型的元素"],
            "example": "my_list = [1, \"hello\", 3.14]",
            "related_concepts": ["Array", "Index"]
        },
        "Dictionary": {
            "definition": "字典（Dictionary）是一种键值对的数据结构，通过键来快速访问对应的值。",
            "characteristics": ["键唯一性：每个键只能出现一次", "快速查找：通过键可以O(1)时间复杂度访问值"],
            "example": "person = {\"name\": \"Alice\", \"age\": 25}",
            "related_concepts": ["Key", "Value"]
        },
        "Module": {
            "definition": "模块（Module）是一个包含相关代码的文件，可以被其他程序导入和使用。",
            "characteristics": ["代码组织：将相关功能组织在一起", "可重用性：可以在多个项目中使用"],
            "example": "import math",
            "related_concepts": ["Package", "Import"]
        },
        "Exception": {
            "definition": "异常（Exception）是程序运行时发生的错误或意外情况。",
            "characteristics": ["可捕获性：可以使用try-catch语句捕获和处理", "层次结构：异常通常形成类层次结构"],
            "example": "try: risky_code() except Exception as e: handle_error(e)",
            "related_concepts": ["Error", "Try-Catch"]
        }
    },
    "languages": {
        "python": {
            "name": "Python",
            "description": "Python 是一种高级、解释型、通用的编程语言，以其简洁的语法和强大的功能著称。",
            "elements": [
                {
                    "id": "python_print",
                    "name": "print()",
                    "description": "输出函数，用于在控制台打印指定的内容",
                    "search_keywords": ["打印", "输出", "显示", "print", "输出到控制台", "console", "日志"],
                    "technical_explanation": "print() 是 Python 的内置<a class=\"glossary-term\" data-term=\"Function\">函数</a>，用于将指定的对象输出到标准输出流（通常是控制台）。",
                    "metaphor_explanation": "你可以把 print() <a class=\"glossary-term\" data-term=\"Function\">函数</a>想象成一个公告牌。当你有话要说时，把内容写在纸上交给公告牌管理员（调用 print()），管理员会帮你把内容张贴在公告板上（输出到控制台）。",
                    "examples": [
                        { "title": "基本输出", "code": "print(\"Hello, World!\")\n# 输出: Hello, World!" },
                        { "title": "输出多个对象", "code": "name = \"Alice\"\nage = 25\nprint(\"Name:\", name, \"Age:\", age)\n# 输出: Name: Alice Age: 25" },
                        { "title": "自定义分隔符", "code": "print(\"a\", \"b\", \"c\", sep=\"-\")\n# 输出: a-b-c" }
                    ],
                    "syntax_notes": [
                        "print() 是一个<a class=\"glossary-term\" data-term=\"Function\">函数</a>，必须使用圆括号调用",
                        "可以接受任意数量的位置<a class=\"glossary-term\" data-term=\"Parameter\">参数</a>",
                        "默认情况下，print() 会在每次调用后添加换行符",
                        "可以使用 sep 参数指定多个对象之间的分隔符",
                        "可以使用 end 参数指定结尾字符"
                    ],
                    "related_terms": ["Function", "Parameter", "String"]
                },
                {
                    "id": "python_input",
                    "name": "input()",
                    "description": "输入函数，用于从控制台获取用户输入",
                    "search_keywords": ["输入", "获取", "读取", "input", "用户输入", "控制台输入"],
                    "technical_explanation": "input() 是 Python 的内置<a class=\"glossary-term\" data-term=\"Function\">函数</a>，用于从标准输入（通常是键盘）读取一行文本。",
                    "metaphor_explanation": "你可以把 input() <a class=\"glossary-term\" data-term=\"Function\">函数</a>想象成一个调查问卷。程序停下来说：\"请填写你的答案\"，然后等待你填写。",
                    "examples": [
                        { "title": "基本输入", "code": "name = input(\"请输入你的名字: \")\nprint(f\"你好, {name}!\")" },
                        { "title": "获取数字输入", "code": "age = int(input(\"请输入你的年龄: \"))\nprint(f\"明年你将 {age + 1} 岁\")" }
                    ],
                    "syntax_notes": [
                        "input() 的<a class=\"glossary-term\" data-term=\"Return Value\">返回值</a>始终是<a class=\"glossary-term\" data-term=\"String\">字符串</a>类型",
                        "如果需要获取数字，需要使用 int() 或 float() 进行类型转换"
                    ],
                    "related_terms": ["Function", "Return Value", "String", "Variable"]
                },
                {
                    "id": "python_for",
                    "name": "for 循环",
                    "description": "迭代循环，用于遍历可迭代对象中的元素",
                    "search_keywords": ["循环", "遍历", "迭代", "for", "循环语句"],
                    "technical_explanation": "for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>是 Python 中的一种控制结构，用于遍历可迭代对象中的每个元素。",
                    "metaphor_explanation": "你可以把 for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>想象成一个分拣员。他有一篮子水果，需要对每个水果进行检查。",
                    "examples": [
                        { "title": "遍历列表", "code": "fruits = [\"apple\", \"banana\", \"cherry\"]\nfor fruit in fruits:\n    print(f\"我喜欢 {fruit}\")" },
                        { "title": "使用 range()", "code": "for i in range(5):\n    print(f\"计数: {i}\")" },
                        { "title": "遍历字典", "code": "person = {\"name\": \"Alice\", \"age\": 25}\nfor key, value in person.items():\n    print(f\"{key}: {value}\")" }
                    ],
                    "syntax_notes": [
                        "for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>后面必须跟冒号",
                        "<a class=\"glossary-term\" data-term=\"Loop\">循环</a>体必须缩进（通常4个空格）",
                        "可以使用 break 语句提前退出循环",
                        "可以使用 continue 语句跳过当前迭代"
                    ],
                    "related_terms": ["Loop", "Variable", "List", "Dictionary"]
                },
                {
                    "id": "python_if",
                    "name": "if 语句",
                    "description": "条件判断语句，根据条件执行不同的代码块",
                    "search_keywords": ["条件", "判断", "如果", "if", "条件判断", "分支"],
                    "technical_explanation": "if 语句是 Python 中的条件控制结构，用于根据条件表达式的结果执行不同的代码块。",
                    "metaphor_explanation": "你可以把 if 语句想象成一个交通信号灯。当绿灯亮时，车辆可以通行；当红灯亮时，车辆需要等待。",
                    "examples": [
                        { "title": "基本 if 语句", "code": "age = 18\nif age >= 18:\n    print(\"你已经成年了\")" },
                        { "title": "if-else 语句", "code": "age = 15\nif age >= 18:\n    print(\"成年人\")\nelse:\n    print(\"未成年人\")" },
                        { "title": "if-elif-else 语句", "code": "score = 85\nif score >= 90:\n    print(\"优秀\")\nelif score >= 80:\n    print(\"良好\")\nelif score >= 60:\n    print(\"及格\")\nelse:\n    print(\"不及格\")" }
                    ],
                    "syntax_notes": [
                        "if、elif、else 后面必须跟冒号",
                        "代码块必须缩进",
                        "条件表达式的结果会被转换为布尔值"
                    ],
                    "related_terms": ["Loop", "Operator", "Variable"]
                },
                {
                    "id": "python_def",
                    "name": "def 函数定义",
                    "description": "定义一个新的函数，封装可重用的代码块",
                    "search_keywords": ["函数", "定义", "def", "function", "创建函数"],
                    "technical_explanation": "def 关键字用于在 Python 中定义一个新的<a class=\"glossary-term\" data-term=\"Function\">函数</a>。",
                    "metaphor_explanation": "你可以把 def 关键字想象成一个工具箱的标签。当你定义一个<a class=\"glossary-term\" data-term=\"Function\">函数</a>时，就像是在给一个工具箱贴上标签。",
                    "examples": [
                        { "title": "基本函数定义", "code": "def greet():\n    print(\"Hello, World!\")\n\ngreet()" },
                        { "title": "带参数的函数", "code": "def greet(name):\n    print(f\"Hello, {name}!\")\n\ngreet(\"Alice\")" },
                        { "title": "带返回值的函数", "code": "def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)  # 输出: 8" },
                        { "title": "默认参数", "code": "def greet(name=\"World\"):\n    print(f\"Hello, {name}!\")\n\ngreet()           # 输出: Hello, World!\ngreet(\"Alice\")   # 输出: Hello, Alice!" }
                    ],
                    "syntax_notes": [
                        "def 关键字后面必须跟<a class=\"glossary-term\" data-term=\"Function\">函数</a>名和圆括号",
                        "<a class=\"glossary-term\" data-term=\"Function\">函数</a>定义行末尾必须有冒号",
                        "函数体必须缩进",
                        "使用 return 语句返回值"
                    ],
                    "related_terms": ["Function", "Parameter", "Return Value"]
                },
                {
                    "id": "python_while",
                    "name": "while 循环",
                    "description": "条件循环，当条件为真时重复执行代码块",
                    "search_keywords": ["循环", "while", "条件循环", "重复执行", "循环语句", "无限循环"],
                    "technical_explanation": "while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>是 Python 中的一种控制结构，用于在条件表达式为 true 时重复执行一段代码块。与 for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>不同，while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>适用于不确定迭代次数的场景。",
                    "metaphor_explanation": "你可以把 while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>想象成一个等待信号灯的司机。司机不断检查信号灯（检查条件），只要红灯亮着（条件为 true），就继续等待（执行循环体）。只有当绿灯亮起（条件变为 false）时，司机才会继续前进（退出循环）。",
                    "examples": [
                        { "title": "基本 while 循环", "code": "count = 0\nwhile count < 5:\n    print(f\"当前计数: {count}\")\n    count += 1" },
                        { "title": "while-else 循环", "code": "count = 0\nwhile count < 3:\n    print(f\"计数: {count}\")\n    count += 1\nelse:\n    print(\"循环正常结束\")" }
                    ],
                    "syntax_notes": [
                        "while 关键字后面必须跟条件表达式和冒号",
                        "<a class=\"glossary-term\" data-term=\"Loop\">循环</a>体必须缩进（通常4个空格）",
                        "如果条件始终为 true，会形成无限<a class=\"glossary-term\" data-term=\"Loop\">循环</a>",
                        "可以使用 break 语句提前退出<a class=\"glossary-term\" data-term=\"Loop\">循环</a>",
                        "while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>可以搭配 else 子句"
                    ],
                    "related_terms": ["Loop", "Variable", "Operator"]
                },
                {
                    "id": "python_list",
                    "name": "List 列表",
                    "description": "有序、可变的集合，可以存储任意类型的元素",
                    "search_keywords": ["列表", "list", "数组", "集合", "数据结构"],
                    "technical_explanation": "列表（List）是 Python 中最常用的数据结构之一，是一个有序、可变的元素集合。<a class=\"glossary-term\" data-term=\"List\">列表</a>中的元素可以是不同类型。",
                    "metaphor_explanation": "你可以把列表想象成一个购物清单。你可以添加新物品、删除物品、修改物品，清单上的物品有固定的顺序。",
                    "examples": [
                        { "title": "创建列表", "code": "fruits = [\"apple\", \"banana\", \"cherry\"]\nnumbers = [1, 2, 3, 4, 5]\nmixed = [\"hello\", 42, 3.14, True]" },
                        { "title": "访问和修改元素", "code": "fruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[0])      # 输出: apple\nfruits[1] = \"orange\"\nprint(fruits)         # 输出: ['apple', 'orange', 'cherry']" },
                        { "title": "列表方法", "code": "fruits = [\"apple\"]\nfruits.append(\"banana\")      # 添加元素\nfruits.insert(1, \"orange\")   # 在指定位置插入\nfruits.remove(\"apple\")        # 移除元素\nprint(fruits)                  # 输出: ['orange', 'banana']" }
                    ],
                    "syntax_notes": [
                        "列表使用方括号 [] 定义，元素之间用逗号分隔",
                        "列表索引从 0 开始",
                        "可以使用负索引从末尾访问元素（-1 表示最后一个元素）",
                        "列表是可变的，可以添加、删除、修改元素"
                    ],
                    "related_terms": ["List", "Index", "Array", "Dictionary"]
                },
                {
                    "id": "python_dict",
                    "name": "Dictionary 字典",
                    "description": "键值对集合，通过键快速访问值",
                    "search_keywords": ["字典", "dict", "键值对", "map", "哈希表"],
                    "technical_explanation": "字典（Dictionary）是 Python 中的一种键值对数据结构，类似于现实世界中的字典，通过键（key）来查找值（value）。",
                    "metaphor_explanation": "你可以把字典想象成一本通讯录。你知道一个人的名字（键），就可以找到对应的电话号码（值）。",
                    "examples": [
                        { "title": "创建字典", "code": "person = {\n    \"name\": \"Alice\",\n    \"age\": 25,\n    \"city\": \"Beijing\"\n}" },
                        { "title": "访问和修改", "code": "person = {\"name\": \"Alice\", \"age\": 25}\nprint(person[\"name\"])    # 输出: Alice\nperson[\"age\"] = 26\nprint(person)             # 输出: {'name': 'Alice', 'age': 26}" },
                        { "title": "遍历字典", "code": "person = {\"name\": \"Alice\", \"age\": 25}\nfor key, value in person.items():\n    print(f\"{key}: {value}\")" }
                    ],
                    "syntax_notes": [
                        "字典使用花括号 {} 定义，键值对用冒号分隔",
                        "键必须是不可变类型（字符串、数字、元组）",
                        "键必须是唯一的，如果重复会覆盖之前的值",
                        "可以使用 get() 方法安全地访问值"
                    ],
                    "related_terms": ["Dictionary", "Key", "List"]
                },
                {
                    "id": "python_import",
                    "name": "import 导入",
                    "description": "导入模块或模块中的特定功能",
                    "search_keywords": ["导入", "import", "模块", "module", "包", "package"],
                    "technical_explanation": "import 语句用于在 Python 中导入<a class=\"glossary-term\" data-term=\"Module\">模块</a>或模块中的特定对象。模块是一个包含相关代码的文件。",
                    "metaphor_explanation": "你可以把 import 想象成从图书馆借书。当你需要某个功能时，从标准库或第三方库中导入它。",
                    "examples": [
                        { "title": "导入整个模块", "code": "import math\nprint(math.sqrt(16))  # 输出: 4.0" },
                        { "title": "导入特定对象", "code": "from math import sqrt, pi\nprint(sqrt(16))  # 输出: 4.0\nprint(pi)        # 输出: 3.14159..." },
                        { "title": "使用别名", "code": "import numpy as np\nimport pandas as pd" }
                    ],
                    "syntax_notes": [
                        "import 语句通常放在文件的开头",
                        "可以使用 as 关键字给导入的对象指定别名",
                        "from ... import ... 可以只导入需要的部分"
                    ],
                    "related_terms": ["Module", "Function"]
                },
                {
                    "id": "python_try",
                    "name": "try-except 异常处理",
                    "description": "捕获和处理程序运行时的异常",
                    "search_keywords": ["异常", "错误", "try", "except", "错误处理", "异常处理"],
                    "technical_explanation": "try-except 语句用于在 Python 中捕获和处理<a class=\"glossary-term\" data-term=\"Exception\">异常</a>，使程序在遇到错误时能够优雅地处理而不是崩溃。",
                    "metaphor_explanation": "你可以把 try-except 想象成一个安全网。当你做有风险的事情（try）时，如果出了问题（exception），安全网会接住你，让你可以安全地处理问题。",
                    "examples": [
                        { "title": "基本异常处理", "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print(\"不能除以零!\")" },
                        { "title": "多异常处理", "code": "try:\n    value = int(input(\"请输入数字: \"))\n    result = 10 / value\nexcept ValueError:\n    print(\"请输入有效的数字\")\nexcept ZeroDivisionError:\n    print(\"不能输入零\")\nelse:\n    print(f\"结果: {result}\")\nfinally:\n    print(\"执行完毕\")" }
                    ],
                    "syntax_notes": [
                        "try 块包含可能抛出异常的代码",
                        "except 块定义如何处理特定类型的异常",
                        "else 块在没有异常时执行",
                        "finally 块无论是否有异常都会执行"
                    ],
                    "related_terms": ["Exception", "Error"]
                }
            ]
        },
        "cpp": {
            "name": "C++",
            "description": "C++ 是一种通用的编译型编程语言，支持面向对象编程和泛型编程。",
            "elements": [
                {
                    "id": "cpp_cout",
                    "name": "cout",
                    "description": "标准输出流对象，用于向控制台输出数据",
                    "search_keywords": ["打印", "输出", "显示", "cout", "输出到控制台", "ostream"],
                    "technical_explanation": "cout 是 C++ 标准库中定义的全局对象，与插入<a class=\"glossary-term\" data-term=\"Operator\">运算符</a><< 配合使用。",
                    "metaphor_explanation": "你可以把 cout 想象成一个打印机，而 << <a class=\"glossary-term\" data-term=\"Operator\">运算符</a>就像是把纸张送入打印机的动作。",
                    "examples": [
                        { "title": "基本输出", "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}" },
                        { "title": "输出多个值", "code": "int age = 25;\nstring name = \"Alice\";\ncout << \"Name: \" << name << \", Age: \" << age << endl;" },
                        { "title": "格式化输出", "code": "#include <iomanip>\ndouble pi = 3.14159265;\ncout << fixed << setprecision(2) << pi << endl;  // 输出: 3.14" }
                    ],
                    "syntax_notes": [
                        "使用 cout 需要包含头文件 <iostream>",
                        "cout 位于 std 命名空间中",
                        "使用 << 运算符连接多个输出项",
                        "endl 输出换行符并刷新缓冲区"
                    ],
                    "related_terms": ["Operator", "String", "Function"]
                },
                {
                    "id": "cpp_cin",
                    "name": "cin",
                    "description": "标准输入流对象，用于从控制台读取用户输入",
                    "search_keywords": ["输入", "获取", "读取", "cin", "用户输入", "istream"],
                    "technical_explanation": "cin 是 C++ 标准库中定义的全局对象，与提取<a class=\"glossary-term\" data-term=\"Operator\">运算符</a>>> 配合使用。",
                    "metaphor_explanation": "你可以把 cin 想象成一个扫描仪，而 >> <a class=\"glossary-term\" data-term=\"Operator\">运算符</a>就像是把纸张从扫描仪中拉出来的动作。",
                    "examples": [
                        { "title": "基本输入", "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    string name;\n    cout << \"请输入你的名字: \";\n    cin >> name;\n    cout << \"你好, \" << name << \"!\" << endl;\n    return 0;\n}" },
                        { "title": "读取整行", "code": "string fullName;\ncout << \"请输入全名: \";\ncin.ignore();  // 忽略之前的换行符\ngetline(cin, fullName);" }
                    ],
                    "syntax_notes": [
                        "使用 cin 需要包含头文件 <iostream>",
                        "提取<a class=\"glossary-term\" data-term=\"Operator\">运算符</a>>> 自动跳过空白字符",
                        "cin >> 读取到空白字符就停止",
                        "使用 getline() 读取整行（包括空格）"
                    ],
                    "related_terms": ["Operator", "Variable", "String"]
                },
                {
                    "id": "cpp_for",
                    "name": "for 循环",
                    "description": "迭代循环，用于重复执行代码块指定次数",
                    "search_keywords": ["循环", "遍历", "迭代", "for", "循环语句"],
                    "technical_explanation": "for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>是 C++ 中的一种控制结构，由初始化表达式、条件表达式和更新表达式组成。",
                    "metaphor_explanation": "你可以把 for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>想象成一个跑步机训练计划。",
                    "examples": [
                        { "title": "基本 for 循环", "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    for (int i = 0; i < 5; i++) {\n        cout << \"当前数字: \" << i << endl;\n    }\n    return 0;\n}" },
                        { "title": "范围-based for 循环", "code": "int numbers[] = {1, 2, 3, 4, 5};\nfor (int num : numbers) {\n    cout << num << \" \";\n}" }
                    ],
                    "syntax_notes": [
                        "for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>的三个部分都是可选的，但分号必须保留",
                        "可以使用 break 语句提前退出<a class=\"glossary-term\" data-term=\"Loop\">循环</a>",
                        "C++11 引入了范围-based for 循环"
                    ],
                    "related_terms": ["Loop", "Variable", "Array"]
                },
                {
                    "id": "cpp_if",
                    "name": "if 语句",
                    "description": "条件判断语句，根据条件执行不同的代码块",
                    "search_keywords": ["条件", "判断", "如果", "if", "条件判断", "分支"],
                    "technical_explanation": "if 语句是 C++ 中的条件控制结构，条件表达式的结果会被转换为布尔值。",
                    "metaphor_explanation": "你可以把 if 语句想象成一个岔路口的路标。",
                    "examples": [
                        { "title": "基本 if 语句", "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 18;\n    if (age >= 18) {\n        cout << \"你已经成年了\" << endl;\n    }\n    return 0;\n}" },
                        { "title": "if-else if-else", "code": "int score = 85;\nif (score >= 90) {\n    cout << \"优秀\" << endl;\n} else if (score >= 80) {\n    cout << \"良好\" << endl;\n} else {\n    cout << \"需要努力\" << endl;\n}" }
                    ],
                    "syntax_notes": [
                        "if 后面的条件表达式必须放在圆括号中",
                        "非零值转换为 true，零值转换为 false",
                        "可以使用 && 和 || 组合多个条件"
                    ],
                    "related_terms": ["Loop", "Operator", "Variable"]
                },
                {
                    "id": "cpp_class",
                    "name": "class 类定义",
                    "description": "定义一个新的类，封装数据和方法",
                    "search_keywords": ["类", "定义", "class", "面向对象", "OOP", "封装"],
                    "technical_explanation": "class 关键字用于在 C++ 中定义一个新的<a class=\"glossary-term\" data-term=\"Class\">类</a>。",
                    "metaphor_explanation": "你可以把 class 想象成一个建筑蓝图。",
                    "examples": [
                        { "title": "基本类定义", "code": "class Person {\nprivate:\n    string name;\n    int age;\npublic:\n    Person(string n, int a) : name(n), age(a) {}\n    void greet() {\n        cout << \"你好，我是\" << name << endl;\n    }\n};" },
                        { "title": "使用类", "code": "Person alice(\"Alice\", 25);\nalice.greet();" }
                    ],
                    "syntax_notes": [
                        "class 关键字后面跟<a class=\"glossary-term\" data-term=\"Class\">类</a>名",
                        "<a class=\"glossary-term\" data-term=\"Class\">类</a>体必须放在大括号中，末尾必须有分号",
                        "成员默认是 private 访问权限",
                        "构造函数与类同名，没有返回值"
                    ],
                    "related_terms": ["Class", "Method", "Function"]
                },
                {
                    "id": "cpp_while",
                    "name": "while 循环",
                    "description": "条件循环，当条件为真时重复执行代码块",
                    "search_keywords": ["循环", "while", "条件循环", "重复执行", "循环语句", "无限循环", "do while"],
                    "technical_explanation": "while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>是 C++ 中的一种控制结构，用于在条件表达式为 true 时重复执行一段代码块。C++ 还提供了 do-while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>。",
                    "metaphor_explanation": "你可以把 while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>想象成一个自助洗车场。",
                    "examples": [
                        { "title": "基本 while 循环", "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int count = 0;\n    while (count < 5) {\n        cout << \"当前计数: \" << count << endl;\n        count++;\n    }\n    return 0;\n}" },
                        { "title": "do-while 循环", "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int count = 0;\n    do {\n        cout << \"计数: \" << count << endl;\n        count++;\n    } while (count < 3);\n    return 0;\n}" }
                    ],
                    "syntax_notes": [
                        "while 关键字后面必须跟条件表达式（放在圆括号中）",
                        "条件表达式必须是可转换为 bool 类型的表达式",
                        "while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>先检查条件，再执行<a class=\"glossary-term\" data-term=\"Loop\">循环</a>体",
                        "do-while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>先执行<a class=\"glossary-term\" data-term=\"Loop\">循环</a>体，再检查条件",
                        "如果条件始终为 true，会形成无限<a class=\"glossary-term\" data-term=\"Loop\">循环</a>"
                    ],
                    "related_terms": ["Loop", "Variable", "Operator"]
                },
                {
                    "id": "cpp_vector",
                    "name": "vector 向量",
                    "description": "动态数组，可以自动调整大小",
                    "search_keywords": ["向量", "vector", "动态数组", "STL", "容器"],
                    "technical_explanation": "vector 是 C++ 标准模板库（STL）中的一个容器类，提供了动态<a class=\"glossary-term\" data-term=\"Array\">数组</a>的功能。",
                    "metaphor_explanation": "你可以把 vector 想象成一个可伸缩的货架。你可以根据需要添加或移除物品，货架会自动调整大小。",
                    "examples": [
                        { "title": "基本使用", "code": "#include <vector>\n#include <iostream>\nusing namespace std;\n\nvector<int> numbers = {1, 2, 3, 4, 5};\nnumbers.push_back(6);  // 添加元素\nnumbers.pop_back();    // 移除最后一个元素\ncout << numbers.size();  // 输出: 5" },
                        { "title": "遍历 vector", "code": "vector<string> fruits = {\"apple\", \"banana\", \"cherry\"};\nfor (const string& fruit : fruits) {\n    cout << fruit << \" \";\n}" }
                    ],
                    "syntax_notes": [
                        "使用 vector 需要包含头文件 <vector>",
                        "vector 位于 std 命名空间中",
                        "可以使用 push_back() 在末尾添加元素",
                        "可以使用 [] 或 at() 访问元素"
                    ],
                    "related_terms": ["Array", "List"]
                },
                {
                    "id": "cpp_function",
                    "name": "function 函数",
                    "description": "定义可重用的代码块",
                    "search_keywords": ["函数", "function", "方法", "定义函数"],
                    "technical_explanation": "<a class=\"glossary-term\" data-term=\"Function\">函数</a>是 C++ 中组织代码的基本单元，可以接受参数并返回值。",
                    "metaphor_explanation": "你可以把函数想象成一个加工厂。原材料（参数）进去，经过加工处理，产出成品（返回值）。",
                    "examples": [
                        { "title": "基本函数", "code": "int add(int a, int b) {\n    return a + b;\n}\n\nint result = add(3, 5);  // result = 8" },
                        { "title": "函数重载", "code": "int max(int a, int b) {\n    return (a > b) ? a : b;\n}\n\ndouble max(double a, double b) {\n    return (a > b) ? a : b;\n}" }
                    ],
                    "syntax_notes": [
                        "函数声明包括返回类型、函数名和参数列表",
                        "函数必须在使用前声明或定义",
                        "C++ 支持函数重载（同名但参数不同）",
                        "使用 return 语句返回值"
                    ],
                    "related_terms": ["Function", "Parameter", "Return Value", "Method"]
                },
                {
                    "id": "cpp_pointer",
                    "name": "pointer 指针",
                    "description": "存储内存地址的变量",
                    "search_keywords": ["指针", "pointer", "内存", "地址", "引用"],
                    "technical_explanation": "指针是一个存储另一个<a class=\"glossary-term\" data-term=\"Variable\">变量</a>内存地址的变量。通过指针可以间接访问和修改其他变量的值。",
                    "metaphor_explanation": "你可以把指针想象成一个房屋地址。地址本身不是房子，但通过地址你可以找到房子。",
                    "examples": [
                        { "title": "基本指针", "code": "int x = 42;\nint* ptr = &x;  // ptr 存储 x 的地址\ncout << *ptr;   // 输出: 42 (通过指针访问值)\n*ptr = 100;     // 通过指针修改 x 的值\ncout << x;      // 输出: 100" },
                        { "title": "空指针", "code": "int* ptr = nullptr;  // C++11 空指针\nif (ptr != nullptr) {\n    cout << *ptr;\n}" }
                    ],
                    "syntax_notes": [
                        "使用 * 声明指针类型",
                        "使用 & 获取变量的地址",
                        "使用 * 解引用指针（访问指向的值）",
                        "始终检查指针是否为空再使用"
                    ],
                    "related_terms": ["Variable", "Array"]
                },
                {
                    "id": "cpp_include",
                    "name": "#include 头文件",
                    "description": "包含头文件，导入声明",
                    "search_keywords": ["include", "头文件", "header", "导入", "声明"],
                    "technical_explanation": "#include 是 C++ 的预处理指令，用于在编译时将指定头文件的内容包含到当前文件中。",
                    "metaphor_explanation": "你可以把 #include 想象成复制粘贴。编译器在编译时会把头文件的内容粘贴到 #include 的位置。",
                    "examples": [
                        { "title": "包含标准库头文件", "code": "#include <iostream>\n#include <vector>\n#include <string>" },
                        { "title": "包含自定义头文件", "code": "#include \"myheader.h\"" }
                    ],
                    "syntax_notes": [
                        "使用 <> 包含标准库头文件",
                        "使用 \"\" 包含自定义头文件",
                        "头文件通常包含函数声明、类定义等",
                        "使用头文件保护防止重复包含"
                    ],
                    "related_terms": ["Module", "Function", "Class"]
                }
            ]
        },
        "java": {
            "name": "Java",
            "description": "Java 是一种面向对象的编程语言，以其\"一次编写，到处运行\"的特性著称。",
            "elements": [
                {
                    "id": "java_system_out_println",
                    "name": "System.out.println()",
                    "description": "标准输出方法，用于向控制台打印一行文本",
                    "search_keywords": ["打印", "输出", "显示", "println", "print", "System.out"],
                    "technical_explanation": "System.out.println() 是 Java 中最常用的输出<a class=\"glossary-term\" data-term=\"Method\">方法</a>。",
                    "metaphor_explanation": "你可以把 System.out.println() 想象成一个带自动换行的打字机。",
                    "examples": [
                        { "title": "基本输出", "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}" },
                        { "title": "输出变量", "code": "String name = \"Alice\";\nint age = 25;\nSystem.out.println(\"Name: \" + name + \", Age: \" + age);" },
                        { "title": "格式化输出", "code": "double price = 19.99;\nSystem.out.printf(\"价格: $%.2f%n\", price);" }
                    ],
                    "syntax_notes": [
                        "System.out.println() 输出内容后会自动换行",
                        "System.out.print() 输出内容后不会换行",
                        "System.out.printf() 支持格式化输出"
                    ],
                    "related_terms": ["Method", "Class", "String", "Operator"]
                },
                {
                    "id": "java_scanner",
                    "name": "Scanner",
                    "description": "输入工具类，用于从各种输入源读取数据",
                    "search_keywords": ["输入", "获取", "读取", "Scanner", "用户输入", "键盘输入"],
                    "technical_explanation": "Scanner 是 java.util 包中的一个<a class=\"glossary-term\" data-term=\"Class\">类</a>，用于从各种输入源读取数据。",
                    "metaphor_explanation": "你可以把 Scanner 想象成一个多功能的数据采集器。",
                    "examples": [
                        { "title": "基本输入", "code": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        System.out.print(\"请输入你的名字: \");\n        String name = scanner.nextLine();\n        System.out.println(\"你好, \" + name + \"!\");\n        scanner.close();\n    }\n}" },
                        { "title": "读取不同类型", "code": "Scanner scanner = new Scanner(System.in);\nSystem.out.print(\"请输入整数: \");\nint num = scanner.nextInt();\nSystem.out.print(\"请输入小数: \");\ndouble d = scanner.nextDouble();" }
                    ],
                    "syntax_notes": [
                        "使用 Scanner 需要导入 java.util.Scanner 包",
                        "创建 Scanner 对象时需要传入输入源",
                        "使用完 Scanner 后应该调用 close() 方法",
                        "nextLine() 读取整行，next() 读取到空白字符"
                    ],
                    "related_terms": ["Class", "Method", "Variable", "String"]
                },
                {
                    "id": "java_for",
                    "name": "for 循环",
                    "description": "迭代循环，用于重复执行代码块指定次数",
                    "search_keywords": ["循环", "遍历", "迭代", "for", "循环语句", "增强for"],
                    "technical_explanation": "for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>是 Java 中的一种控制结构，有传统 for 循环和增强型 for 循环两种形式。",
                    "metaphor_explanation": "你可以把 for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>想象成一个打卡上班的流程。",
                    "examples": [
                        { "title": "基本 for 循环", "code": "public class Main {\n    public static void main(String[] args) {\n        for (int i = 0; i < 5; i++) {\n            System.out.println(\"当前数字: \" + i);\n        }\n    }\n}" },
                        { "title": "增强型 for 循环", "code": "String[] fruits = {\"apple\", \"banana\", \"cherry\"};\nfor (String fruit : fruits) {\n    System.out.println(fruit);\n}" }
                    ],
                    "syntax_notes": [
                        "for <a class=\"glossary-term\" data-term=\"Loop\">循环</a>的三个部分都是可选的，但分号必须保留",
                        "增强型 for 循环用于遍历<a class=\"glossary-term\" data-term=\"Array\">数组</a>和集合",
                        "增强型 for 循环从 Java 5 开始支持"
                    ],
                    "related_terms": ["Loop", "Variable", "Array"]
                },
                {
                    "id": "java_if",
                    "name": "if 语句",
                    "description": "条件判断语句，根据条件执行不同的代码块",
                    "search_keywords": ["条件", "判断", "如果", "if", "条件判断", "分支"],
                    "technical_explanation": "if 语句是 Java 中的条件控制结构。",
                    "metaphor_explanation": "你可以把 if 语句想象成一个岔路口的路标。",
                    "examples": [
                        { "title": "基本 if 语句", "code": "public class Main {\n    public static void main(String[] args) {\n        int age = 18;\n        if (age >= 18) {\n            System.out.println(\"你已经成年了\");\n        }\n    }\n}" },
                        { "title": "三元运算符", "code": "int age = 18;\nString status = (age >= 18) ? \"成年\" : \"未成年\";\nSystem.out.println(status);" }
                    ],
                    "syntax_notes": [
                        "if 后面的条件表达式必须放在圆括号中",
                        "条件表达式必须是 boolean 类型",
                        "Java 也支持三元运算符 ?:"
                    ],
                    "related_terms": ["Loop", "Operator", "Variable"]
                },
                {
                    "id": "java_class",
                    "name": "class 类定义",
                    "description": "定义一个新的类，封装数据和方法",
                    "search_keywords": ["类", "定义", "class", "面向对象", "OOP", "封装"],
                    "technical_explanation": "class 关键字用于在 Java 中定义一个新的<a class=\"glossary-term\" data-term=\"Class\">类</a>。",
                    "metaphor_explanation": "你可以把 class 想象成一个建筑蓝图。",
                    "examples": [
                        { "title": "基本类定义", "code": "public class Person {\n    private String name;\n    private int age;\n    \n    public Person(String name, int age) {\n        this.name = name;\n        this.age = age;\n    }\n    \n    public void greet() {\n        System.out.println(\"你好，我是\" + name);\n    }\n}" },
                        { "title": "使用类", "code": "Person alice = new Person(\"Alice\", 25);\nalice.greet();" }
                    ],
                    "syntax_notes": [
                        "class 关键字后面跟<a class=\"glossary-term\" data-term=\"Class\">类</a>名",
                        "Java 中的所有代码都必须在<a class=\"glossary-term\" data-term=\"Class\">类</a>中定义",
                        "类名通常采用大驼峰命名法",
                        "一个 Java 文件中只能有一个 public 类"
                    ],
                    "related_terms": ["Class", "Method", "Function"]
                },
                {
                    "id": "java_while",
                    "name": "while 循环",
                    "description": "条件循环，当条件为真时重复执行代码块",
                    "search_keywords": ["循环", "while", "条件循环", "重复执行", "循环语句", "无限循环", "do while"],
                    "technical_explanation": "while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>是 Java 中的一种控制结构，用于在条件表达式为 true 时重复执行一段代码块。Java 还提供了 do-while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>。",
                    "metaphor_explanation": "你可以把 while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>想象成一个健身房的跑步机。",
                    "examples": [
                        { "title": "基本 while 循环", "code": "public class Main {\n    public static void main(String[] args) {\n        int count = 0;\n        while (count < 5) {\n            System.out.println(\"当前计数: \" + count);\n            count++;\n        }\n    }\n}" },
                        { "title": "do-while 循环", "code": "public class Main {\n    public static void main(String[] args) {\n        int count = 0;\n        do {\n            System.out.println(\"计数: \" + count);\n            count++;\n        } while (count < 3);\n    }\n}" }
                    ],
                    "syntax_notes": [
                        "while 关键字后面必须跟条件表达式（放在圆括号中）",
                        "条件表达式必须是 boolean 类型",
                        "while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>先检查条件，再执行<a class=\"glossary-term\" data-term=\"Loop\">循环</a>体",
                        "do-while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>先执行<a class=\"glossary-term\" data-term=\"Loop\">循环</a>体，再检查条件",
                        "如果条件始终为 true，会形成无限<a class=\"glossary-term\" data-term=\"Loop\">循环</a>",
                        "do-while <a class=\"glossary-term\" data-term=\"Loop\">循环</a>的条件表达式后面必须有分号"
                    ],
                    "related_terms": ["Loop", "Variable", "Operator"]
                },
                {
                    "id": "java_arraylist",
                    "name": "ArrayList",
                    "description": "动态数组，大小可以自动调整",
                    "search_keywords": ["ArrayList", "列表", "动态数组", "集合", "List"],
                    "technical_explanation": "ArrayList 是 Java 集合框架中的一个类，实现了动态<a class=\"glossary-term\" data-term=\"Array\">数组</a>的功能。",
                    "metaphor_explanation": "你可以把 ArrayList 想象成一个可伸缩的书架。你可以根据需要添加或移除书籍，书架会自动调整大小。",
                    "examples": [
                        { "title": "基本使用", "code": "import java.util.ArrayList;\n\nArrayList<String> fruits = new ArrayList<>();\nfruits.add(\"apple\");\nfruits.add(\"banana\");\nfruits.add(\"cherry\");\n\nSystem.out.println(fruits.get(0));  // 输出: apple\nSystem.out.println(fruits.size());  // 输出: 3" },
                        { "title": "遍历 ArrayList", "code": "for (String fruit : fruits) {\n    System.out.println(fruit);\n}" }
                    ],
                    "syntax_notes": [
                        "使用 ArrayList 需要导入 java.util.ArrayList",
                        "ArrayList 只能存储对象类型（使用包装类存储基本类型）",
                        "使用 add() 添加元素，get() 访问元素",
                        "可以使用泛型指定元素类型"
                    ],
                    "related_terms": ["Array", "List", "Class"]
                },
                {
                    "id": "java_method",
                    "name": "method 方法",
                    "description": "定义类的行为，封装可重用的代码",
                    "search_keywords": ["方法", "method", "函数", "定义方法"],
                    "technical_explanation": "<a class=\"glossary-term\" data-term=\"Method\">方法</a>是 Java 中类的行为单元，可以接受参数、执行操作并返回值。",
                    "metaphor_explanation": "你可以把方法想象成一个自动售货机。你投入硬币（参数），选择商品，机器给你商品（返回值）。",
                    "examples": [
                        { "title": "基本方法", "code": "public class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n    \n    public static void main(String[] args) {\n        Calculator calc = new Calculator();\n        int result = calc.add(3, 5);\n        System.out.println(result);  // 输出: 8\n    }\n}" },
                        { "title": "静态方法", "code": "public class MathUtils {\n    public static int square(int x) {\n        return x * x;\n    }\n}\n\n// 调用静态方法不需要创建对象\nint result = MathUtils.square(5);" }
                    ],
                    "syntax_notes": [
                        "方法声明包括修饰符、返回类型、方法名和参数列表",
                        "静态方法使用 static 关键字，属于类而不是对象",
                        "void 表示方法没有返回值",
                        "方法名通常采用小驼峰命名法"
                    ],
                    "related_terms": ["Method", "Function", "Parameter", "Return Value"]
                },
                {
                    "id": "java_string",
                    "name": "String 字符串",
                    "description": "表示文本数据的类",
                    "search_keywords": ["字符串", "String", "文本", "字符"],
                    "technical_explanation": "<a class=\"glossary-term\" data-term=\"String\">String</a> 是 Java 中表示字符串的类，字符串是不可变的（immutable）。",
                    "metaphor_explanation": "你可以把 String 想象成刻在石头上的文字。一旦刻好，就不能改变了；如果要修改，需要刻一块新的石头。",
                    "examples": [
                        { "title": "字符串操作", "code": "String greeting = \"Hello, World!\";\nSystem.out.println(greeting.length());      // 输出: 13\nSystem.out.println(greeting.toUpperCase()); // 输出: HELLO, WORLD!\nSystem.out.println(greeting.substring(7));  // 输出: World!" },
                        { "title": "字符串连接", "code": "String firstName = \"Alice\";\nString lastName = \"Smith\";\nString fullName = firstName + \" \" + lastName;\nSystem.out.println(fullName);  // 输出: Alice Smith" }
                    ],
                    "syntax_notes": [
                        "String 对象是不可变的，任何修改都会创建新对象",
                        "可以使用 + 运算符连接字符串",
                        "equals() 方法比较字符串内容，== 比较引用",
                        "字符串字面量存储在字符串池中"
                    ],
                    "related_terms": ["String", "Class", "Method"]
                },
                {
                    "id": "java_import",
                    "name": "import 导入",
                    "description": "导入其他包中的类",
                    "search_keywords": ["导入", "import", "包", "package", "类"],
                    "technical_explanation": "import 语句用于在 Java 中导入其他包中的<a class=\"glossary-term\" data-term=\"Class\">类</a>，使代码更简洁。",
                    "metaphor_explanation": "你可以把 import 想象成提前通知编译器你要使用哪些工具。这样你就不用每次都写完整的工具名称。",
                    "examples": [
                        { "title": "导入单个类", "code": "import java.util.Scanner;\nimport java.util.ArrayList;" },
                        { "title": "导入整个包", "code": "import java.util.*;" },
                        { "title": "静态导入", "code": "import static java.lang.Math.PI;\nimport static java.lang.Math.sqrt;\n\ndouble area = PI * sqrt(25);" }
                    ],
                    "syntax_notes": [
                        "import 语句放在 package 语句之后，类定义之前",
                        "使用 * 可以导入包中的所有类",
                        "静态导入可以直接使用静态成员",
                        "java.lang 包中的类会自动导入"
                    ],
                    "related_terms": ["Module", "Class", "Method"]
                }
            ]
        }
    }
}


async def fetch_data_from_url(url: str) -> dict | None:
    if not url:
        return None
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                print(f"Successfully fetched data from {url}")
                return data
    except Exception as e:
        print(f"Failed to fetch data from {url}: {e}")
    
    return None


def merge_data(base_data: dict, new_data: dict) -> dict:
    result = {
        "glossary": {},
        "languages": {}
    }
    
    result["glossary"].update(base_data.get("glossary", {}))
    result["glossary"].update(new_data.get("glossary", {}))
    
    result["languages"].update(base_data.get("languages", {}))
    for lang_key, lang_data in new_data.get("languages", {}).items():
        if lang_key in result["languages"]:
            existing_elements = {e["id"]: e for e in result["languages"][lang_key].get("elements", [])}
            for elem in lang_data.get("elements", []):
                existing_elements[elem["id"]] = elem
            result["languages"][lang_key]["elements"] = list(existing_elements.values())
        else:
            result["languages"][lang_key] = lang_data
    
    return result


async def get_combined_data() -> dict:
    data = DEFAULT_DATA
    
    if settings.DATA_SOURCE_URL:
        remote_data = await fetch_data_from_url(settings.DATA_SOURCE_URL)
        if remote_data:
            data = merge_data(data, remote_data)
    
    return data
