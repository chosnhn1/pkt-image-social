# Data denormalization on django

## Using signals

i.e. Image 모델의 총 좋아요 수를 합산하여 정렬하는 view

on view:

`images_by_popularity = Image.objects.annotate(total_likes=Count('users_like)).order_by('-total_likes')`

vs.

on model:

`total_likes = models.PositiveIntergerField(default=0)`


