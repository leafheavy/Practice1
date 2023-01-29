#oop三大特征：
* 封装
* 继承
* 多态

#析构方法
* 程序脚本执行完毕会自动调用
* 用于手动销毁对象，释放资源

#封装
将内容封装，方便重复使用
* 封装到某个地方
* 在另一个地方进行调用

#继承
子类可以继承父类的属性和行为
##单继承
class 类名（父类）：
    $$...$$

##多继承
class 类名（父类1，父类2，...,父类n）：
    $$...$$

**父类出现重名**
* 遵从C3算法（暂时按**广度优先搜索策略**理解）查找，可以用魔术方法mro查看遍历的顺序
* 重写会**覆盖**父类里面的属性和行为

#属性
* 类属性：**类对象**所拥有的属性
    * 通过类名.属性修改、访问
* 实例属性：**实例对象**所拥有的属性
    * 通过实例对象.属性修改、访问

#方法
* 类方法
    * 在方法前面用$@classmethod$进行修饰即可
    * 方法默认参数为类对象（cls），也就是**需要通过类对象来访问类方法**

* 静态方法
    * 在方法前面用$@staticmethod$进行修饰即可
    * **可以不需要**任何参数
    * 和类、实例对象没有交互，因此和类方法比较**节省数据资源**

* 实例方法
    * 方法默认参数为对象（self），**该对象可为类对象也可为实例对象**

##多态
* 同一种行为，对于不同的子类有不同的行为表现
    [例:有一条指令让人和鸭子说话，人说人话，鸭子说鸭子话]

* 实现前提
    * 多态发生在父类和子类之间
    * 子类重写父类的方法

* 好处：只要你是派生类（**不需要继承于同一个父类**）且有要的某个方法（如每个派生类里面都有say_who方法），我就会把它执行出来（尽管每个类中的say_who的内容各不同）