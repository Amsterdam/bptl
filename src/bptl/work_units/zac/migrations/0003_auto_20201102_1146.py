# Generated by Django 2.2.14 on 2020-11-02 10:46

from django.db import migrations

from zgw_consumers.constants import APITypes, AuthTypes


def refactor_configuration_forward(apps, schema_editor):
    Service = apps.get_model("zgw_consumers", "Service")
    ZACConfig = apps.get_model("zac", "ZACConfig")
    configuration = ZACConfig.objects.first()
    if configuration is None:
        return
    configuration.service = Service.objects.create(
        label="ZAC",
        api_type=APITypes.orc,
        api_root=configuration.api_root,
        auth_type=AuthTypes.api_key,
        header_key=configuration.header_key,
        header_value=configuration.header_value,
    )
    configuration.save()


def refactor_configuration_backwards(apps, schema_editor):
    ZACConfig = apps.get_model("zac", "ZACConfig")
    configuration = ZACConfig.objects.first()
    if configuration is None:
        return
    configuration.api_root = configuration.service.api_root
    configuration.header_value = configuration.service.header_value
    configuration.header_key = configuration.service.header_key
    configuration.save()


class Migration(migrations.Migration):

    dependencies = [
        ("zgw_consumers", "0011_remove_service_extra"),
        ("zac", "0002_zacconfig_service"),
    ]

    operations = [
        migrations.RunPython(
            refactor_configuration_forward, refactor_configuration_backwards
        )
    ]
