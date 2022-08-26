# Двойная связь между моделями

Если связывать две модели простым отношением, алхимия догадается, 
какой внешний ключ использовать. Если же у нас есть две связи и два внешних ключа, 
ключи нужно явно распределить между отношениями, указав foreign_keys.

```
owner = db.relationship("UserModel", foreign_keys=[owner_pk])
performer = db.relationship("UserModel", foreign_keys=[performer_pk])
    
```
