from django.forms import ModelForm
from models import *
from django.db.models import Q


class CategoryForm(ModelForm):
	
	class Meta:
		model = Category
		exclude = ('slug',)

	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		if self.instance.id:
			excluded = Category.objects.exclude(Q(parent__id__exact=self.instance.id) | Q(id__exact=self.instance.id))
			self.fields['parent'].choices = excluded.values_list('id','title')
			self.fields['parent'].choices = [('', '---------')]+self.fields['parent'].choices

class ArticleForm(ModelForm):
	
	class Meta:
		model = Article
		exclude = ('hits', 'slug')

	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)
		self.fields['related_articles'].choices = Article.objects.exclude(id__exact=self.instance.id).values_list('id','title')