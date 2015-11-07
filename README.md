== README

######大家先装好tornado，可以使用pip安装  
######再装好sqlalchemy,也可以使用pip安装
######数据库在阿里云上，大家可以不用管
######前台的html文件放在templates下，
######js以及cs放在static的对应目录下
######如何调用看教程http://demo.pythoner.com/itt2zh/index.html

###服务端返回的格式为:
    {'code':200,'content':{}}

    大部分是这样的
	code表示此次请求成功或者失败
    content是返回内容，可能不同api返回会有一点差别(具体见api函数的注释)
    code表:
        200:成功
        400：参数缺少
        401：密码错误
        402:其他类型错误
        403：权限不够
        500；系统错误

