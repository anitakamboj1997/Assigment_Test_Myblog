from django.contrib import admin
from django.apps import apps
# Register your models here.
apps_to_register = ["blog"]
models = [model for app in apps_to_register for model in apps.all_models[app].values()]
print(models)
for model in models:
    char_fields = []
    other_fields = []
    for field in model._meta.fields:
        if field.get_internal_type() == "CharField":
            char_fields.append(field.name)
        else:
            other_fields.append(field.name)

    try:
        admclass = type(
            f"{model._meta.model.__name__}Admin",
            (admin.ModelAdmin,),
            {"list_display": char_fields + other_fields},
        )
        admin.site.register(model, admclass)
    except admin.sites.AlreadyRegistered:
        pass
    except Exception as msg:
        print(msg)