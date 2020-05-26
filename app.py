from datetime import datetime

from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import NewsForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/newsystem?charset=utf8'
app.config["SECRET_KEY"] = "12345678"

db = SQLAlchemy(app)


# 新闻类型
class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(1300), )
    author = db.Column(db.String(20), )
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/index/')
def index():
    # 新闻首页
    news_list = News.query.all()
    # print(news_list)
    return render_template('index.html', news_list=news_list)


@app.route('/')
def index_html():
    # 新闻首页
    news_list = News.query.all()
    return redirect('/')


@app.route('/cat/<name>/')
def category(name):
    # 查询新闻类别
    news_list = News.query.filter(News.types == name)
    return render_template('category.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    # 查询新闻的详细信息
    obj = News.query.get(pk)
    return render_template('detail.html', obj=obj)


# 数据后端
@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    '''后台新闻列表'''
    if page is None:
        page = 1
    news_list = News.query.filter_by(is_valid=True).paginate(page=page, per_page=3)

    return render_template('admin/index.html', news_list=news_list)


@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def admin_update(pk):
    '''后台新闻列表'''
    new_obj = News.query.get(pk)
    print('admin_update:new_obj %s' % new_obj)
    if not new_obj:
        return redirect(url_for('admin'))

    form = NewsForm(obj=new_obj)
    if form.validate_on_submit():
        new_obj.title = form.title.data
        new_obj.content = form.content.data
        new_obj.types = form.types.data
        new_obj.created_at = datetime.now()
        # 保存数据
        db.session.add(new_obj)
        db.session.commit()

        # 文字提示flash消息闪现
        flash('修改成功')
        return redirect('/admin/')

    return render_template('admin/update.html', new_obj=new_obj, form=form)


@app.route('/admin/add/')
def admin_add():
    '''跳转到后台新闻列表'''
    form = NewsForm()
    return render_template('admin/add.html', form=form)


@app.route('/admin/do_add/', methods=['POST'])
def admin_do_add():
    ''' 新增新闻信息 '''
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            types=form.types.data,
            image=form.image.data,
            created_at=datetime.now()
        )
        # 保存数据
        db.session.add(new_obj)
        db.session.commit()

        # 文字提示flash消息闪现
        flash('添加成功')
    return redirect('/admin/')


@app.route('/admin/delete/<int:pk>/', methods=['GET', 'POST'])
def admin_delete(pk):
    ''' 删除新闻信息 '''
    new_obj = News.query.get(pk)

    if not new_obj:
        return redirect('/404/')
    db.session.delete(new_obj)
    db.session.commit()
    return redirect('/admin/')

if __name__ == '__main__':
    app.run(debug=True)
