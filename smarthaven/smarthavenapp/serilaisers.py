from django.core import serializers

from models import alerttable, complainttable, controltable, friendtable, logintable, managementtable, remaindertable, usertable


class logintableseriliazers(serializers.ModelSerializer):
    class Meta:
        model=logintable
        fields=['username','password','usertype']
class usertableserializers(serializers.ModelSerializers):
    class Meta:
        model=usertable
        fields=['user','login_id','name','address','phone','email']
class alerttableserializers(serializers.ModelSerializers):
    class Meta:
        model=alerttable
        fields=['fieldname','alert_id','login_id','alert_type','alert_message','alert_date','alert_time','status']
class friendtableserializers(serializers.ModelSerializers):
    class Meta:
        model=friendtable
        fields=['field_id','user_id','friend_user_id','date','status']
class remindertableserializers(serializers.ModelSerializers):
    class Meta:
        model=remaindertable
        fields=['reminder_id','user_id','title','desciption','reminder_date','reminder_time','status']
class managementtableserializers(serializers.ModelSerializers):
    class Meta:
        model=managementtable
        fields=['management_id','login_id','emergency_number','description','created_date','status']
class controltableserializers(serializers.ModelSerializers):
    class Meta:
        model=controltable
        fields=['control_id','user_id','device_name','device_type','device_status','update_date']
class complainttableserializers(serializers.ModelSerializers):
    class Meta:
        model=complainttable
        fields=['complaint_id','user_id','complaint_titl','complaint_description','complaint_date','reply','reply_date','status']
        




            