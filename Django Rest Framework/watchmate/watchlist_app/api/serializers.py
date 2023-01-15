from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'

        # exclude = ['active']
        # fields = ['id', 'name']

    # def get_len_name(self, object):
    #     return len(object.title)

    # def validate_title(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Title should be > 3 characters")
    #     else:
    #         return value

    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Name and Description should not be same")
    #     else:
    #         return data


class StreamPlatformSerializer(serializers.ModelSerializer):
    # class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-details'
    # )

    class Meta:
        model = StreamPlatform
        fields = '__all__'


# def title_validator(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name should be > 3 characters")
#     else:
#         return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_validator])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance

#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Name should be > 3 characters")
#         else:
#             return value

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Name and Description should not be same")
#         else:
#             return data
