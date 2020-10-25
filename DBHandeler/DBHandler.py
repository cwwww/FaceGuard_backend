import records

# 获取所有名字，返回一个列表
def getAllName(db):
    rows = db.query('SELECT Name FROM faceguard_user')
    names = []
    for item in rows.as_dict():
        names.append(item['Name'])
    return names

# 获取所有图片地址，返回一个列表
def getAllImage(db):
    rows = db.query('SELECT Image FROM faceguard_user')
    images = []
    for item in rows.as_dict():
        images.append(item['Image'])
    return images

# 输入用户名，查询对应的图片地址，返回该用户的图片地址
def nameToImage(db,name):
    rows = db.query("SELECT Image FROM faceguard_user WHERE NAME = '%s'"% (name))

    image = rows.as_dict()[0]['Image']
    return image


if __name__ == "__main__":
    # 数据库连接，根据自己数据库设置修改
    db = records.Database('mysql://root:N535348@localhost/proj1')
    # db = records.Database('mysql://数据库用户名:密码@localhost/数据库名')

    # 查询所有名字
    names = getAllName(db)
    print(names)
    # 查询所有图片
    images = getAllImage(db)
    print(images)
    # 查询名字对应的图片， 以caowen为例
    image = nameToImage(db,'caowen')
    print(image)
