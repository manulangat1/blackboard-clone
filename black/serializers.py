from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User,Assignment,GradedAssignment,Question,Choice

class UserSerializer(serializers.ModelSerializer):
    # user_type = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('username','is_student','is_teacher','email')
####Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','is_student','is_teacher','email')
        extra_kwargs = {"password":{'write_only':True}}

        def create(self,validated_data):
            user = User.objects.create_user(validated_data['username'],validated_data['password'],validated_data['is_student'],validated_data['is_teacher'],validated_data['email'])
            return user
###Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("incoreect credentials")

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self,value):
        return value
class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'  
class AssignmentSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    teacher = StringSerializer()
    class Meta:
        model = Assignment
        fields = '__all__'
    def get_questions(self,obj):
        questions = QuestionSerializer(obj.questions.all(),many=True).data
        return questions
class GradedAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradedAssignment
        fields = '__all__'
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
