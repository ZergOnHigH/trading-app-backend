from marshmallow import Schema, fields, validate

class TaskModel(Schema):
    nazwa = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    opis = fields.Str(required=False, allow_none=True)
    priorytet = fields.Str(required=True, validate=validate.OneOf(["niski", "średni", "wysoki"]))
    termin = fields.DateTime(required=True)