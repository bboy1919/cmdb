# CMDB

**参考龙果学院的cmdb，该源码基于python2，so重写后端代码**

## 目前实现功能：

1、用户及权限管理


> 基于pycasbin实现资源的访问控制

```python
@web.before_request
def role_access_control():
	#每次访问都对访问列表重加载，以防规则改变后不起作用
    enforcer.load_policy()
    user = session.get("username", None)
    if user is None:
        user = 'anonymous'
    path = request.path
    method = request.method
    if enforcer.enforce(user, path, method):
        return None
    else:
        description = "没有权限访问改功能，请联系管理员"
        return Forbidden(msg=description)
```
文件路径`/app/lib/casbin_api.py`
```python
	#规则列表的修改与存储
   file_adapter = File_Adapter(os.path.join(base_dir, "conf", "authz_policy.csv"))
   file_adapter.change_policy("g", update_group_policy)
```

2、资产管理


> 实现资产的增删改查，主机与zabbix的同步功能

## 目前只有这么多了,后续功能开发中、、、、