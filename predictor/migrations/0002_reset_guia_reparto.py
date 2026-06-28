from django.db import migrations


def reset_reparto(apps, schema_editor):
    GuiaReparto = apps.get_model('predictor', 'GuiaReparto')
    GuiaReparto.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(reset_reparto, migrations.RunPython.noop),
    ]
