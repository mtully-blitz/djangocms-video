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
        ('djangocms_video', '0004_1_migrate_data_attributes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoplayer',
            name='auto_hide',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='auto_play',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='bgcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='buttonhighlightcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='buttonoutcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='buttonovercolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='fullscreen',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='height',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='loadingbarcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='loop',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='seekbarbgcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='seekbarcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='textcolor',
        ),
        migrations.RemoveField(
            model_name='videoplayer',
            name='width',
        ),

        migrations.RemoveField(
            model_name='videoplayer',
            name='migration_0004_control',
        ),
    ]

    def apply(self, project_state, schema_editor, collect_sql=False):
        connection = schema_editor.connection
        column_names = [
            column.name for column in
            connection.introspection.get_table_description(connection.cursor(), 'djangocms_video_videoplayer')
        ]
        if 'migration_0004_control' in column_names:
            # The new 0004 migration has been applied
            return super(Migration, self).apply(project_state, schema_editor, collect_sql)

        # The old 0004 migration was applied
        # Move the project state forward without actually running
        # any of the operations against the database.
        for operation in self.operations:
            operation.state_forwards(self.app_label, project_state)
        return project_state

    def unapply(self, project_state, schema_editor, collect_sql=False):
        raise IrreversibleError('Migration %s is not reversible' % self.name)
