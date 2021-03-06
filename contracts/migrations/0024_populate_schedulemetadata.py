# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-19 20:30
from __future__ import unicode_literals
from textwrap import dedent

from django.db import migrations


def create_schedules(apps, schema_editor):
    ScheduleMetadata = apps.get_model('contracts', 'ScheduleMetadata')
    ScheduleMetadata(
        sin='899',
        schedule='Environmental',
        name='Legacy Environmental',
        description=dedent('''
        Provides services in environmental management, electronics stewardship,
        pollution prevention cleanup and restoration, HAZMAT, and training.
        '''),
    ).save()
    ScheduleMetadata(
        sin='87405',
        schedule='Logistics',
        name='Legacy Logistics',
        description=dedent('''
        Provides services (including deployment of supplies, equipment,
        materials and personnel) in the areas of planning acquisition and
        management of logistics system, expert advice, assistance,
        guidance, management, and operational support services. Various
        types of training are also available.

        This schedule was formerly known as Logistics Worldwide (LOGWORLD).
        '''),
    ).save()
    ScheduleMetadata(
        sin='874',
        schedule='MOBIS',
        name='Legacy MOBIS',
        description=dedent('''
        Mission Oriented Business Integrated Services (MOBIS) provides management
        and consulting services, including facilitation,
        surveys, competetive sourcing and project management.
        '''),
    ).save()
    ScheduleMetadata(
        sin='871',
        schedule='PES',
        name='Legacy PES',
        description=dedent('''
        Covers engineering disciplines, including mechanical, electrical,
        chemical, civil, software, aerospace, nuclear, bio, fire protection,
        and marine.

        This schedule was formerly known as the Professional Engineering Schedule.
        '''),
    ).save()
    ScheduleMetadata(
        sin='73802',
        schedule='Language Services',
        name='Legacy Language',
        description=dedent('''
        Provides a range of services, from basic transcribing to
        advance analytical consulting. Sign language and training
        are also offered.
        '''),
    ).save()
    ScheduleMetadata(
        sin='541',
        schedule='AIMS',
        name='Legacy AIMS',
        description=dedent('''
        Advertising and Integrated Marketing Schedules (AIMS) provides
        advertising, marketing and related communications
        fields, including web & graphic design, direct mail
        campaigns, etc.

        *Note: AIMS is newly added so available results in CALC is
        currently limited.*
        '''),
    ).save()
    ScheduleMetadata(
        sin='520',
        schedule='FABS',
        name='Legacy FABS',
        description=dedent('''
        Includes services for asset management, financial management,
        auditing, business information, program management and
        grant management.

        *Note: FABS is newly added so available results in CALC is
        currently limited.*
        '''),
    ).save()
    ScheduleMetadata(
        schedule='Consolidated',
        name='The Consolidated Schedule',
        description=dedent('''
        Covers contracts awarded to a single company for services that
        cover multiple schedules.
        '''),
    ).save()
    ScheduleMetadata(
        sin='132',
        schedule='IT Schedule 70',
        name='IT Schedule 70',
        description=dedent('''
        IT Schedule 70 offers federal, state and local governments
        innovative solutions to their information technology needs.

        *Note: IT Schedule 70 is newly added so available results
        in CALC is currently limited.*
        '''),
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0023_schedulemetadata'),
    ]

    operations = [
        migrations.RunPython(create_schedules)
    ]
