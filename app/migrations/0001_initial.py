# Generated by Django 4.2.7 on 2023-12-08 22:13

import app.models
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=False, verbose_name='Prix')),
                ('paid_status', models.BooleanField(default=False, verbose_name='Statut de paiement')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de commande')),
                ('product_status', models.CharField(choices=[('traitement', 'Traitement'), ('expedier', 'Expédié'), ('Livrer', 'Livré')], default='traitement', max_length=15, verbose_name='Statut du produit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Panier de commande',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='cat', unique=True)),
                ('title', models.CharField(max_length=150, verbose_name='Nom')),
                ('image', models.ImageField(default='category.jpg', upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='', unique=True)),
                ('title', models.CharField(default='Hp', max_length=150, verbose_name='Nom')),
                ('image', models.ImageField(default='product.jpg', upload_to=app.models.user_dictory_path)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default="C'est un bon produit", null=True)),
                ('price', models.IntegerField(default=0, verbose_name='Prix')),
                ('old_price', models.IntegerField(default=0, verbose_name='Prix Promo')),
                ('specification', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('type', models.CharField(blank=True, default='Outils', max_length=150, null=True)),
                ('stock_account', models.CharField(blank=True, default=8, max_length=100, null=True, verbose_name='Compte de stock')),
                ('life', models.CharField(blank=True, default='100', max_length=100, null=True, verbose_name='Vie')),
                ('mfd', models.DateTimeField(blank=True, null=True)),
                ('product_status', models.CharField(choices=[('brouillon', 'Brouillon'), ('desactiver', 'Désactivé'), ('rejeter', 'Rejeté'), ('en_revue', 'En revue'), ('publier', 'Publié')], default='Statut du produit', max_length=15)),
                ('status', models.BooleanField(default=False)),
                ('in_stock', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('digital', models.BooleanField(default=False)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=10, prefix='sku', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app.category', verbose_name='Catégorie')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product', verbose_name='Produit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Liste de voeux',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='ven', unique=True)),
                ('title', models.CharField(default='Bon fournisseur', max_length=150, verbose_name='Nom')),
                ('image', models.ImageField(default='fournisseur.jpg', upload_to=app.models.user_dictory_path)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='Je suis un fournisseur incroyable', null=True)),
                ('address', models.CharField(default='Conakry/Kaloum/Sans-fil', max_length=150, verbose_name='Adresse')),
                ('contact', models.CharField(default='+224669016140', max_length=150)),
                ('chat_resp_time', models.CharField(default='100', max_length=150)),
                ('shipping_on_time', models.CharField(default='100', max_length=150)),
                ('authentic_rating', models.CharField(default='100', max_length=150)),
                ('days_return', models.CharField(default='100', max_length=150)),
                ('warranty_period', models.CharField(default='100', max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Fournisseurs',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Avis')),
                ('rating', models.IntegerField(choices=[(1, '★✩✩✩'), (2, '★★✩✩✩'), (3, '★★★✩✩'), (4, '★★★★✩'), (5, '★★★★★')], default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='app.product', verbose_name='review')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Avis sur les produits',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='app.product')),
            ],
            options={
                'verbose_name_plural': 'Images du produit',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='app.vendor', verbose_name='Fournisseur'),
        ),
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=200)),
                ('product_status', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200, verbose_name='Article')),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField(default=0, verbose_name='Quantité')),
                ('price', models.IntegerField(default=0, verbose_name='Prix')),
                ('total', models.IntegerField(default=0, verbose_name='Total')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cartorder', verbose_name='Commande')),
            ],
            options={
                'verbose_name_plural': 'Panier de commande art',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name_plural': 'Adresse',
            },
        ),
    ]
