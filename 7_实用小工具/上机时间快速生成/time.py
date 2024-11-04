import random
import csv

from datetime import datetime, timedelta
from tracemalloc import start

def validate_date(date_string):
    ''' 验证输入的日期是否有效 '''
    try:
        # 尝试将字符串解析为日期对象
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calc_date(start_date, offset):
    # 将字符串转换为日期对象
    date_format = "%Y-%m-%d"
    start_date_obj = datetime.strptime(start_date, date_format)
    
    # 打印 n 天后的日期
    current_date = start_date_obj + timedelta(days=offset)
    # print(type(current_date.strftime(date_format)))
    return current_date.strftime(date_format)


def random_hour_minute_second(start_date, days, start_hour, end_hour):
    '''
    随机生成指定天数的时间段，时间段的起始和终止时间在给定的小时范围内。

    参数:
    days (int): 要生成的时间段数量，即天数。
    start_hour (int): 时间段起始小时的最小值（包含）。
    end_hour (int): 时间段起始小时的最大值（包含）。

    返回:
    list: 包含每个时间段的起始和终止时间的列表，每个时间段用一个包含两个字符串的列表表示。
          例如：[['HH:MM:SS', 'HH:MM:SS'], ...]
    
    过程:
    1. 初始化起始和结束小时、分钟、秒的范围。
    2. 对于每一天，生成一个随机的起始时间（小时、分钟、秒）。
    3. 生成一个随机的持续时间（1到3小时）。
    4. 提示用户确认生成的时间段，如果用户选择需要重新生成，则重新生成。
    5. 将确认后的时间段添加到结果列表中。
    '''
    n = days
    
    start_minute = 0
    end_minute = 59
    
    start_second = 0
    end_second = 59
    
    l = []
    
    for i in range(n):
        flag = 'Y'
        while flag != 'N':
            rand_hour = random.randint(a=start_hour, b=end_hour)
            rand_minute1 = random.randint(a=start_minute, b=end_minute)
            rand_second1 = random.randint(a=start_second, b=end_second)
            rand_minute2 = random.randint(a=start_minute, b=end_minute)
            rand_second2 = random.randint(a=start_second, b=end_second)
            rand_span = random.randint(a=1, b=3)
            time1 = (str(rand_hour)+':'+str(rand_minute1)+':'+str(rand_second1))
            while rand_hour+rand_span >= 24:
                rand_span = random.randint(a=1, b=3)
            time2 = (str(rand_hour+rand_span)+':'+str(rand_minute2)+':'+str(rand_second2))
            current_date = calc_date(start_date=start_date, offset= i)
            flag = input(f'第{i+1}个, 起始时间为{current_date+" "+time1}, 终止时间为{current_date+" "+time2}, 是否需要重新生成(y/n)？').upper()
        
        
        l2 = [current_date+" "+time1, current_date+" "+time2]
        l.append(l2)
    
    return l

def input_csv(l, file_path_name='./time.csv'):
    with open(file=file_path_name, mode='w', newline='') as f:
        spamwriter = csv.writer(f)
        l.append(['若文件中显示“######”, 这并不是乱码, 而是字符太长导致的, 请双击单元格即可查看其中信息.'])
        spamwriter.writerows(l)
        

if __name__ == '__main__':
    print("这是一个生成上机时间的程序, 用于快速生成上机时间, 每次上机时间约为1~3小时, 希望能为大家节省时间, Nekasu祝您生活愉快~万事顺意~")
    start_date = input("请输入起始日期 (YYYY-MM-DD): ")
    while not validate_date(start_date):
        print("输入的日期无效，请输入正确的日期格式（YYYY-MM-DD）, 或检查是否输入了越界的日期(如1919-81-021)。")
        start_date = input("请输入起始日期 (YYYY-MM-DD): ")        
    
    
    flag= True
    while flag:
        n = input("请输入需要生成的天数: ")
        try:
            n = int(n)
            flag = False
        except ValueError:
            print("输入有误, 请检查是否将天数错误的输入为日期？")
            
            
    flag= True
    while flag:
        try:
            start_hour = int(input("请输入开始工作的时间(如8:45开始工作则输入8, 仅输入代表小时的数即可): "))
            if 0<=start_hour and start_hour<24:
                flag = False
            else:
                print("输入有误, 请检查是否输入的是[0,24)的数.")
        except:
            print("输入有误, 请检查是否输入的是[0,24)的数.")

            
    flag= True
    while flag:
        try:
            end_hour = int(input("请输入结束工作的时间(如22:21结束工作则输入22, 仅输入代表小时的数即可): "))
            if start_hour<end_hour and end_hour<24:
                flag = False
            else:
                print(f"输入有误, 请检查是否输入的是({start_hour},23]的数, 或结束时间是否小于或等于开始时间.")
        except:
            print(f"输入有误, 请检查是否输入的是({start_hour},23]的数.")
        


    l = random_hour_minute_second(start_date=start_date, days=n, start_hour=start_hour, end_hour=end_hour)
    input_csv(l=l)
    print('''\n 数据处理完成, 上述数据已保存在同路径下的time.csv文件中, 可以直接复制到Excel中.\n 若打开文件后显示“######”, 这并不是乱码, 而是字符太长导致的, 请双击单元格即可查看其中信息.\n 在复制到Excel后, 请使用格式刷统一格式.
          ''')