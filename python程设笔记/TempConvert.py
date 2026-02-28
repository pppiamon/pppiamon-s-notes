
#TempConvert.py               # 注释：代码文件名
TempStr = input("请输入带有符号的温度值: ")  # 获取用户输入的温度字符串
if TempStr[-1] in ['F', 'f']:  # 判断输入是否为华氏度（F/f结尾）
    C = (eval(TempStr[0:-1]) - 32)/1.8  # 提取数值部分，按公式转成摄氏度
    print("转换后的温度是{:.2f}C".format(C))  # 格式化输出结果
elif TempStr[-1] in ['C', 'c']:  # 判断输入是否为摄氏度（C/c结尾）
    F = 1.8*eval(TempStr[0:-1]) + 32  # 提取数值部分，按公式转成华氏度
    print("转换后的温度是{:.2f}F".format(F))  # 格式化输出结果
else:
    print("输入格式错误")  # 处理无效输入的情况