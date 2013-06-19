from app import db
from flask.ext.mongoengine.wtf import model_form

class User(db.Document):
	email = db.StringField(required=True)
	first_name = db.StringField(max_length=50)
	last_name = db.StringField(max_length=50)

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Content(db.EmbeddedDocument):
	text = db.StringField()
	lang = db.StringField(max_length=3)

class Entry(db.Document):
	title = db.StringField(max_length=120, required=True)
	author = db.ReferenceField(User)
	tags = db.ListField(db.StringField(max_length=30))
	content = db.EmbeddedDocumentField(Content)

InsertEntry = model_form(Entry)

def add_entry(request):
	form = InsertEntry(request.POST)
	if request.method == 'POST' and form.validate():
		redirect('done')
	return render_response('about.html', form=form)