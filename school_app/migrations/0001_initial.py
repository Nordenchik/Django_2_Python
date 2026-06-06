import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name = 'Question',
            fields = [
                ('question_id', models.BigAutoField(primary_key = True, serialize = False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name = 'Quiz',
            fields = [
                ('quiz_id', models.BigAutoField(primary_key = True, serialize = False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name = 'Option',
            fields = [
                ('option_id', models.BigAutoField(primary_key = True, serialize = False)),
                ('content', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'options', to = 'app.question')),
            ],
        ),
        migrations.AddField(
            model_name = 'question',
            name = 'quiz',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'questions', to = 'app.quiz'),
        ),
    ]