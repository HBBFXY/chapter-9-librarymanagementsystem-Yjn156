class Book:
    """书籍类，包含书名、作者、ISBN、可借状态等属性"""
    def __init__(self, book_name, author, isbn):
        self.book_name = book_name  # 书名
        self.author = author        # 作者
        self.isbn = isbn            # ISBN编号
        self.is_available = True    # 可借状态，默认可借

    def __str__(self):
        """返回书籍的字符串描述"""
        status = "可借" if self.is_available else "已借出"
        return f"书名：{self.book_name}，作者：{self.author}，ISBN：{self.isbn}，状态：{status}"


class User:
    """用户类，包含姓名、借书卡号、已借书籍列表等属性"""
    def __init__(self, name, card_id):
        self.name = name            # 姓名
        self.card_id = card_id      # 借书卡号
        self.borrowed_books = []    # 已借书籍列表

    def borrow_book(self, book):
        """借书功能：检查书籍可借状态，成功则加入已借列表并修改书籍状态"""
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name}成功借阅《{book.book_name}》")
        else:
            print(f"抱歉，《{book.book_name}》已被借出，无法借阅")

    def return_book(self, book):
        """还书功能：检查是否为已借书籍，成功则移除并恢复书籍可借状态"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name}成功归还《{book.book_name}》")
        else:
            print(f"{self.name}未借阅《{book.book_name}》，无法归还")

    def check_borrowed(self):
        """查看用户已借书籍"""
        if self.borrowed_books:
            print(f"\n{self.name}的已借书籍：")
            for b in self.borrowed_books:
                print(f"- {b.book_name}（ISBN：{b.isbn}）")
        else:
            print(f"\n{self.name}暂无已借书籍")


class LibrarySystem:
    """图书馆系统类，管理书籍和用户，提供书籍状态检查功能"""
    def __init__(self):
        self.books = []    # 图书馆书籍列表
        self.users = []    # 图书馆用户列表

    def add_book(self, book):
        """添加书籍到图书馆"""
        self.books.append(book)

    def add_user(self, user):
        """添加用户到图书馆"""
        self.users.append(user)

    def check_book_status(self, isbn):
        """根据ISBN检查书籍可借状态"""
        for book in self.books:
            if book.isbn == isbn:
                print(f"\n书籍查询结果：{book}")
                return book
        print(f"\n未找到ISBN为{isbn}的书籍")
        return None


# 系统测试示例
if __name__ == "__main__":
    # 初始化图书馆系统
    lib = LibrarySystem()

    # 添加书籍
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787115546920")
    lib.add_book(book1)
    lib.add_book(book2)

    # 添加用户
    user1 = User("张三", "U001")
    user2 = User("李四", "U002")
    lib.add_user(user1)
    lib.add_user(user2)

    # 检查书籍状态
    lib.check_book_status("9787115428028")

    # 借书操作
    user1.borrow_book(book1)
    user2.borrow_book(book1)  # 尝试借阅已借出的书

    # 查看用户已借书籍
    user1.check_borrowed()

    # 还书操作
    user1.return_book(book1)
    lib.check_book_status("9787115428028")  # 再次检查书籍状态
