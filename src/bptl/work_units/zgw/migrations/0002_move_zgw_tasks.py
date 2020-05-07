# Generated by Django 2.2.10 on 2020-04-10 09:00

from django.db import migrations
from django.db.models import Case, Value, When

PREFIX = "bptl.work_units.zgw.tasks"
MAPPING = {
    f"{PREFIX}.CreateZaakTask": f"{PREFIX}.zaak.CreateZaakTask",
    f"{PREFIX}.CloseZaakTask": f"{PREFIX}.zaak.CloseZaakTask",
    f"{PREFIX}.CreateStatusTask": f"{PREFIX}.status.CreateStatusTask",
    f"{PREFIX}.CreateResultaatTask": f"{PREFIX}.resultaat.CreateResultaatTask",
    f"{PREFIX}.RelateDocumentToZaakTask": f"{PREFIX}.zaak_relations.RelateDocumentToZaakTask",
    f"{PREFIX}.RelatePand": f"{PREFIX}.zaak_relations.RelatePand",
}


def do_update(apps, mapping: dict):
    TaskMapping = apps.get_model("tasks", "TaskMapping")
    whens = [When(callback__exact=old, then=Value(new)) for old, new in mapping.items()]
    TaskMapping.objects.filter(callback__in=mapping).update(callback=Case(*whens))


def forwards(apps, _):
    do_update(apps, MAPPING)


def backwards(apps, _):
    do_update(apps, {value: key for key, value in MAPPING.items()})


class Migration(migrations.Migration):

    dependencies = [
        ("zgw", "0001_initial"),
        ("tasks", "0008_auto_20200228_1616"),
    ]

    operations = [migrations.RunPython(forwards, backwards)]