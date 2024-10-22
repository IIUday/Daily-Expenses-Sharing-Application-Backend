from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    mobile = fields.Str(required=True)

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    amount = fields.Float(required=True)
    paid_by = fields.Int(required=True)
    split_method = fields.Str(required=True)
    split_details = fields.Dict(required=True)
    participants = fields.List(fields.Int(), required=True)
    date = fields.DateTime(dump_only=True)
