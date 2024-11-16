from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    chat_type = fields.CharField(max_length=20, default='private')
    language = fields.CharField(max_length=30, null=True)
    user_type = fields.CharField(max_length=30, default='user')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'users'
