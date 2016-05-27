ModelName.objects.all()
ModelName.objects.create()
ModelName.objects.all()
ModelName.objects.filter(property='valuee', anotherproperty='value', etc...)
ModelName.objects.get(name="Apress")
ModelName.objects.order_by("name")

chaining:
ModelName.objects.order_by("name").filter(property="value")

slicing:
ModelName.objects.order_by('name')[0:2]

update multiple:
Publisher.objects.filter(id=52).update(name='Apress Publishing')

ModelName.objects.foo.delete()
