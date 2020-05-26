from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    """新闻表单数据验证"""
    title = StringField(label='新闻标题', validators=[DataRequired('请输入标题')],
                        description='请输入标题',
                        render_kw={'required': 'required', 'class': 'form-control'})
    content = TextAreaField(label='新闻内容', validators=[DataRequired('请输入新闻内容')],
                            description='请输入新闻内容',
                            render_kw={'required': 'required', 'class': 'form-control'})
    types = SelectField('新闻类型', choices=[('推荐', '推荐'), ('时政新闻', '时政新闻'), ('娱乐', '娱乐')])
    image = StringField(label='新闻图片', description='请输入图片地址',
                        render_kw={'required': 'required', 'class': 'form-control'})
    author = StringField(label='作者', validators=[DataRequired('请输入作者笔名')],
                         description='请输入作者笔名', render_kw={'required': 'required', 'class': 'form-control'})
    submit = SubmitField('提交')
