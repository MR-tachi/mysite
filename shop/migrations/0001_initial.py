# Generated by Django 4.0 on 2022-08-11 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateField()),
                ('informations', models.TextField(null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desciption', models.TextField(blank=True, max_length=300, null=True)),
                ('dkp', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('createDate', models.DateField(null=True)),
                ('averageRating', models.IntegerField(blank=True, null=True)),
                ('ratingCount', models.IntegerField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('category', models.ManyToManyField(to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='VariantProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('dkpc', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('size', models.IntegerField()),
                ('mainPrice', models.IntegerField()),
                ('discountPrice', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('createDate', models.DateField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationaID', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('mobilephone', models.CharField(blank=True, max_length=11, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=10, null=True)),
                ('cardNumber', models.CharField(blank=True, max_length=24, null=True)),
                ('createDate', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('createDate', models.DateField()),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('d', 'delivered'), ('o', 'onway'), ('r', 'refunded')], default='o', max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
                ('variantProduct', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.variantproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('createDate', models.DateField(null=True)),
                ('shopCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopcart')),
                ('variantProduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.variantproduct')),
            ],
        ),
    ]
