from CStudent import CStudent

def main():
    student1 = CStudent('S109102345', '張三', 'IECS', 'zs100232@gmail.com', '2000-02-02')   #對應上面的參數，self不用
    print("name is{}.".format(student1.name))
    student2 = CStudent('S109104533', '李四', 'IECS', 'ktr002222@gmail.com', '2004-03-22')
    print("name is{}.".format(student2.name))
    student3 = CStudent('S109123346', '王五', 'EE', 'zs1543232@gmail.com', '1999-04-22')
    print("name is{}.".format(student3.name))
    student4 = CStudent('S109102355', '趙雲', 'CE', 'zkkse0252@gmail.com', '2001-05-10')
    print("name is{}.".format(student4.name))
    student5 = CStudent('S109102785', '李白', 'AI', 'zsf23s3d@gmail.com', '2002-06-04')
    print("name is{}.".format(student5.name))