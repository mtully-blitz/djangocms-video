# -*- coding: utf-8 -*-

'''
WARNING: This is a fix for original migration 0004[1] (failing in some old versions of postgresql[2]).
Fix was added way after 0004 was created (at writing time we are on migration 0009), and is based on a similar django CMS issue[3].

[1] https://github.com/divio/djangocms-video/blob/2.0.4/djangocms_video/migrations/0004_move_to_attributes.py
[2] https://github.com/divio/djangocms-video/issues/34
[3] https://github.com/divio/django-cms/pull/6322
'''
from __future__ import unicode_literals

from django.db import migrations, models

try:
    IrreversibleError = migrations.Migration.IrreversibleError
except AttributeError:
    from django.db.migrations.exceptions import IrreversibleError


class Migration(migrations.Migration):
    dependencies = [
        ('djangocms_video', '0003_field_adaptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoplayer',
            name='migration_0004_control',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

    def unapply(self, project_state, schema_editor, collect_sql=False):
        raise IrreversibleError('Migration %s is not reversible' % self.name)
