# Queryset Optimization

**related Chapter 7.2.6**

7.2에서 만든 Action 모델: 객체 조회 때마다 참조하는 다른 모델들 빈번하게 조회

Django ORM의 동시조회 기능 사용하기 (SQL Join 수행)

* `model.selected_related()`
* `model.prefetch_related()`

적용례: [dashboard view](../bookmarks/account/views.py)
