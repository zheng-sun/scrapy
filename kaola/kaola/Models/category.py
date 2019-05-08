


class categoryModel():

    # 添加数据
    def insertCategory(self, item):
        sql = """replace into categorys(categoryId, parentId, categoryLevel, categoryName, categoryStatus) values (%s, %s, %s, %s, %s)"""
        self.cursor.execute(sql, (
        item['categoryId'], item['parentId'], item['categoryLevel'], item['categoryName'], item['categoryStatus']))
        self.connect.commit()