# Queryset Optimization

**related Chapter 7.2.6**

7.2에서 만든 Action 모델: 객체 조회 때마다 참조하는 다른 모델들 빈번하게 조회

Django ORM의 동시조회 기능 사용하기 (SQL Join 수행)

* `model.selected_related()`\
  * used in 1:M rel
* `model.prefetch_related()`
  * used in M:N, M:1 rel

* 적용례: [dashboard view](../bookmarks/account/views.py)
* 관련 링크
  * 공식문서 (models / querysets)
    * [selected_related](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#select-related)
    * [prefetch_related](https://docs.djangoproject.com/en/5.2/ref/models/querysets/#prefetch-related)