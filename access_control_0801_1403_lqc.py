# 代码生成时间: 2025-08-01 14:03:57
import numpy as np

# 定义一个类来处理权限控制
class AccessControl:
    def __init__(self):
        # 用户权限信息，可以根据实际需求从数据库或其他存储中加载
        self.user_permissions = {
            'alice': {'read': True, 'write': False, 'delete': False},
            'bob': {'read': False, 'write': True, 'delete': False},
            # 更多用户可以在这里添加
        }

    def check_permission(self, username, action):
        '''
        检查用户是否有执行某操作的权限
        :param username: 用户名
        :param action: 要执行的操作（'read', 'write', 'delete'）
        :return: 如果有权限返回True，否则返回False
        '''
        if username in self.user_permissions:
            return self.user_permissions[username].get(action, False)
        else:
            # 如果用户不存在，返回没有权限
            return False

    def grant_permission(self, username, action):
        '''
        赋予用户权限
        :param username: 用户名
        :param action: 要赋予的权限（'read', 'write', 'delete'）
        '''
        if username in self.user_permissions:
            self.user_permissions[username][action] = True
        else:
            # 如果用户不存在，则创建新的用户权限条目
            self.user_permissions[username] = {action: True}

    def revoke_permission(self, username, action):
        '''
        撤销用户权限
        :param username: 用户名
        :param action: 要撤销的权限（'read', 'write', 'delete'）
        '''
        if username in self.user_permissions and action in self.user_permissions[username]:
            self.user_permissions[username][action] = False
        else:
            # 如果用户不存在或没有此权限，则不作任何操作
            pass

# 示例用法
if __name__ == '__main__':
    access_control = AccessControl()
    
    # 检查用户权限
    print("Does Alice have read permission?", access_control.check_permission('alice', 'read'))
    print("Does Bob have write permission?", access_control.check_permission('bob', 'write'))
    
    # 赋予和撤销权限
    access_control.grant_permission('alice', 'write')
    print("Does Alice have write permission after granting?", access_control.check_permission('alice', 'write'))
    
    access_control.revoke_permission('alice', 'write')
    print("Does Alice have write permission after revoking?", access_control.check_permission('alice', 'write'))
