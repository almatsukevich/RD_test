
from rest_framework.routers import DefaultRouter
from .views import EmployeeView #, LevelView

router = DefaultRouter()
router.register(r'employees', EmployeeView, basename='user')
urlpatterns = router.urls

