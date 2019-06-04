# My_blog

## Day01

## 1. 在github上创建一个My_blog的项目

## 2. 在笔记本电脑任意目录上，打开终端
git clone git@github.com:liyuan3970/My_blog.git

## 3. 进入这个文件夹 
cd My_blog

## 4. 创建一个虚拟环境　
python -m venv env

## 5. 启动虚拟环境 source env/bin/active   && 终止虚拟环境　deactivate

## 6. 安装django--->
pip install django==1.11.8

## 7. 创建一个django项目---> 
django-admin startproject My_blog

## 8. 创建生产开发环境
1. 在My_blog/My_blog下创建settings文件夹
2. 在settings文件夹下创建product.py(实际上就是settings.py)
3. 修改wsgi.py 和 manage.py两个文件

   ```python
   profile = os.environ.get('MY_BLOG_PROFILE', 'product')
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_blog.settings.%s" % profile)
   #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_blog.settings")
   ```
   以上的步骤的作用是修改默认启动的settings文件　
## 9. 创建app
python manage.py startapp blog<br>
python manage.py startapp config<br>
python manage.py startapp comment<br>