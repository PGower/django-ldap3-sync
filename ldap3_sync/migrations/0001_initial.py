# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LDAPConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('auto_bind', models.CharField(choices=[(b'AUTO_BIND_NONE', b'ldap3.AUTO_BIND_NONE'), (b'AUTO_BIND_NO_TLS', b'ldap3.AUTO_BIND_NO_TLS'), (b'AUTO_BIND_TLS_BEFORE_BIND', b'ldap3.AUTO_BIND_TLS_BEFORE_BIND'), (b'AUTO_BIND_TLS_AFTER_BIND', b'ldap3.AUTO_BIND_TLS_AFTER_BIND')], default=b'AUTO_BIND_NONE', max_length=128)),
                ('version', models.PositiveIntegerField(default=3)),
                ('authentication', models.CharField(blank=True, choices=[(b'ANONYMOUS', b'ldap3.ANONYMOUS'), (b'SIMPLE', b'ldap3.SIMPLE'), (b'SASL', b'ldap3.SASL'), (b'NTLM', b'ldap3.NTLM')], max_length=128, null=True)),
                ('client_strategy', models.CharField(choices=[(b'SYNC', b'ldap3.SYNC'), (b'ASYNC', b'ldap3.ASYNC'), (b'LDIF', b'ldap3.LDIF'), (b'RESTARTABLE', b'ldap3.RESTARTABLE'), (b'REUSABLE', b'ldap3.REUSABLE'), (b'MOCK_SYNC', b'ldap3.MOCK_SYNC'), (b'MOCK_ASYNC', b'ldap3.MOCK_ASYNC')], default=b'SYNC', max_length=128)),
                ('auto_referrals', models.BooleanField(default=True)),
                ('sasl_mechanism', models.CharField(blank=True, choices=[(b'EXTERNAL', b'ldap3.EXTERNAL'), (b'DIGEST_MD5', b'ldap3.DIGEST_MD5'), (b'KERBEROS', b'ldap3.KERBEROS'), (b'GSSAPI', b'ldap3.GSSAPI')], max_length=128, null=True)),
                ('sasl_credential', models.CharField(help_text=b'Path to an object to use as the SASL Credential.', max_length=255)),
                ('read_only', models.BooleanField(default=False)),
                ('lazy', models.BooleanField(default=False)),
                ('check_names', models.BooleanField(default=True)),
                ('collect_usage', models.BooleanField(default=False)),
                ('raise_exceptions', models.BooleanField(default=False)),
                ('pool_name', models.CharField(blank=True, max_length=255, null=True)),
                ('pool_size', models.PositiveIntegerField(blank=True, null=True)),
                ('pool_lifetime', models.PositiveIntegerField(blank=True, null=True)),
                ('fast_decoder', models.BooleanField(default=True)),
                ('receive_timeout', models.PositiveIntegerField(blank=True, null=True)),
                ('return_empty_attributes', models.BooleanField(default=True)),
                ('use_referral_cache', models.BooleanField(default=False)),
                ('auto_escape', models.BooleanField(default=True)),
                ('auto_encode', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LDAPPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('exhaust', models.BooleanField(default=False)),
                ('pool_strategy', models.CharField(blank=True, choices=[(b'FIRST', b'ldap3.FIRST'), (b'ROUND_ROBIN', b'ldap3.ROUND_ROBIN'), (b'RANDOM', b'ldap3.RANDOM')], max_length=128, null=True)),
                ('connection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pool', to='ldap3_sync.LDAPConnection')),
            ],
        ),
        migrations.CreateModel(
            name='LDAPReferralHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
                ('allowed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LDAPServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255)),
                ('port', models.PositiveIntegerField(blank=True, null=True)),
                ('use_ssl', models.BooleanField(default=False)),
                ('get_info', models.CharField(blank=True, choices=[(b'GET_NO_INFO', b'ldap3.GET_NO_INFO'), (b'GET_DSA_INFO', b'ldap3.GET_DSA_INFO'), (b'GET_SCHEMA_INFO', b'ldap3.GET_SCHEMA_INFO'), (b'GET_ALL_INFO', b'ldap3.GET_ALL_INFO')], max_length=128, null=True)),
                ('mode', models.CharField(blank=True, choices=[(b'IP_SYSTEM_DEFAULT', b'ldap3.IP_SYSTEM_DEFAULT'), (b'IP_V4_ONLY', b'ldap3.IP_V4_ONLY'), (b'IP_V6_ONLY', b'ldap3.IP_V6_ONLY'), (b'IP_V4_PREFERRED', b'ldap3.IP_V4_PREFERRED'), (b'IP_V6_PREFERRED', b'ldap3.IP_V6_PREFERRED')], max_length=128, null=True)),
                ('connect_timeout', models.PositiveIntegerField(blank=True, null=True)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servers', to='ldap3_sync.LDAPConnection')),
            ],
        ),
        migrations.CreateModel(
            name='LDAPSyncJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'likely.sharp.ocelot', max_length=255, unique=True)),
                ('ldap_base_dn', models.TextField()),
                ('ldap_search_filter', models.TextField()),
                ('removal_action', models.CharField(choices=[(1, b'Nothing'), (2, b'DELETE'), (3, b'Function')], max_length=50)),
                ('removal_function', models.CharField(max_length=255)),
                ('ldap_connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldap3_sync.LDAPConnection')),
                ('target_django_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='LDAPSyncRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('distinguished_name', models.TextField(help_text=b'DO NOT edit this unless you really know what your doing. It is much safer to delete this entire record and let the sync command recreate it.')),
                ('object_id', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'LDAP Sync Record',
                'verbose_name_plural': 'LDAP Sync Records',
            },
        ),
        migrations.AddField(
            model_name='ldapreferralhost',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed_referral_hosts', to='ldap3_sync.LDAPServer'),
        ),
        migrations.AlterUniqueTogether(
            name='ldapsyncrecord',
            unique_together=set([('distinguished_name', 'content_type', 'object_id')]),
        ),
    ]
