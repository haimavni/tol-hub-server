db.define_table('TblCustomemrs', 
    Field('subdomain', type='string'),
    Field('app_name', type='string'), #may be different from subdomain to allow auto generated databases
    Field('manager_user_id', type=db.auth_user)
)

x = 99999
y = x