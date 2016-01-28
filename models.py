def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).
                                    values_list('pk', flat=True))
        elif isinstance(f, models.DateField):
            data[f.name] = f.value_from_object(instance).strftime("%d.%m.%Y")
        elif isinstance(f, models.ForeignKey):
            relFtr = f.value_from_object(instance)
            if hasattr(relFtr, "to_dict"):
                data[f.name] = relFtr.to_dict()
            else:
                data[f.name] = unicode(relFtr)
        else:
            data[f.name] = f.value_from_object(instance)
    return data

def __getitem__(self, field):
    if hasattr(self, field):
        return getattr(self, field)
    else:
        raise AttributeError('Models not get AbstractTelemetryValue not attribute' +
                             field + str(type(field)))

def __setitem__(self, field, value):
    if hasattr(self, field):
        setattr(self, field, value)
    else:
        raise AttributeError('Models not set AbstractTelemetryValue not attribute' +
                             field + str(type(field)))